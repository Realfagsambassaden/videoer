set -e
K="../MEG.mov"
mkdir -p biter3
cp biter2/c00.mkv biter3/c00.mkv
cp biter2/c01.mkv biter3/c01.mkv
cp biter2/c02.mkv biter3/c02.mkv
cp biter2/c03.mkv biter3/c03.mkv
cp biter2/c04.mkv biter3/c04.mkv
cp biter2/c05.mkv biter3/c05.mkv
cp biter2/c06.mkv biter3/c06.mkv
cp biter2/c07.mkv biter3/c07.mkv
cp biter2/c08.mkv biter3/c08.mkv
cp biter2/c09.mkv biter3/c09.mkv
cp biter2/c10.mkv biter3/c10.mkv
cp biter2/c11.mkv biter3/c11.mkv
cp biter2/c12.mkv biter3/c12.mkv
cp biter2/c13.mkv biter3/c13.mkv
cp biter2/c14.mkv biter3/c14.mkv
cp biter2/c15.mkv biter3/c15.mkv
cp biter2/c16.mkv biter3/c16.mkv
cp biter2/c17.mkv biter3/c17.mkv
cp biter2/c18.mkv biter3/c18.mkv
cp biter2/c19.mkv biter3/c19.mkv
cp biter2/c20.mkv biter3/c20.mkv
cp biter2/c21.mkv biter3/c21.mkv
cp biter2/c22.mkv biter3/c22.mkv
cp biter2/c23.mkv biter3/c23.mkv
cp biter2/c24.mkv biter3/c24.mkv
ffmpeg -v error -y -ss 376.720 -i "$K" -frames:v 188 -t 7.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter3/c25.mkv
cp biter2/c26.mkv biter3/c26.mkv
ffmpeg -v error -y -ss 388.640 -i "$K" -frames:v 64 -t 2.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter3/c27.mkv
ffmpeg -v error -y -ss 391.040 -i "$K" -ss 384.640 -i "$K" -map 0:v -map 1:a -frames:v 20 -t 0.800 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter3/c28.mkv
ffmpeg -v error -y -ss 391.840 -i "$K" -frames:v 247 -t 9.880 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter3/c29.mkv
cp biter2/c28.mkv biter3/c30.mkv
cp biter2/c29.mkv biter3/c31.mkv
cp biter2/c30.mkv biter3/c32.mkv
cp biter2/c31.mkv biter3/c33.mkv
cp biter2/c32.mkv biter3/c34.mkv
cp biter2/c33.mkv biter3/c35.mkv
cp biter2/c34.mkv biter3/c36.mkv
cp biter2/c35.mkv biter3/c37.mkv
cp biter2/c36.mkv biter3/c38.mkv
cp biter2/c37.mkv biter3/c39.mkv
cp biter2/c38.mkv biter3/c40.mkv
cp biter2/c39.mkv biter3/c41.mkv
ls biter3 | wc -l
