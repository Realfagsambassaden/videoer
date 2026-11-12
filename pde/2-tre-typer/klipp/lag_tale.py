# Setter sammen tale.wav (48 kHz) fra utvalget i rng.py.
# Pauser inne i bitene over MAXP s strammes inn til MAXP; romtone mellom bitene.
# kart.json: [[ut_start, ut_slutt, kilde_start, kilde_slutt, seksjon], ...] (lineær innenfor hver delbit)
import json, numpy as np, soundfile as sf
import sys; exec(open(sys.argv[1] if len(sys.argv)>1 else 'rng.py').read())
UT=sys.argv[2] if len(sys.argv)>2 else 'tale'
MAXP=0.32
x,sr=sf.read('/mnt/user-data/uploads/DrNormann/INGENIØRMATTE/_arbeidsfiler/pde1_take2.flac',dtype='float32')
if x.ndim>1: x=x.mean(1)
rom=x[int(652.5*sr):int(671.5*sr)]
def romtone(d):
    n=int(round(d*sr)); r=np.resize(rom,n).copy(); f=min(n//2,int(0.02*sr))
    if f: r[:f]*=np.linspace(0,1,f); r[-f:]*=np.linspace(1,0,f)
    return r
def fade(y):
    f=min(len(y)//2,int(0.012*sr)); y=y.copy(); y[:f]*=np.linspace(0,1,f); y[-f:]*=np.linspace(1,0,f); return y
def delbiter(a,b):
    seg=x[int(a*sr):int(b*sr)]; n=int(0.02*sr)
    e=np.array([10*np.log10(np.mean(seg[i:i+n]**2)+1e-12) for i in range(0,len(seg)-n,n)])
    on=e>-50; ut=[]; start=0; i=0
    while i<len(on):
        if not on[i]:
            j=i
            while j<len(on) and not on[j]: j+=1
            if (j-i)*0.02>MAXP and i>0 and j<len(on):
                h=MAXP/2
                ut.append((a+start*0.02, a+i*0.02+h)); start=None
                start=(j*0.02-h)/0.02
            i=j
        else: i+=1
    ut.append((a+start*0.02,b))
    return ut
ut=[];kart=[];t=0.0
for k,(a,b,s) in enumerate(R):
    if k>0:
        d=0.9 if s!=R[k-1][2] else 0.25
        ut.append(romtone(d)); t+=d
    for c,d2 in delbiter(a,b):
        y=fade(x[int(c*sr):int(d2*sr)])
        kart.append([round(t,3),round(t+len(y)/sr,3),round(c,3),round(d2,3),s]); ut.append(y); t+=len(y)/sr
ut.append(romtone(0.5))
y=np.concatenate(ut)
sf.write(UT+'_raa.wav',y,sr,subtype='PCM_24')
json.dump(kart,open(UT+'_kart.json','w'))
print('lengde',len(y)/sr, 'delbiter',len(kart))
for s in sorted(set(q[4] for q in kart)):
    v=[q for q in kart if q[4]==s]; print(s, v[0][0], v[-1][1])
