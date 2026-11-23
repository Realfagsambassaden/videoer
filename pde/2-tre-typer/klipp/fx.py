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
sv,po,kn,sm,sl=last('overgang-svosj.wav'),last('pop.wav'),last('knirk.wav'),last('smokk.wav'),last('overgang-svosj-med-slag.wav')
SVISJ=[173.08,428.3,515.68,574.9,667.24,724.1,862.52,947.9,1117.4,1137.2,1345.9,1495.7]
POP=[467.4,483.0,768.3,893.6,1036.5,1316.0]
KNIRK=[587.1]
SMOKK=[1352.6,1353.5,1354.4,1385.4]
SLAG=[574.9,724.1,1137.2,1345.9,1495.7]  # store skifter: svosj med slag (slaget ved 0.6 s)
for t,y,v in [(t,sv,0.45) for t in SVISJ if t not in SLAG]+[(t-0.6,sl,0.45) for t in SLAG]+[(t,po,0.25) for t in POP]+[(t,kn,0.35) for t in KNIRK]+[(t,sm,0.5) for t in SMOKK]:
    i=max(0,int((M(t+0.6)-0.6 if y is sl else M(t))*sr)); n=min(len(y),len(x)-i); x[i:i+n]+=y[:n]*v
sf.write('opptak_lyd_fx.wav',x,sr,subtype='PCM_24'); print('ok')
