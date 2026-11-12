import sys, soundfile as sf, numpy as np
l,sr=sf.read('lyd16k.wav',dtype='float32')
for arg in sys.argv[1:]:
    a,b=map(float,arg.split('-'))
    x=l[int(a*sr):int(b*sr)]; n=int(0.02*sr)
    e=np.array([10*np.log10(np.mean(x[i:i+n]**2)+1e-12) for i in range(0,len(x)-n,n)])
    on=e>-50; segs=[];s=None
    for i,v in enumerate(on):
        if v and s is None: s=i
        if not v and s is not None:
            segs.append((s,i));s=None
    if s is not None: segs.append((s,len(on)))
    # merge gaps < 0.12 s
    m=[]
    for s,t in segs:
        if m and s-m[-1][1]<6: m[-1]=(m[-1][0],t)
        else: m.append((s,t))
    print(arg,' '.join(f'[{a+s*0.02:.2f}-{a+t*0.02:.2f}]' for s,t in m))
