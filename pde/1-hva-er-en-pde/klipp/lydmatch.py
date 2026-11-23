# Gjør ekstratake-lyden (181.56–192.08) lik nabobitene: EQ-matching, nivå og romtone.
import numpy as np, soundfile as sf
from scipy.signal import welch, firwin2, fftconvolve
x,sr=sf.read('fix/opptak_lyd_fx_orig.wav',dtype='float64')
A,B=181.56,192.08; ia,ib=int(A*sr),int(B*sr)
def spek(y):
    f=1024;fr=y[:len(y)//f*f].reshape(-1,f);e=np.sqrt((fr**2).mean(1))
    sp=fr[e>np.percentile(e,40)].ravel(); F,P=welch(sp,sr,nperseg=4096); return F,P,np.sqrt((sp**2).mean())
F,Pr,_=spek(np.concatenate([x[int(160*sr):int(181.5*sr)],x[int(192.1*sr):int(209*sr)]]))
_,Pe,_=spek(x[ia:ib])
# 1/3-oktav glatting av forholdet
g=np.zeros_like(F)
for i,f in enumerate(F):
    m=(F>=f/2**(1/6))&(F<=f*2**(1/6)) if f>0 else F<20
    g[i]=10*np.log10(Pr[m].mean()/Pe[m].mean())
g=np.clip(g,-6,10); g[F<50]=0; g[F>16000]=np.minimum(g[F>16000],6)
h=firwin2(2047,F/(sr/2),10**(g/20))
y=fftconvolve(x[ia-4096:ib+4096],h,mode='same')[4096:-4096]
# nivå: lik talenivå
_,_,rr=spek(np.concatenate([x[int(160*sr):int(181.5*sr)],x[int(192.1*sr):int(209*sr)]]))
_,_,re=spek(y); y*=rr/re
# romtone fra en pause i nabobiten, på nivå med differansen
f=1024
def stoy(y):
    fr=y[:len(y)//f*f].reshape(-1,f);e=np.sqrt((fr**2).mean(1));return np.percentile(e,10)
ref=x[int(160*sr):int(181.5*sr)]
fr=ref[:len(ref)//f*f].reshape(-1,f);e=np.sqrt((fr**2).mean(1));rom=fr[e<np.percentile(e,12)].ravel()
nr,ne=stoy(ref),stoy(y)
if nr>ne:
    k=np.sqrt(max(nr**2-ne**2,0))/np.sqrt((rom**2).mean())
    rt=np.tile(rom,len(y)//len(rom)+1)[:len(y)]*k; y=y+rt
# myke overganger 30 ms
n=int(0.03*sr); w=np.linspace(0,1,n)
out=x.copy(); seg=x[ia:ib].copy(); seg[:]=y
seg[:n]=x[ia:ia+n]*(1-w)+y[:n]*w; seg[-n:]=y[-n:]*(1-w)+x[ib-n:ib]*w
out[ia:ib]=seg
sf.write('opptak_lyd_fx.wav',out,sr,subtype='PCM_24')
print('gain dB (100,200,1k,3k,8k,12k):',[round(float(np.interp(q,F,g)),1) for q in [100,200,1000,3000,8000,12000]],'nivå',round(20*np.log10(rr/re),1),'støy',20*np.log10(nr),20*np.log10(ne))
