# Utkast 4: opptak3.mkv = opptak2.mkv (lag_opptak2.sh) med
#  - «Da vil» (T 74.12–74.64) byttet ut med én bit fra stammingen (fil 309.24, 17 bilder = 0.68 s, biter/dav_s309.24_17.mkv)
#  - «Tilsvarende så vet jeg at på toppen av bevegelsen» (T 164.36–167.28) kuttet
E="-c:v libx264 -crf 16 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1"
ffmpeg -v error -y -i opptak2.mkv -frames:v 1853 -t 74.12 $E o3a.mkv
ffmpeg -v error -y -i dav.mkv -frames:v 17 -t 0.68 $E o3b.mkv
ffmpeg -v error -y -ss 74.64 -i opptak2.mkv -frames:v 2243 -t 89.72 $E o3c.mkv
ffmpeg -v error -y -ss 167.28 -i opptak2.mkv -frames:v 5741 -t 229.64 $E o3d.mkv
printf "file o3a.mkv\nfile o3b.mkv\nfile o3c.mkv\nfile o3d.mkv\n" > l3.txt && ffmpeg -v error -y -f concat -safe 0 -i l3.txt -c copy opptak3.mkv
python3 dubb.py opptak3.mkv tale.wav
