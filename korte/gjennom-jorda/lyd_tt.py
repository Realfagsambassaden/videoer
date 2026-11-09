import json, numpy as np, soundfile as sf, subprocess
D = json.load(open('overlay.json')); sr = 48000; L = D['lengde']
subprocess.run(['ffmpeg','-v','error','-y','-i','grunn.mkv','-vn','-ac','1','-ar','48000','tale.wav'],check=True)
tale,_ = sf.read('tale.wav',dtype='float32')
ut = np.zeros(int(L*sr)+sr, np.float32); ut[:len(tale)] += tale
LY = '/home/claude/videoer/_verktoy/lyd/'
def les(n): x,r = sf.read(LY+n,dtype='float32'); return x.mean(1) if x.ndim>1 else x
def legg(x,t,v=1): i=int(t*sr); n=min(len(x),len(ut)-i); ut[i:i+n]+=x[:n]*v
def trombone():   # «wah wah wah waaah»
    out=[]
    for f,d in [(311,.38),(293,.38),(277,.38),(262,1.3)]:
        t=np.arange(int(d*sr))/sr; vib = 1+ (0.03*np.sin(2*np.pi*6*t) if d>1 else 0)
        ph=2*np.pi*np.cumsum(f*vib*(1-0.02*t))/sr; x=sum(np.sin(k*ph)/k for k in range(1,8))
        e=np.minimum(1,t/0.04)*np.minimum(1,(d-t)/0.12); out.append(np.convolve(x*e,np.ones(6)/6,'same'))
    return 0.18*np.concatenate(out)
svisj, pop, boing = les('svisj.wav'), les('pop.wav'), les('boing.wav')
for k in D['kutt'][1:]: legg(svisj, k-0.15, .3)
for t0,v,tx,stil in D['stempler']:
    if 'FAIL' in tx: legg(trombone(), t0, 1.0)
    elif 'SPLÆSJ' in tx: legg(boing, t0, .4)
    else: legg(pop, t0, .3)
legg(svisj, D['slutt']-0.1, .4)
m = les('outro_musikk.wav'); legg(m[:int(2.9*sr)], D['slutt'], 1.6)
sf.write('tt_lyd.wav', np.clip(ut[:int(L*sr)],-1,1), sr)
