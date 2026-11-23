# PDE film 2: kald start (0–KS) → Ben-intro på tavla (med egen lyd) → tittelkort → resten → Ben-outro. Kjøres i arbeidsmappa (komp.mp4, opptak_lyd_fx.wav).
set -e
V=/home/claude/videoer/pde/2-tre-typer; VT=/home/claude/videoer/_verktoy
KS=6.88; FART=1.07  # speedes opp med samme tonehøyde (atempo)
UT=${UT:-tre-typer_utkast3.mp4}
ffmpeg -v error -y -i komp.mp4 -i opptak_lyd_fx.wav -t $KS -map 0:v -map 1:a -vf setpts=PTS/$FART -af atempo=$FART -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 s0.mkv
ffmpeg -v error -y -ss $KS -i komp.mp4 -ss $KS -i opptak_lyd_fx.wav -map 0:v -map 1:a -vf setpts=PTS/$FART -af atempo=$FART -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 s3.mkv
cp $VT/ben/intro-ben-tavle.mkv s1.mkv; cp $VT/ben/outro-ben-tavle.mkv s4.mkv
ffmpeg -v error -y -loop 1 -t 2.4 -i $V/thumbnail.jpg -f lavfi -t 2.4 -i anullsrc=r=48000:cl=stereo -vf scale=1920:1080,format=yuv420p -r 30 -map 0:v -map 1:a -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le s2.mkv
d() { ffprobe -v error -show_entries format=duration -of csv=p=0 $1; }
d0=$(d s0.mkv); d1=$(d s1.mkv); d3=$(d s3.mkv)
o0=$(python3 -c "print($d0-0.4)"); o1=$(python3 -c "print($d0-0.4+$d1-0.3)"); o2=$(python3 -c "print($d0-0.4+$d1-0.3+2.4-0.4)"); o3=$(python3 -c "print($d0-0.4+$d1-0.3+2.4-0.4+$d3-0.5)")
mi=$(python3 -c "print(int(($o0-0.3)*1000))")
ffmpeg -v error -y -i s0.mkv -i s1.mkv -i s2.mkv -i s3.mkv -i s4.mkv -i $VT/lyd/overgang-svosj.wav -filter_complex "\
[0:v][1:v]xfade=transition=slideleft:duration=0.4:offset=$o0[v1];[v1][2:v]xfade=transition=fade:duration=0.3:offset=$o1[v2];[v2][3:v]xfade=transition=slideleft:duration=0.4:offset=$o2[v3];[v3][4:v]xfade=transition=fadeblack:duration=0.5:offset=$o3[v];\
[0:a][1:a]acrossfade=d=0.4[a1];[a1][2:a]acrossfade=d=0.3:c1=nofade[a2];[a2][3:a]acrossfade=d=0.4[a3];[a3][4:a]acrossfade=d=0.5:c2=nofade[a4];\
[5:a]aresample=48000,volume=0.6,adelay=$mi|$mi,apad[s];[a4][s]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart $UT
d $UT
