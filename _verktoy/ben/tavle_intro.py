# Tavla fra lærerens Intro.mp4 (i negativ, uten «Dr. Normann»-teksten) som bakgrunn for Ben-introen/-outroen.
# Bruk: python3 tavle_intro.py <Intro.mp4> <ut.mp4> <lengde> [lysstyrke=0.7] [still=0]
import subprocess, numpy as np, sys
from scipy import ndimage as nd
src, ut, L = sys.argv[1], sys.argv[2], float(sys.argv[3]); lys=float(sys.argv[4]) if len(sys.argv)>4 else 0.7; still=len(sys.argv)>5 and sys.argv[5]=='1'
W,H=1920,1080
vf='negate,fps=30'+(',trim=end_frame=1,loop=999:1' if still else '')
inn=subprocess.Popen(['ffmpeg','-v','error','-t',str(L) if not still else '1','-i',src,'-vf',vf,'-t',str(L),'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','30','-i','-','-c:v','libx264','-crf','16','-preset','veryfast','-pix_fmt','yuv420p',ut],stdin=subprocess.PIPE)
x0,x1,y0,y1=680,1100,370,810;n=0
while n<int(L*30):
    b=inn.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    f=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.float32).copy()
    reg=f[y0:y1,x0:x1];m=reg.min(2)>110;st=nd.binary_dilation(m,iterations=5)
    if (~st).any(): reg[st]=np.median(reg[~st].reshape(-1,3),0)
    f[y0:y1,x0:x1]=reg
    enc.stdin.write(np.clip(f*lys,0,255).astype(np.uint8).tobytes());n+=1
enc.stdin.close();enc.wait();print('ferdig',ut,n)
