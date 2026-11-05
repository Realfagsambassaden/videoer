# Bruk: python3 outro_gronn.py <Intro.mp4> <ut.mp4>
# Outro: dempet tavlebakgrunn + den grønne DrNormann-logoen som spretter fram, så toning til svart.
import numpy as np, subprocess, sys, os
from scipy import ndimage as nd
from PIL import Image, ImageEnhance
W,H,fps,L = 1920,1080,30,2.8
subprocess.run(['ffmpeg','-v','error','-y','-ss','0.2','-i',sys.argv[1],'-frames:v','1','-vf','negate','/tmp/_bg.png'],check=True)
a=np.asarray(Image.open('/tmp/_bg.png').convert('RGB')).astype(np.float32).copy()
x0,x1,y0,y1=680,1100,370,810; reg=a[y0:y1,x0:x1]; st=nd.binary_dilation(reg.min(2)>110,iterations=5)
reg[st]=np.median(reg[~st].reshape(-1,3),0); a[y0:y1,x0:x1]=reg      # fjern den hvite teksten fra introen
bg = ImageEnhance.Brightness(Image.fromarray(a.astype(np.uint8))).enhance(0.35)
logo = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'drnormann-logo.png')).convert('RGBA')
enc = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-c:v','libx264','-crf','16','-preset','veryfast','-pix_fmt','yuv420p',sys.argv[2]],stdin=subprocess.PIPE)
def back(x):  # ease-out-back
    c=1.9; x=min(max(x,0),1); return 1+(c+1)*(x-1)**3+c*(x-1)**2
for i in range(int(L*fps)):
    t=i/fps; f=bg.copy()
    k=back((t-0.1)/0.45); s=0.62*(0.5+0.5*k) if t>0.1 else 0
    if s>0:
        h=int(H*s); w=int(logo.width*h/logo.height); lg=logo.resize((w,h),Image.LANCZOS)
        a=np.asarray(lg).copy(); a[...,3]=(a[...,3]*min(1,(t-0.1)/0.2)).astype(np.uint8); lg=Image.fromarray(a)
        f.paste(lg,((W-w)//2,(H-h)//2),lg)
    ut=1-min(max((t-(L-0.6))/0.6,0),1)
    arr=(np.asarray(f).astype(np.float32)*ut).astype(np.uint8)
    enc.stdin.write(arr.tobytes())
enc.stdin.close(); enc.wait(); print('ok')
