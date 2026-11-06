set -e
K="../Meg.mov"
mkdir -p biter
ffmpeg -v error -y -ss 25.920 -i "$K" -frames:v 178 -t 7.120 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c00.mkv
ffmpeg -v error -y -ss 33.960 -i "$K" -frames:v 85 -t 3.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c01.mkv
ffmpeg -v error -y -ss 39.680 -i "$K" -frames:v 60 -t 2.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c02.mkv
ffmpeg -v error -y -ss 42.600 -i "$K" -frames:v 87 -t 3.480 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c03.mkv
ffmpeg -v error -y -ss 51.920 -i "$K" -frames:v 234 -t 9.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c04.mkv
ffmpeg -v error -y -ss 68.400 -i "$K" -frames:v 50 -t 2.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c05.mkv
ffmpeg -v error -y -ss 71.520 -i "$K" -frames:v 415 -t 16.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c06.mkv
ffmpeg -v error -y -ss 106.160 -i "$K" -frames:v 160 -t 6.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c07.mkv
ffmpeg -v error -y -ss 113.720 -i "$K" -frames:v 130 -t 5.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c08.mkv
ffmpeg -v error -y -ss 188.040 -i "$K" -frames:v 721 -t 28.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c09.mkv
ffmpeg -v error -y -ss 218.480 -i "$K" -frames:v 129 -t 5.160 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c10.mkv
ffmpeg -v error -y -ss 232.520 -i "$K" -frames:v 166 -t 6.640 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c11.mkv
ffmpeg -v error -y -ss 252.800 -i "$K" -frames:v 232 -t 9.280 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c12.mkv
ffmpeg -v error -y -ss 271.240 -i "$K" -frames:v 155 -t 6.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c13.mkv
ffmpeg -v error -y -ss 278.360 -i "$K" -frames:v 215 -t 8.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c14.mkv
ffmpeg -v error -y -ss 290.600 -i "$K" -frames:v 71 -t 2.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c15.mkv
ffmpeg -v error -y -ss 294.120 -i "$K" -frames:v 183 -t 7.320 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c16.mkv
ffmpeg -v error -y -ss 302.760 -i "$K" -frames:v 75 -t 3.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c17.mkv
ffmpeg -v error -y -ss 326.680 -i "$K" -frames:v 188 -t 7.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c18.mkv
ffmpeg -v error -y -ss 360.400 -i "$K" -frames:v 131 -t 5.240 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c19.mkv
ffmpeg -v error -y -ss 366.280 -i "$K" -frames:v 41 -t 1.640 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c20.mkv
ffmpeg -v error -y -ss 369.600 -i "$K" -frames:v 260 -t 10.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c21.mkv
ffmpeg -v error -y -ss 392.040 -i "$K" -frames:v 327 -t 13.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c22.mkv
ffmpeg -v error -y -ss 441.320 -i "$K" -frames:v 154 -t 6.160 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c23.mkv
ffmpeg -v error -y -ss 448.120 -i "$K" -frames:v 64 -t 2.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c24.mkv
ffmpeg -v error -y -ss 454.800 -i "$K" -frames:v 101 -t 4.040 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c25.mkv
ffmpeg -v error -y -ss 459.680 -i "$K" -frames:v 253 -t 10.120 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c26.mkv
ffmpeg -v error -y -ss 470.600 -i "$K" -frames:v 162 -t 6.480 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c27.mkv
ffmpeg -v error -y -ss 512.280 -i "$K" -frames:v 236 -t 9.440 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c28.mkv
ffmpeg -v error -y -ss 526.800 -i "$K" -frames:v 145 -t 5.800 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c29.mkv
ffmpeg -v error -y -ss 538.880 -i "$K" -frames:v 91 -t 3.640 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c30.mkv
ffmpeg -v error -y -ss 544.680 -i "$K" -frames:v 35 -t 1.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c31.mkv
ls biter/*.mkv | sed "s/^/file /" > liste.txt
ffmpeg -v error -y -f concat -safe 0 -i liste.txt -c copy opptak.mkv
ffprobe -v error -show_entries format=duration -of csv=p=0 opptak.mkv
