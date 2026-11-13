# Setter sammen bitene til opptak.mkv (bilde + lyd nøyaktig like lange) og lager kart.json (ut-tid → kildetid).
import json, subprocess, numpy as np, soundfile as sf
U='/mnt/user-data/uploads/DrNormann/INGENIØRMATTE/_arbeidsfiler/pde1/'
B=json.load(open('biter.json')); fil=json.load(open('filer.json'))
lyd=[]; kart=[]; t=0
with open('concat.txt','w') as c:
    for (a,b,s,m,n),f in zip(B,fil):
        nf=int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',U+f]).decode().strip().strip(','))
        subprocess.run(['ffmpeg','-v','error','-y','-i',U+f,'-vn','-ac','1','-ar','48000','-f','wav','tmp.wav'],check=True)
        x,_=sf.read('tmp.wav',dtype='float32'); x=np.pad(x,(0,max(0,n*1920-len(x))))[:n*1920]
        k=240; x[:k]*=np.linspace(0,1,k); x[-k:]*=np.linspace(1,0,k)
        assert nf==n,(f,nf,n)
        lyd.append(x); kart.append([round(t,3),round(t+n/25,3),a,b,s]); t+=n/25
        c.write(f"file '{U+f}'\n")
sf.write('opptak_lyd.wav',np.concatenate(lyd),48000,subtype='PCM_24')
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','concat.txt','-an','-c:v','copy','opptak_v.mkv'],check=True)
json.dump(kart,open('kart.json','w'))
print('lengde',t)
