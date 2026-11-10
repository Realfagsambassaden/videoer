import subprocess, numpy as np, cv2
SRC='/home/claude/kilder/sn_5743.mov'; A,B=29.95,31.6; FPS=30
X0,Y0,CW,CH=294,262,432,768
# hele bildet (ikke utsnitt) for sporing
raw=subprocess.run(['ffmpeg','-v','error','-ss',str(A),'-t',str(B-A),'-i',SRC,'-vf',f'fps={FPS}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
FF=np.frombuffer(raw,np.uint8).reshape(-1,1920,1080,3); n=len(FF); print(n)
mask=np.zeros((1920,1080),np.uint8); mask[100:560,:]=255           # bakgrunn: åser, hus
orb=cv2.ORB_create(3000)
g0=cv2.cvtColor(FF[0],cv2.COLOR_RGB2GRAY); k0,d0=orb.detectAndCompute(g0,mask)
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True); M=[]
for i in range(n):
    g=cv2.cvtColor(FF[i],cv2.COLOR_RGB2GRAY); k,d=orb.detectAndCompute(g,mask)
    mt=sorted(bf.match(d,d0),key=lambda m:m.distance)[:400]
    src=np.float32([k[m.queryIdx].pt for m in mt]); dst=np.float32([k0[m.trainIdx].pt for m in mt])
    T,inl=cv2.estimateAffinePartial2D(src,dst,method=cv2.RANSAC,ransacReprojThreshold=3)
    M.append(T)
    if i%10==0: print(i, T.round(3).tolist(), int(inl.sum()))
np.save('M.npy',np.array(M)); np.save('FF.npy',FF)
