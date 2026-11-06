#!/bin/bash
# kutter bitene (25 fps, lik lengde lyd/bilde)
cd "$(dirname "$0")"; mkdir -p biter2
K="../MEG.mov"
[ -s biter2/c00.mkv ] || ffmpeg -v error -y -ss 0.080 -i "$K" -frames:v 311 -t 12.440 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c00.mkv
[ -s biter2/c01.mkv ] || ffmpeg -v error -y -ss 14.440 -i "$K" -frames:v 52 -t 2.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c01.mkv
[ -s biter2/c02.mkv ] || ffmpeg -v error -y -ss 19.200 -i "$K" -frames:v 116 -t 4.640 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c02.mkv
[ -s biter2/c03.mkv ] || ffmpeg -v error -y -ss 27.680 -i "$K" -frames:v 220 -t 8.800 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c03.mkv
[ -s biter2/c04.mkv ] || ffmpeg -v error -y -ss 48.240 -i "$K" -frames:v 209 -t 8.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c04.mkv
[ -s biter2/c05.mkv ] || ffmpeg -v error -y -ss 63.440 -i "$K" -frames:v 62 -t 2.480 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c05.mkv
[ -s biter2/c06.mkv ] || ffmpeg -v error -y -ss 66.720 -i "$K" -frames:v 83 -t 3.320 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c06.mkv
[ -s biter2/c07.mkv ] || ffmpeg -v error -y -ss 70.440 -i "$K" -frames:v 193 -t 7.720 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c07.mkv
[ -s biter2/c08.mkv ] || ffmpeg -v error -y -ss 78.200 -i "$K" -frames:v 68 -t 2.720 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c08.mkv
[ -s biter2/c09.mkv ] || ffmpeg -v error -y -ss 102.400 -i "$K" -frames:v 115 -t 4.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c09.mkv
[ -s biter2/c10.mkv ] || ffmpeg -v error -y -ss 107.760 -i "$K" -frames:v 49 -t 1.960 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c10.mkv
[ -s biter2/c11.mkv ] || ffmpeg -v error -y -ss 160.400 -i "$K" -frames:v 330 -t 13.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c11.mkv
[ -s biter2/c12.mkv ] || ffmpeg -v error -y -ss 174.520 -i "$K" -frames:v 250 -t 10.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c12.mkv
[ -s biter2/c13.mkv ] || ffmpeg -v error -y -ss 192.080 -i "$K" -frames:v 209 -t 8.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c13.mkv
[ -s biter2/c14.mkv ] || ffmpeg -v error -y -ss 213.320 -i "$K" -frames:v 164 -t 6.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c14.mkv
[ -s biter2/c15.mkv ] || ffmpeg -v error -y -ss 258.240 -i "$K" -frames:v 200 -t 8.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c15.mkv
[ -s biter2/c16.mkv ] || ffmpeg -v error -y -ss 276.120 -i "$K" -frames:v 52 -t 2.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c16.mkv
[ -s biter2/c17.mkv ] || ffmpeg -v error -y -ss 280.560 -i "$K" -frames:v 138 -t 5.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c17.mkv
[ -s biter2/c18.mkv ] || ffmpeg -v error -y -ss 289.840 -i "$K" -frames:v 96 -t 3.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c18.mkv
[ -s biter2/c19.mkv ] || ffmpeg -v error -y -ss 306.360 -i "$K" -frames:v 136 -t 5.440 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c19.mkv
[ -s biter2/c20.mkv ] || ffmpeg -v error -y -ss 312.320 -i "$K" -frames:v 244 -t 9.760 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c20.mkv
[ -s biter2/c21.mkv ] || ffmpeg -v error -y -ss 329.760 -i "$K" -frames:v 296 -t 11.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c21.mkv
[ -s biter2/c22.mkv ] || ffmpeg -v error -y -ss 342.200 -i "$K" -frames:v 36 -t 1.440 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c22.mkv
[ -s biter2/c23.mkv ] || ffmpeg -v error -y -ss 591.160 -i "$K" -frames:v 50 -t 2.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c23.mkv
[ -s biter2/c24.mkv ] || ffmpeg -v error -y -ss 344.720 -i "$K" -frames:v 35 -t 1.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c24.mkv
[ -s biter2/c25.mkv ] || ffmpeg -v error -y -ss 376.720 -i "$K" -frames:v 225 -t 9.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c25.mkv
[ -s biter2/c26.mkv ] || ffmpeg -v error -y -ss 388.040 -i "$K" -frames:v 5 -t 0.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c26.mkv
[ -s biter2/c27.mkv ] || ffmpeg -v error -y -ss 388.640 -i "$K" -frames:v 327 -t 13.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c27.mkv
[ -s biter2/c28.mkv ] || ffmpeg -v error -y -ss 421.880 -i "$K" -frames:v 260 -t 10.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c28.mkv
[ -s biter2/c29.mkv ] || ffmpeg -v error -y -ss 432.760 -i "$K" -frames:v 164 -t 6.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c29.mkv
[ -s biter2/c30.mkv ] || ffmpeg -v error -y -ss 442.880 -i "$K" -frames:v 144 -t 5.760 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c30.mkv
[ -s biter2/c31.mkv ] || ffmpeg -v error -y -ss 449.080 -i "$K" -frames:v 56 -t 2.240 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c31.mkv
[ -s biter2/c32.mkv ] || ffmpeg -v error -y -ss 451.960 -i "$K" -frames:v 100 -t 4.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c32.mkv
[ -s biter2/c33.mkv ] || ffmpeg -v error -y -ss 513.360 -i "$K" -frames:v 243 -t 9.720 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c33.mkv
[ -s biter2/c34.mkv ] || ffmpeg -v error -y -ss 523.680 -i "$K" -frames:v 95 -t 3.800 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c34.mkv
[ -s biter2/c35.mkv ] || ffmpeg -v error -y -ss 540.600 -i "$K" -frames:v 59 -t 2.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c35.mkv
[ -s biter2/c36.mkv ] || ffmpeg -v error -y -ss 552.200 -i "$K" -frames:v 72 -t 2.880 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c36.mkv
[ -s biter2/c37.mkv ] || ffmpeg -v error -y -ss 615.920 -i "$K" -frames:v 135 -t 5.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c37.mkv
[ -s biter2/c38.mkv ] || ffmpeg -v error -y -ss 621.840 -i "$K" -frames:v 162 -t 6.480 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c38.mkv
[ -s biter2/c39.mkv ] || ffmpeg -v error -y -ss 556.400 -i "$K" -frames:v 27 -t 1.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter2/c39.mkv
