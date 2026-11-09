set -e
V=/home/claude/videoer/arbeid-og-energi/energibevaring
VT=/home/claude/videoer/_verktoy
python3 $VT/komponer.py --anim $V/energibevaring.mp4 --opptak opptak.mkv --plan plan.json --ut bilde.mp4
ffmpeg -v error -y -i bilde.mp4 -i A_lyd.wav -map 0:v -map 1:a -c:v copy -c:a pcm_s16le -shortest A.mkv
K=10.4
ffmpeg -v error -y -t $K -i A.mkv -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 seg1.mkv
ffmpeg -v error -y -ss $K -i A.mkv -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 seg3.mkv
ffmpeg -v error -y -i intro.mp4 -f lavfi -t 2.2 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -c:v copy -c:a pcm_s16le seg2.mkv
ffmpeg -v error -y -i outro.mp4 -f lavfi -t 2.8 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -c:v copy -c:a pcm_s16le seg4.mkv
d3=$(ffprobe -v error -show_entries format=duration -of csv=p=0 seg3.mkv)
o1=$(python3 -c "print($K-0.4)"); o2=$(python3 -c "print($K-0.4+2.2-0.3)"); o3=$(python3 -c "print($K-0.4+2.2-0.3+$d3-0.5)")
ms1=$(python3 -c "print(int(($K-0.6)*1000))"); ms2=$(python3 -c "print(int(($K-0.4)*1000))"); ms3=$(python3 -c "print(int($o3*1000))")
ffmpeg -v error -y -i seg1.mkv -i seg2.mkv -i seg3.mkv -i seg4.mkv -i $VT/lyd/svisj.wav -i $VT/lyd/intro_musikk.wav -i $VT/lyd/outro_musikk.wav -filter_complex "\
[0:v][1:v]xfade=transition=slideleft:duration=0.4:offset=$o1[v1];[v1][2:v]xfade=transition=fade:duration=0.3:offset=$o2[v2];[v2][3:v]xfade=transition=fadeblack:duration=0.5:offset=$o3[v];\
[0:a][1:a]acrossfade=d=0.4[a1];[a1][2:a]acrossfade=d=0.3[a2];[a2][3:a]acrossfade=d=0.5[a3];\
[4:a]aresample=48000,volume=0.35,adelay=$ms1|$ms1,apad[s];[5:a]aresample=48000,adelay=$ms2|$ms2,apad[m];[6:a]aresample=48000,adelay=$ms3|$ms3,apad[o];[a3][s][m][o]amix=inputs=4:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart energibevaring_utkast1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 energibevaring_utkast1.mp4
