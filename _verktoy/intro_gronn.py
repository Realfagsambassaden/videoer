# Bruk: python3 intro_gronn.py <Intro.mp4> <ut.mp4> [lengde=2.2]
# DrNormann-introen i negativ, der «Dr. Normann» farges neongrønn med glød (som logoen i hjørnet).
import subprocess, numpy as np, sys
from scipy import ndimage as nd
src, ut, lengde = sys.argv[1], sys.argv[2], float(sys.argv[3] if len(sys.argv) > 3 else 2.2)
W, H = 1920, 1080
inn = subprocess.Popen(['ffmpeg','-v','error','-t',str(lengde),'-i',src,'-vf','negate,fps=30','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','30','-i','-','-c:v','libx264','-crf','16','-preset','veryfast','-pix_fmt','yuv420p',ut],stdin=subprocess.PIPE)
x0,x1,y0,y1 = 680,1100,370,810
GR = np.array([110,240,74],np.float32); KJ = np.array([215,255,190],np.float32)
while True:
    b = inn.stdout.read(W*H*3)
    if len(b) < W*H*3: break
    f = np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.float32).copy()
    reg = f[y0:y1,x0:x1]
    lys = reg.min(2)
    m = np.clip((lys-110)/80,0,1)                      # tekstmaske (myk)
    m = nd.grey_closing(m, size=(3,3))
    stor = nd.binary_dilation(m>0.05, iterations=4)
    bak = np.median(reg[~stor].reshape(-1,3),0) if (~stor).any() else np.array([12,14,13.])
    reg[stor] = bak                                     # fjern den hvite teksten
    glod = nd.gaussian_filter(m, 14)*1.8 + nd.gaussian_filter(m, 5)*1.2
    glod = np.clip(glod,0,1)[...,None]
    reg[:] = reg*(1-glod*0.85) + GR*glod*0.85
    mm = m[...,None]; reg[:] = reg*(1-mm) + (GR*0.55+KJ*0.45)*mm
    f[y0:y1,x0:x1] = reg
    enc.stdin.write(np.clip(f,0,255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait(); print('ferdig', ut)
