# Lydeffekter i opptak_lyd.wav → opptak_lyd_fx.wav: svisj ved hvert nytt steg (når tavla glir), pop når stempler dukker opp.
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
sv,po=last('svisj.wav'),last('pop.wav')
SVISJ=[173.08,428.3,515.68,574.9,667.24,724.1,862.52,947.9,1117.4,1137.2,1345.9,1495.7]
POP=[468.2,483.0,768.3,893.6,1036.5,1316.0]
for t,y,v in [(t,sv,0.30) for t in SVISJ]+[(t,po,0.25) for t in POP]:
    i=int(M(t)*sr); n=min(len(y),len(x)-i); x[i:i+n]+=y[:n]*v
sf.write('opptak_lyd_fx.wav',x,sr,subtype='PCM_24'); print('ok')
