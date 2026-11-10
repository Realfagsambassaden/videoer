import subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter
A=29.95; FPS=30; X0,Y0,CW,CH=294,262,432,768
FF=np.load('FF.npy'); M=np.load('M.npy'); n=len(FF)
# grovt spor (fullbilde-koordinater) fra håndsporing, finjusteres lokalt
S=[(30.03,234,441,24),(30.17,231,452,26),(30.3,225,462,28),(30.43,231,471,30),(30.57,228,474,32),(30.7,216,489,36),(30.83,204,504,40),(30.97,195,519,44),(31.1,204,546,50),(31.23,249,579,56),(31.37,270,621,62),(31.5,264,660,68)]
T=np.array([s[0] for s in S])
def grov(t): return np.interp(t,T,[s[1]+270 for s in S]),np.interp(t,T,[s[2]+96 for s in S]),np.interp(t,T,[s[3] for s in S])
P=[]
for i in range(n):
    t=A+i/FPS; x,y,d=grov(t); r=int(d*0.9)
    x0,y0=int(x-r),int(y-r); w=FF[i][y0:y0+2*r,x0:x0+2*r].astype(int)
    m=(w.min(2)>160)&((w.max(2)-w.min(2))<70)
    if m.sum()>20: ys,xs=np.nonzero(m); x,y=x0+xs.mean(),y0+ys.mean()
    P.append((x,y,d))
def til_ref(i,x,y): Tm=M[i]; return Tm@np.array([x,y,1.0])
def fra_ref(j,p): Tm=np.vstack([M[j],[0,0,1]]); return (np.linalg.inv(Tm)@np.array([p[0],p[1],1.0]))[:2]
gi=[i for i in range(n) if 30.03<=A+i/FPS<=31.5 and i%4==0]
G=[]
for i in gi:
    x,y,d=P[i]; r=int(d*0.62)+4; patch=FF[i][int(y)-r:int(y)+r,int(x)-r:int(x)+r].copy()
    mask=Image.new('L',(2*r,2*r),0); ImageDraw.Draw(mask).ellipse((4,4,2*r-4,2*r-4),fill=255); mask=mask.filter(ImageFilter.GaussianBlur(2))
    G.append((i,til_ref(i,x,y),Image.fromarray(patch),mask,r))
def ramme(j,antall):
    im=Image.fromarray(FF[j])
    for (i,p0,patch,mask,r) in G[:antall]:
        if i>=j and antall<len(G): continue
        x,y=fra_ref(j,p0); im.paste(patch,(int(x)-r,int(y)-r),mask.point(lambda v:int(v*0.75)))
    im=im.crop((X0,Y0,X0+CW,Y0+CH)).resize((1080,1920),Image.LANCZOS)
    return im
ut=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-c:v','libx264','-crf','16','-preset','veryfast','-pix_fmt','yuv420p','spol.mp4'],stdin=subprocess.PIPE)
def skriv(im): ut.stdin.write(np.asarray(im.convert('RGB')).tobytes())
L={'a':0,'b':0,'c':0}
for i in range(n):                                   # 1) sakte, uten opptegning
    for _ in range(2): skriv(ramme(i,0)); L['a']+=1
for i in range(n-1,-1,-3): skriv(ramme(i,0)); L['b']+=1   # 2) spol tilbake
for i in range(n):                                   # 3) på nytt, banen tegnes opp
    k=sum(1 for g in G if g[0]<=i)
    for _ in range(2): skriv(ramme(i,k)); L['c']+=1
for _ in range(20): skriv(ramme(n-1,len(G))); L['c']+=1
ut.stdin.close(); ut.wait(); print({k:v/30 for k,v in L.items()}, sum(L.values())/30)
