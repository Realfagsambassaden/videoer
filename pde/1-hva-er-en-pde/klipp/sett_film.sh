# PDE film 1: kald start (0–KS) → intro → tittelkort → resten → outro
set -e
V=/home/claude/videoer/pde/1-hva-er-en-pde; VT=/home/claude/videoer/_verktoy
KS=26.08; L=272.36
ffmpeg -v error -y -i komp.mp4 -i opptak_lyd.wav -t $KS -map 0:v -map 1:a -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 s0.mkv
ffmpeg -v error -y -ss $KS -i komp.mp4 -ss $KS -i opptak_lyd.wav -map 0:v -map 1:a -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 s3.mkv
ffmpeg -v error -y -i ut/intro.mp4 -f lavfi -t 2.2 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le s1.mkv
ffmpeg -v error -y -loop 1 -t 1.9 -i $V/thumbnail.jpg -f lavfi -t 1.9 -i anullsrc=r=48000:cl=stereo -vf scale=1920:1080,format=yuv420p -r 30 -map 0:v -map 1:a -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le s2.mkv
ffmpeg -v error -y -i ut/outro.mp4 -f lavfi -t 2.8 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le s4.mkv
d0=$(ffprobe -v error -show_entries format=duration -of csv=p=0 s0.mkv); d1=$(ffprobe -v error -show_entries format=duration -of csv=p=0 s1.mkv); d3=$(ffprobe -v error -show_entries format=duration -of csv=p=0 s3.mkv)
o0=$(python3 -c "print($d0-0.4)"); o1=$(python3 -c "print($d0-0.4+$d1-0.3)"); o2=$(python3 -c "print($d0-0.4+$d1-0.3+1.9-0.4)"); o3=$(python3 -c "print($d0-0.4+$d1-0.3+1.9-0.4+$d3-0.5)")
mi=$(python3 -c "print(int($o0*1000))"); mo=$(python3 -c "print(int($o3*1000))")
ffmpeg -v error -y -i s0.mkv -i s1.mkv -i s2.mkv -i s3.mkv -i s4.mkv -i $VT/lyd/svisj.wav -i $VT/lyd/intro_musikk.wav -i $VT/lyd/outro_musikk.wav -filter_complex "\
[0:v][1:v]xfade=transition=slideleft:duration=0.4:offset=$o0[v1];[v1][2:v]xfade=transition=fade:duration=0.3:offset=$o1[v2];[v2][3:v]xfade=transition=slideleft:duration=0.4:offset=$o2[v3];[v3][4:v]xfade=transition=fadeblack:duration=0.5:offset=$o3[v];\
[0:a][1:a]acrossfade=d=0.4[a1];[a1][2:a]acrossfade=d=0.3[a2];[a2][3:a]acrossfade=d=0.4[a3];[a3][4:a]acrossfade=d=0.5[a4];\
[5:a]aresample=48000,volume=0.35,adelay=$mi|$mi,apad[s];[6:a]aresample=48000,adelay=$mi|$mi,apad[m];[7:a]aresample=48000,adelay=$mo|$mo,apad[o];[a4][s][m][o]amix=inputs=4:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart hva-er-en-pde_utkast1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 hva-er-en-pde_utkast1.mp4
