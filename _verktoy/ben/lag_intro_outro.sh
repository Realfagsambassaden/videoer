# Lager Ben-intro og -outro på tavla fra lærerens merkevarefiler (Merkevare/animasjon/transparent/*.webm og Merkevare/lyd/enkel/wav/).
# Bruk: bash _verktoy/ben/lag_intro_outro.sh <Merkevare-mappe>
set -e; M=$1; V=$(dirname $0)
ffmpeg -v error -y -loop 1 -i $V/tavle-1920.png -c:v libvpx-vp9 -i $M/animasjon/transparent/ben-ring-stjerner-intro-16x9-transparent.webm -i $M/lyd/enkel/wav/intro-ring-stjerner.wav -filter_complex "[0][1]overlay=shortest=1,format=yuv420p[v]" -map "[v]" -map 2:a -r 30 -c:v libx264 -crf 16 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 -shortest $V/intro-ben-tavle.mkv
ffmpeg -v error -y -loop 1 -i $V/tavle-1920.png -c:v libvpx-vp9 -i $M/animasjon/transparent/ben-ring-stjerner-outro-16x9-transparent.webm -i $M/lyd/enkel/wav/outro-stjerner.wav -filter_complex "[0][1]overlay=shortest=1,format=yuv420p[v]" -map "[v]" -map 2:a -r 30 -c:v libx264 -crf 16 -preset veryfast -c:a pcm_s16le -ar 48000 -ac 2 -shortest $V/outro-ben-tavle.mkv
