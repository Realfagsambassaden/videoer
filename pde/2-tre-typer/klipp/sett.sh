# Setter sammen film 2: intro → tittelkort → tavle med Dashman → outro.
# Kjør i en arbeidsmappe med intro.mp4 og outro.mp4 (fra intro_gronn.py/outro_gronn.py) og film2_tale.wav.
set -e
V=/home/claude/videoer/pde/2-tre-typer; VT=/home/claude/videoer/_verktoy
python3 $VT/dashman_hjorne.py $V/2-tre-typer.mp4 film2_tale.wav $V/poser.json dashman.mp4
(cd $V && python3 klipp/lyd.py $OLDPWD/film2_tale.wav $OLDPWD/hoved_lyd.wav)
ffmpeg -v error -y -i dashman.mp4 -i hoved_lyd.wav -map 0:v -map 1:a -c:v libx264 -crf 17 -preset veryfast -r 30 -c:a pcm_s16le -ar 48000 -ac 2 -shortest seg3.mkv
ffmpeg -v error -y -i intro.mp4 -f lavfi -t 2.2 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le seg1.mkv
ffmpeg -v error -y -loop 1 -t 1.9 -i $V/thumbnail.jpg -f lavfi -t 1.9 -i anullsrc=r=48000:cl=stereo -vf scale=1920:1080,format=yuv420p -r 30 -map 0:v -map 1:a -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le seg2.mkv
ffmpeg -v error -y -i outro.mp4 -f lavfi -t 2.8 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -r 30 -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le seg4.mkv
d1=$(ffprobe -v error -show_entries format=duration -of csv=p=0 seg1.mkv); d3=$(ffprobe -v error -show_entries format=duration -of csv=p=0 seg3.mkv)
o1=$(python3 -c "print($d1-0.3)"); o2=$(python3 -c "print($d1-0.3+1.9-0.4)"); o3=$(python3 -c "print($d1-0.3+1.9-0.4+$d3-0.5)")
ms3=$(python3 -c "print(int($o3*1000))")
ffmpeg -v error -y -i seg1.mkv -i seg2.mkv -i seg3.mkv -i seg4.mkv -i $VT/lyd/svisj.wav -i $VT/lyd/intro_musikk.wav -i $VT/lyd/outro_musikk.wav -filter_complex "\
[0:v][1:v]xfade=transition=fade:duration=0.3:offset=$o1[v1];[v1][2:v]xfade=transition=slideleft:duration=0.4:offset=$o2[v2];[v2][3:v]xfade=transition=fadeblack:duration=0.5:offset=$o3[v];\
[0:a][1:a]acrossfade=d=0.3[a1];[a1][2:a]acrossfade=d=0.4[a2];[a2][3:a]acrossfade=d=0.5[a3];\
[4:a]aresample=48000,volume=0.35,apad[s];[5:a]aresample=48000,apad[m];[6:a]aresample=48000,adelay=$ms3|$ms3,apad[o];[a3][s][m][o]amix=inputs=4:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart tre-typer-pde_utkast1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 tre-typer-pde_utkast1.mp4
