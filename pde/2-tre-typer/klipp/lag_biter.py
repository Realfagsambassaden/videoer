# Lager biter (25 fps-rutenett) fra edl.py og klipper dem fra 5-min-bitene av opptaket (k00..k04).
# Bruk: python3 lag_biter.py <lyd16k.wav> <mappe med kNN.mkv> <ut-mappe>
import json, sys, os, subprocess, soundfile as sf, numpy as np
exec(open(os.path.join(os.path.dirname(__file__),'edl.py')).read())
lydfil,kmappe,ut=sys.argv[1:4]; NK=len([f for f in os.listdir(kmappe) if f.startswith('k')]); os.makedirs(ut,exist_ok=True)
l,sr=sf.read(lydfil,dtype='float32'); h=320
db=np.array([20*np.log10(np.sqrt((l[i:i+h]**2).mean())+1e-9) for i in range(0,len(l)-h,h)])
F=lambda t: round(t*25)/25
biter=[]
for a,b,s,m in B:
    if s=='X': biter.append([F(a),F(b),s,m]); continue
    i0,i1=int(a*50),int(b*50); on=db[i0:i1]>-45; idx=np.where(on)[0]
    ts=a+idx[0]*0.02; on55=np.where(db[i0:i1]>-55)[0]; te=a+on55[-1]*0.02  # slutt: følg utklingingen ned til -55 dB
    start=max(a,ts-0.2)
    if m.startswith('§'):  # kunstpause: gå bakover i stillheten, opptil 1.0 s før talen
        j=int(ts*50); k=0
        while k<50 and db[j-k-1]<-45: k+=1
        start=min(start,ts-max(0.2,k*0.02-0.05))
    slutt=b if s=='K' else min(b,te+0.3)  # kald start: la pausen stå, overgangen spiser 0.4 s
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
# del biter som krysser en 300 s-grense
B2=[]
for a,b,s,m in biter:
    k=min(int(a//300),NK-1)
    if k<NK-1 and b>300*(k+1)+1e-6: B2+= [[a,300.0*(k+1),s,m],[300.0*(k+1),b,s,m]]
    else: B2.append([a,b,s,m])
filer=[]
for i,q in enumerate(B2):
    a,b=q[0],q[1]; n=round((b-a)*25); q.append(n); k=min(int(a//300+1e-9),NK-1); f=f'{ut}/b_{i:02d}.mkv'; filer.append(f)
    if not os.path.exists(f):
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{a-300*k:.3f}','-i',f'{kmappe}/k{k:02d}.mkv','-frames:v',str(n),'-af',f'atrim=end_sample={n*1920}','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-c:a','pcm_s16le',f],check=True)
json.dump(B2,open('biter.json','w'),indent=0); json.dump(filer,open('filer.json','w'))
print(len(B2),'biter',sum(q[4] for q in B2)/25,'s')
