# Lager Ben-intro og -outro (23. november 2026, lærerens ønsker):
#  intro: den gamle tavla (første bilde av Intro.mp4, i negativ, uten «Dr. Normann», langsom zoom) + «Ben» med ring og stjerner
#         (ben-ring-intro), 68 % størrelse, lyden intro-ring.wav.
#  outro: «Ben» skrives for hånd (ben-intro uten ring), 68 %, på svart, uten lyd.
# Bruk: bash _verktoy/ben/lag_intro_outro.sh <Intro.mp4>   (webm-filene og lyden ligger i denne mappa, kopiert fra Merkevare/)
set -e; I=$1; V=$(cd $(dirname $0); pwd); T=$(mktemp -d)
python3 $V/tavle_intro.py $I $T/bg.mp4 0.04 1.0 && ffmpeg -v error -y -i $T/bg.mp4 -frames:v 1 $T/tavle.png
python3 -c "from PIL import Image,ImageEnhance as E;im=Image.open('$T/tavle.png');E.Brightness(im).enhance(0.6).save('$V/tavle-intro-60.png')"
ffmpeg -v error -y -loop 1 -i $V/tavle-intro-60.png -c:v libvpx-vp9 -i $V/ben-ring-intro-16x9-transparent.webm -i $V/intro-ring.wav -filter_complex "[0]scale=2400:-1,zoompan=z='1.0+0.06*on/152':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30[b];[1]scale=iw*0.68:-1[l];[b][l]overlay=(W-w)/2:(H-h)/2:shortest=1,format=yuv420p[v]" -map "[v]" -map 2:a -r 30 -c:v libx264 -crf 16 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 -shortest $V/intro-ben-tavle.mkv
ffmpeg -v error -y -f lavfi -i color=c=0x050505:s=1920x1080:r=30 -c:v libvpx-vp9 -i $V/ben-intro-16x9-transparent.webm -f lavfi -i anullsrc=r=48000:cl=stereo -filter_complex "[1]scale=iw*0.68:-1[l];[0][l]overlay=(W-w)/2:(H-h)/2:shortest=1,format=yuv420p[v]" -map "[v]" -map 2:a -r 30 -c:v libx264 -crf 16 -preset veryfast -c:a pcm_s16le -shortest $V/outro-ben-tavle.mkv
rm -rf $T
