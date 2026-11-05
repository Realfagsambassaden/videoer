set -e
V=/home/claude/videoer/arbeid-og-energi/potensiell-energi
python3 /home/claude/videoer/_verktoy/komponer.py --anim $V/potensiell-energi.mp4 --opptak opptak.mkv --plan plan.json --ut bilde.mp4
L=$(ffprobe -v error -show_entries format=duration -of csv=p=0 bilde.mp4); echo bilde $L
# A = bilde + lyd
ffmpeg -v error -y -i bilde.mp4 -i A_lyd.wav -map 0:v -map 1:a -c:v copy -c:a pcm_s16le -shortest A.mkv
ffmpeg -v error -y -t 14.5 -i A.mkv -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 seg1.mkv
ffmpeg -v error -y -ss 14.5 -i A.mkv -c:v libx264 -crf 17 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 seg3.mkv
# intro med lyd (første 2.2 s av introlyden, tones ut) + svisj
ffmpeg -v error -y -i intro.mp4 -f lavfi -t 2.2 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -c:v copy -c:a pcm_s16le seg2.mkv
ffmpeg -v error -y -i outro.mp4 -f lavfi -t 2.8 -i anullsrc=r=48000:cl=stereo -map 0:v -map 1:a -c:v copy -c:a pcm_s16le seg4.mkv
d1=14.5; d2=2.2; d3=$(ffprobe -v error -show_entries format=duration -of csv=p=0 seg3.mkv)
o1=$(python3 -c "print(14.5-0.4)"); o2=$(python3 -c "print(14.5-0.4+2.2-0.3)"); o3=$(python3 -c "print(14.5-0.4+2.2-0.3+$d3-0.5)")
ffmpeg -v error -y -i seg1.mkv -i seg2.mkv -i seg3.mkv -i seg4.mkv -i /home/claude/videoer/_verktoy/lyd/svisj.wav -i /home/claude/videoer/_verktoy/lyd/intro_musikk.wav -filter_complex "\
[0:v][1:v]xfade=transition=slideleft:duration=0.4:offset=$o1[v1];[v1][2:v]xfade=transition=fade:duration=0.3:offset=$o2[v2];[v2][3:v]xfade=transition=fadeblack:duration=0.5:offset=$o3[v];\
[0:a][1:a]acrossfade=d=0.4[a1];[a1][2:a]acrossfade=d=0.3[a2];[a2][3:a]acrossfade=d=0.5[a3];\
[4:a]aresample=48000,volume=0.35,adelay=13900|13900,apad[s];[5:a]aresample=48000,adelay=14100|14100,apad[m];[a3][s][m]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart potensiell-energi_utkast2.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 potensiell-energi_utkast2.mp4
