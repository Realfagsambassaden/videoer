import subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFilter
SRC='/home/claude/kilder/sn_5743.mov'; A,B=29.95,31.6; FPS=30
X0,Y0,CW,CH=294,262,432,768          # utsnitt 2.5x
raw=subprocess.run(['ffmpeg','-v','error','-ss',str(A),'-t',str(B-A),'-i',SRC,'-vf',f'fps={FPS},crop={CW}:{CH}:{X0}:{Y0},scale=1080:1920:flags=lanczos','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
F=np.frombuffer(raw,np.uint8).reshape(-1,1920,1080,3); n=len(F); print('rammer',n)
# håndsporet bane (i 540x960-utsnittet fra x=270,y=96): t, x, y, diameter
S=[(30.03,234,441,24),(30.17,231,452,26),(30.3,225,462,28),(30.43,231,471,30),(30.57,228,474,32),(30.7,216,489,36),(30.83,204,504,40),(30.97,195,519,44),(31.1,204,546,50),(31.23,249,579,56),(31.37,270,621,62),(31.5,264,660,68)]
T=np.array([s[0] for s in S])
def pos(t):
    x=np.interp(t,T,[s[1] for s in S])+270-X0; y=np.interp(t,T,[s[2] for s in S])+96-Y0; d=np.interp(t,T,[s[3] for s in S])
    k=1080/CW; return x*k,y*k,d*k
# finjuster sentrum per ramme mot lyseste runde flekk nær anslaget
def finn(f,t):
    x,y,d=pos(t); r=int(d*0.9); x0,y0=int(max(x-r,0)),int(max(y-r,0)); w=f[y0:int(y+r),x0:int(x+r)].astype(int)
    if w.size==0: return x,y,d
    m=(w.min(2)>160)&((w.max(2)-w.min(2))<70)
    if m.sum()<30: return x,y,d
    ys,xs=np.nonzero(m); return x0+xs.mean(),y0+ys.mean(),d
P=[finn(F[i],A+i/FPS) for i in range(n)]
gi=[i for i in range(n) if A+i/FPS>=30.03 and i%4==0 and A+i/FPS<=31.5]
def spokelse(f,p):
    x,y,d=p; r=d*0.62; im=Image.fromarray(f); mask=Image.new('L',im.size,0)
    ImageDraw.Draw(mask).ellipse((x-r,y-r,x+r,y+r),fill=255); mask=mask.filter(ImageFilter.GaussianBlur(3))
    return im,mask
G=[spokelse(F[i],P[i]) for i in gi]
def ramme(i,antall,strek=False):
    im=Image.fromarray(F[i]).convert('RGBA')
    for k in range(antall):
        g,m=G[k]; a=m.point(lambda v:int(v*0.7)); im.paste(g,(0,0),a)
    if strek and antall>1:
        d=ImageDraw.Draw(im); pts=[(P[j][0],P[j][1]) for j in range(n) if 30.03<=A+j/FPS<=31.5]
        for a_,b_ in zip(pts[::2],pts[1::2]): d.line([a_,b_],fill=(110,240,74,255),width=8)
    return im.convert('RGB')
ut=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-c:v','libx264','-crf','16','-preset','veryfast','-pix_fmt','yuv420p','spol.mp4'],stdin=subprocess.PIPE)
def skriv(im): ut.stdin.write(np.asarray(im).tobytes())
antall=lambda i: sum(1 for g in gi if g<=i)
L=[]
for i in range(n):              # sakte fram, spøkelser bygges opp
    for _ in range(2): skriv(ramme(i,antall(i))); L.append('a')
for i in range(n-1,-1,-3): skriv(ramme(i,len(G))); L.append('b')   # spol tilbake 3x
for _ in range(6): skriv(ramme(0,len(G),True)); L.append('c')
for i in range(n): skriv(ramme(i,len(G),True)); L.append('c')     # fram igjen med hele banen
for _ in range(15): skriv(ramme(n-1,len(G),True)); L.append('c')
ut.stdin.close(); ut.wait()
print('lengde',len(L)/30, 'a',L.count('a')/30,'b',L.count('b')/30,'c',L.count('c')/30)
