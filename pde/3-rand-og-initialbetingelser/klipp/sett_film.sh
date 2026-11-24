# PDE film 3: kald start (0–KS) → (stille toning) Ben-intro på tavla med ring, uten stjerner (egen lyd) → resten → Ben skrives (outro, uten lyd) (miniatyrbildet er bare på YouTube, ikke i filmen). Kjøres i arbeidsmappa (komp.mp4, opptak_lyd_fx.wav).
set -e
V=/home/claude/videoer/pde/3-rand-og-initialbetingelser; VT=/home/claude/videoer/_verktoy
KS=$(python3 -c "import json;print([q for q in json.load(open('kart.json')) if q[4]=='K'][-1][1])"); FART=1.07  # speedes opp med samme tonehøyde (atempo)
UT=${UT:-rand-og-initialbetingelser_utkast3.mp4}
KS0=$(python3 -c "print($KS-0.25)")  # kald start kuttes 0.25 s før: lyden i opptaket ligger 0.08 s etter, og starten på neste setning skal ikke med
ffmpeg -v error -y -t $KS0 -i komp.mp4 -t $KS0 -i opptak_lyd_fx.wav -map 0:v -map 1:a -vf setpts=PTS/$FART -af atempo=$FART -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 s0.mkv
# hoveddelen starter litt etter KS (inntil 0.45 s, bare stillhet hoppes over), så tavla har tonet over til hoveddelen
K3=$(python3 -c "
import soundfile as sf,numpy as np;x,sr=sf.read('opptak_lyd_fx.wav');x=x.mean(1) if x.ndim>1 else x
t=$KS
while t<$KS+0.45 and 20*np.log10(np.sqrt(np.mean(x[int(t*sr):int((t+.04)*sr)]**2))+1e-9)<-45: t+=0.04
print(round(max($KS,t-0.08),2))")
ffmpeg -v error -y -ss $K3 -i komp.mp4 -ss $K3 -i opptak_lyd_fx.wav -map 0:v -map 1:a -vf setpts=PTS/$FART -af atempo=$FART -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 s3b.mkv
# fryst bilde (0.6 s, stille) tatt etter at tavla har tonet over til hoveddelen – ikke slutten av kaldstarten
ffmpeg -v error -y -ss $K3 -i komp.mp4 -frames:v 1 s2.png && ffmpeg -v error -y -loop 1 -framerate 30 -i s2.png -f lavfi -i anullsrc=r=48000:cl=stereo -t 0.6 -map 0:v -map 1:a -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -c:a pcm_s16le -ar 48000 -ac 2 s2.mkv
ffmpeg -v error -y -i s2.mkv -i s3b.mkv -filter_complex '[0:v]format=yuv420p[a];[1:v]format=yuv420p[b];[a][0:a][b][1:a]concat=n=2:v=1:a=1[v][o]' -map '[v]' -map '[o]' -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 s3.mkv  # 0.6 s stille før hoveddelen: overgangen fra introen skal ikke ta med starten av neste setning
cp $VT/ben/intro-ben-tavle.mkv s1.mkv; cp $VT/ben/outro-ben-tavle.mkv s4.mkv
d() { ffprobe -v error -show_entries format=duration -of csv=p=0 $1; }
d0=$(d s0.mkv); d1=$(d s1.mkv); d3=$(d s3.mkv)
o0=$(python3 -c "print($d0-0.4)"); o2=$(python3 -c "print($d0-0.4+$d1-0.4)"); o3=$(python3 -c "print($d0-0.4+$d1-0.4+$d3-0.5)")
mi=$(python3 -c "print(int(($o0-0.3)*1000))")
ffmpeg -v error -y -i s0.mkv -i s1.mkv -i s3.mkv -i s4.mkv -filter_complex "\
[0:v][1:v]xfade=transition=fade:duration=0.4:offset=$o0[v1];[v1][2:v]xfade=transition=slideleft:duration=0.4:offset=$o2[v3];[v3][3:v]xfade=transition=fadeblack:duration=0.5:offset=$o3[v];\
[0:a][1:a]acrossfade=d=0.4[a1];[a1][2:a]acrossfade=d=0.4:c1=nofade[a3];[a3][3:a]acrossfade=d=0.5[a4];\
[a4]loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart $UT
d $UT
