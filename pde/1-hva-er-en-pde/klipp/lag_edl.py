# Lager delbiter (frame-rutenett 25 fps) fra edl.py: tale-start −0.2 s, slutt +0.3 s, pauser > 0.85 s strammes til 0.5 s.
import json, soundfile as sf, numpy as np
exec(open('edl.py').read())
l,sr=sf.read('lyd16k.wav',dtype='float32'); h=320
db=np.array([20*np.log10(np.sqrt((l[i:i+h]**2).mean())+1e-9) for i in range(0,len(l)-h,h)])
F=lambda t: round(t*25)/25
biter=[]
for a,b,s,m in B:
    i0,i1=int(a*50),int(b*50); on=db[i0:i1]>-45; idx=np.where(on)[0]
    ts=a+idx[0]*0.02; te=a+idx[-1]*0.02
    start=max(a,ts-0.2) if s!='K' else a; slutt=min(b,te+0.3)
    # del ved lange pauser
    run=0; kutt=[]
    for k,v in enumerate(on):
        if not v: run+=1
        else:
            if run*0.02>0.85 and k-run>idx[0]: kutt.append((a+(k-run)*0.02, a+k*0.02))
            run=0
    cur=start
    for p0,p1 in kutt:
        if p0<=cur: continue
        biter.append([F(cur),F(p0+0.25),s,m]); cur=p1-0.25
    biter.append([F(cur),F(slutt),s,m])
tot=0
for q in biter: q.append(round((q[1]-q[0])*25)); tot+=q[4]
json.dump(biter,open('biter.json','w'),indent=0)
print(len(biter),'biter',tot/25,'s')
