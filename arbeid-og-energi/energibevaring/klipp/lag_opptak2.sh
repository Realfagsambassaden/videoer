# Utkast 3: opptak2.mkv = opptak.mkv (klippet etter edl.json) uten biten der læreren presser sammen fjæra
# (T 119.68–132.56), og tale.wav med «vil» dubbet inn (dubb.py).
ffmpeg -v error -y -i opptak.mkv -frames:v 2992 -t 119.68 -c:v libx264 -crf 16 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 o2a.mkv
ffmpeg -v error -y -ss 132.56 -i opptak.mkv -frames:v 6931 -t 277.24 -c:v libx264 -crf 16 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 o2b.mkv
printf "file o2a.mkv\nfile o2b.mkv\n" > l2.txt && ffmpeg -v error -y -f concat -safe 0 -i l2.txt -c copy opptak2.mkv
python3 dubb.py opptak2.mkv tale.wav
