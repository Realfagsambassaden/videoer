# Tikkelyd fra klokka: legges inn i opptak_lyd.wav → opptak_lyd_fx.wav
import json, numpy as np, soundfile as sf
k=json.load(open('kart.json'))
def M(T):
    for a,b,c,d,s in k:
        if T<c: return a
        if T<=d: return a+T-c
x,sr=sf.read('opptak_lyd.wav',dtype='float32')
n=int(0.012*sr); t=np.arange(n)/sr
klikk=(np.random.RandomState(1).randn(n)*np.exp(-t*600)+0.6*np.sin(2*np.pi*3200*t)*np.exp(-t*400))*0.08
for t0,dur in [(139.3,3.0),(265.3,4.0)]:
    s0=M(t0)
    for j in range(int(dur*2)):
        i=int((s0+j*0.5)*sr); x[i:i+n]+=klikk*(1.0 if j%2==0 else 0.7)
sf.write('opptak_lyd_fx.wav',x,sr,subtype='PCM_24')
print('ok')
