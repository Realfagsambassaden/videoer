# Lydeffekter i opptak_lyd.wav → opptak_lyd_fx.wav: svisj ved hvert nytt steg (når tavla glir), pop når stempler dukker opp, ba-dum-tss etter vitsen («dritlett»).
# Kjøres i arbeidsmappa: python3 fx.py <kart.json>
import json, sys, numpy as np, soundfile as sf
from scipy.signal import resample_poly
VT='/home/claude/videoer/_verktoy/lyd/'
k=json.load(open(sys.argv[1]))
def M(T):
    for a,b,c,d,s in k:
        if c<=T<=d: return a+T-c
    return min(a for a,b,c,d,s in k if c>T)
x,sr=sf.read('opptak_lyd.wav',dtype='float32')
def last(f):
    y,r=sf.read(VT+f,dtype='float32')
    if y.ndim>1: y=y.mean(1)
    if r!=sr: y=resample_poly(y,sr,r).astype('float32')
    return y
sv,po,bd,sm,pl,sp,sl=last('overgang-svosj.wav'),last('pop.wav'),last('badumtss.wav'),last('smokk.wav'),last('pling.wav'),last('slapp.wav'),last('overgang-svosj-med-slag.wav')
SVISJ=[220.4,232.6,262.1,294.4,306.05,408.1,571.0,785.9,836.7,924.0,972.3,1012.7,1033.0,1048.5,1091.7,1133.8,1217.8,1242.85]
POP=[429.7,454.8,1016.0,1243.0,305.6,309.4]
SMOKK=[71.4,72.6,73.9]
PLING=[74.6]
SLAPP=[1040.55]
SLAG=[262.1,1033.0,1217.8]
BADUM=[1058.1]
for t,y,v in [(t,sv,0.45) for t in SVISJ if t not in SLAG]+[(t,sl,0.45) for t in SLAG]+[(t,sm,0.5) for t in SMOKK]+[(t,pl,0.45) for t in PLING]+[(t,sp,0.6) for t in SLAPP]+[(t,po,0.25) for t in POP]+[(t,bd,0.35) for t in BADUM]:
    i=max(0,int((M(t)-0.6 if y is sl else M(t))*sr)); n=min(len(y),len(x)-i); x[i:i+n]+=y[:n]*v
sf.write('opptak_lyd_fx.wav',x,sr,subtype='PCM_24'); print('ok')
