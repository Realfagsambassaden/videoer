# Lager Ben-intro og -outro på tavla: lærerens gamle tavle (første bilde av Intro.mp4, i negativ, uten «Dr. Normann»)
# med Ben-animasjonene (Merkevare/animasjon/transparent/*.webm) og lyden (Merkevare/lyd/enkel/wav/) over.
# Bruk: bash _verktoy/ben/lag_intro_outro.sh <Merkevare-mappe> <Intro.mp4>
set -e; M=$1; I=$2; V=$(cd $(dirname $0); pwd); T=$(mktemp -d)
python3 $V/tavle_intro.py $I $T/bg.mp4 0.04 1.0 && ffmpeg -v error -y -i $T/bg.mp4 -frames:v 1 $T/tavle.png
python3 -c "from PIL import Image,ImageEnhance as E;im=Image.open('$T/tavle.png');E.Brightness(im).enhance(0.6).save('$V/tavle-intro-60.png');E.Brightness(im).enhance(0.35).save('$V/tavle-intro-35.png')"
ffmpeg -v error -y -loop 1 -i $V/tavle-intro-60.png -c:v libvpx-vp9 -i $M/animasjon/transparent/ben-ring-stjerner-intro-16x9-transparent.webm -i $M/lyd/enkel/wav/intro-ring-stjerner.wav -filter_complex "[0]scale=2400:-1,zoompan=z='1.0+0.06*on/152':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30[b];[b][1]overlay=shortest=1,format=yuv420p[v]" -map "[v]" -map 2:a -r 30 -c:v libx264 -crf 16 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 -shortest $V/intro-ben-tavle.mkv
ffmpeg -v error -y -loop 1 -i $V/tavle-intro-35.png -c:v libvpx-vp9 -i $M/animasjon/transparent/ben-ring-stjerner-outro-16x9-transparent.webm -i $M/lyd/enkel/wav/outro-stjerner.wav -filter_complex "[0][1]overlay=shortest=1,format=yuv420p[v]" -map "[v]" -map 2:a -r 30 -c:v libx264 -crf 16 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 -shortest $V/outro-ben-tavle.mkv
rm -rf $T
