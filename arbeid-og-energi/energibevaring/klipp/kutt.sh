set -e
K="../Meg_Energibevaring.mov"
mkdir -p biter
[ -s biter/s24.96_259.mkv ] || ffmpeg -v error -y -ss 24.960 -i "$K" -frames:v 259 -t 10.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s24.96_259.mkv
[ -s biter/s141.72_138.mkv ] || ffmpeg -v error -y -ss 141.720 -i "$K" -frames:v 138 -t 5.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s141.72_138.mkv
[ -s biter/s147.88_172.mkv ] || ffmpeg -v error -y -ss 147.880 -i "$K" -frames:v 172 -t 6.880 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s147.88_172.mkv
[ -s biter/s177.84_138.mkv ] || ffmpeg -v error -y -ss 177.840 -i "$K" -frames:v 138 -t 5.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s177.84_138.mkv
[ -s biter/s189.64_90.mkv ] || ffmpeg -v error -y -ss 189.640 -i "$K" -frames:v 90 -t 3.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s189.64_90.mkv
[ -s biter/s193.44_161.mkv ] || ffmpeg -v error -y -ss 193.440 -i "$K" -frames:v 161 -t 6.440 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s193.44_161.mkv
[ -s biter/s212.64_321.mkv ] || ffmpeg -v error -y -ss 212.640 -i "$K" -frames:v 321 -t 12.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s212.64_321.mkv
[ -s biter/s225.64_119.mkv ] || ffmpeg -v error -y -ss 225.640 -i "$K" -frames:v 119 -t 4.760 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s225.64_119.mkv
[ -s biter/s230.72_114.mkv ] || ffmpeg -v error -y -ss 230.720 -i "$K" -frames:v 114 -t 4.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s230.72_114.mkv
[ -s biter/s235.52_102.mkv ] || ffmpeg -v error -y -ss 235.520 -i "$K" -frames:v 102 -t 4.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s235.52_102.mkv
[ -s biter/s240.48_107.mkv ] || ffmpeg -v error -y -ss 240.480 -i "$K" -frames:v 107 -t 4.280 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s240.48_107.mkv
[ -s biter/s245.00_35.mkv ] || ffmpeg -v error -y -ss 245.000 -i "$K" -frames:v 35 -t 1.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s245.00_35.mkv
[ -s biter/s247.84_50.mkv ] || ffmpeg -v error -y -ss 247.840 -i "$K" -frames:v 50 -t 2.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s247.84_50.mkv
[ -s biter/s306.96_47.mkv ] || ffmpeg -v error -y -ss 306.960 -i "$K" -frames:v 47 -t 1.880 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s306.96_47.mkv
[ -s biter/s309.24_6.mkv ] || ffmpeg -v error -y -ss 309.240 -i "$K" -frames:v 6 -t 0.240 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s309.24_6.mkv
[ -s biter/s310.16_7.mkv ] || ffmpeg -v error -y -ss 310.160 -i "$K" -frames:v 7 -t 0.280 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s310.16_7.mkv
[ -s biter/s310.72_121.mkv ] || ffmpeg -v error -y -ss 310.720 -i "$K" -frames:v 121 -t 4.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s310.72_121.mkv
[ -s biter/s315.80_158.mkv ] || ffmpeg -v error -y -ss 315.800 -i "$K" -frames:v 158 -t 6.320 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s315.80_158.mkv
[ -s biter/s322.32_80.mkv ] || ffmpeg -v error -y -ss 322.320 -i "$K" -frames:v 80 -t 3.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s322.32_80.mkv
[ -s biter/s332.40_225.mkv ] || ffmpeg -v error -y -ss 332.400 -i "$K" -frames:v 225 -t 9.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s332.40_225.mkv
[ -s biter/s341.56_160.mkv ] || ffmpeg -v error -y -ss 341.560 -i "$K" -frames:v 160 -t 6.400 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s341.56_160.mkv
[ -s biter/s359.56_36.mkv ] || ffmpeg -v error -y -ss 359.560 -i "$K" -frames:v 36 -t 1.440 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s359.56_36.mkv
[ -s biter/s361.12_58.mkv ] || ffmpeg -v error -y -ss 361.120 -i "$K" -frames:v 58 -t 2.320 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s361.12_58.mkv
[ -s biter/s370.12_215.mkv ] || ffmpeg -v error -y -ss 370.120 -i "$K" -frames:v 215 -t 8.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s370.12_215.mkv
[ -s biter/s394.68_395.mkv ] || ffmpeg -v error -y -ss 394.680 -i "$K" -frames:v 395 -t 15.800 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s394.68_395.mkv
[ -s biter/s415.12_77.mkv ] || ffmpeg -v error -y -ss 415.120 -i "$K" -frames:v 77 -t 3.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s415.12_77.mkv
[ -s biter/s418.44_229.mkv ] || ffmpeg -v error -y -ss 418.440 -i "$K" -frames:v 229 -t 9.160 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s418.44_229.mkv
[ -s biter/s427.76_120.mkv ] || ffmpeg -v error -y -ss 427.760 -i "$K" -frames:v 120 -t 4.800 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s427.76_120.mkv
[ -s biter/s433.12_58.mkv ] || ffmpeg -v error -y -ss 433.120 -i "$K" -frames:v 58 -t 2.320 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s433.12_58.mkv
[ -s biter/s435.60_32.mkv ] || ffmpeg -v error -y -ss 435.600 -i "$K" -frames:v 32 -t 1.280 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s435.60_32.mkv
[ -s biter/s437.64_13.mkv ] || ffmpeg -v error -y -ss 437.640 -i "$K" -frames:v 13 -t 0.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s437.64_13.mkv
[ -s biter/s438.68_16.mkv ] || ffmpeg -v error -y -ss 438.680 -i "$K" -frames:v 16 -t 0.640 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s438.68_16.mkv
[ -s biter/s439.68_62.mkv ] || ffmpeg -v error -y -ss 439.680 -i "$K" -frames:v 62 -t 2.480 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s439.68_62.mkv
[ -s biter/s443.08_182.mkv ] || ffmpeg -v error -y -ss 443.080 -i "$K" -frames:v 182 -t 7.280 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s443.08_182.mkv
[ -s biter/s450.76_81.mkv ] || ffmpeg -v error -y -ss 450.760 -i "$K" -frames:v 81 -t 3.240 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s450.76_81.mkv
[ -s biter/s454.40_84.mkv ] || ffmpeg -v error -y -ss 454.400 -i "$K" -frames:v 84 -t 3.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s454.40_84.mkv
[ -s biter/s459.12_125.mkv ] || ffmpeg -v error -y -ss 459.120 -i "$K" -frames:v 125 -t 5.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s459.12_125.mkv
[ -s biter/s464.28_38.mkv ] || ffmpeg -v error -y -ss 464.280 -i "$K" -frames:v 38 -t 1.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s464.28_38.mkv
[ -s biter/s597.52_73.mkv ] || ffmpeg -v error -y -ss 597.520 -i "$K" -frames:v 73 -t 2.920 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s597.52_73.mkv
[ -s biter/s600.60_96.mkv ] || ffmpeg -v error -y -ss 600.600 -i "$K" -frames:v 96 -t 3.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s600.60_96.mkv
[ -s biter/s605.28_70.mkv ] || ffmpeg -v error -y -ss 605.280 -i "$K" -frames:v 70 -t 2.800 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s605.28_70.mkv
[ -s biter/s609.24_75.mkv ] || ffmpeg -v error -y -ss 609.240 -i "$K" -frames:v 75 -t 3.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s609.24_75.mkv
[ -s biter/s612.40_40.mkv ] || ffmpeg -v error -y -ss 612.400 -i "$K" -frames:v 40 -t 1.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s612.40_40.mkv
[ -s biter/s627.84_38.mkv ] || ffmpeg -v error -y -ss 627.840 -i "$K" -frames:v 38 -t 1.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s627.84_38.mkv
[ -s biter/s629.56_105.mkv ] || ffmpeg -v error -y -ss 629.560 -i "$K" -frames:v 105 -t 4.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s629.56_105.mkv
[ -s biter/s635.76_26.mkv ] || ffmpeg -v error -y -ss 635.760 -i "$K" -frames:v 26 -t 1.040 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s635.76_26.mkv
[ -s biter/s638.84_90.mkv ] || ffmpeg -v error -y -ss 638.840 -i "$K" -frames:v 90 -t 3.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s638.84_90.mkv
[ -s biter/s654.52_200.mkv ] || ffmpeg -v error -y -ss 654.520 -i "$K" -frames:v 200 -t 8.000 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s654.52_200.mkv
[ -s biter/s662.64_56.mkv ] || ffmpeg -v error -y -ss 662.640 -i "$K" -frames:v 56 -t 2.240 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s662.64_56.mkv
[ -s biter/s665.04_226.mkv ] || ffmpeg -v error -y -ss 665.040 -i "$K" -frames:v 226 -t 9.040 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s665.04_226.mkv
[ -s biter/s674.72_76.mkv ] || ffmpeg -v error -y -ss 674.720 -i "$K" -frames:v 76 -t 3.040 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s674.72_76.mkv
[ -s biter/s688.28_14.mkv ] || ffmpeg -v error -y -ss 688.280 -i "$K" -frames:v 14 -t 0.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s688.28_14.mkv
[ -s biter/s689.56_188.mkv ] || ffmpeg -v error -y -ss 689.560 -i "$K" -frames:v 188 -t 7.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s689.56_188.mkv
[ -s biter/s697.48_59.mkv ] || ffmpeg -v error -y -ss 697.480 -i "$K" -frames:v 59 -t 2.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s697.48_59.mkv
[ -s biter/s713.36_130.mkv ] || ffmpeg -v error -y -ss 713.360 -i "$K" -frames:v 130 -t 5.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s713.36_130.mkv
[ -s biter/s774.16_253.mkv ] || ffmpeg -v error -y -ss 774.160 -i "$K" -frames:v 253 -t 10.120 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s774.16_253.mkv
[ -s biter/s787.12_101.mkv ] || ffmpeg -v error -y -ss 787.120 -i "$K" -frames:v 101 -t 4.040 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s787.12_101.mkv
[ -s biter/s791.36_81.mkv ] || ffmpeg -v error -y -ss 791.360 -i "$K" -frames:v 81 -t 3.240 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s791.36_81.mkv
[ -s biter/s795.16_78.mkv ] || ffmpeg -v error -y -ss 795.160 -i "$K" -frames:v 78 -t 3.120 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s795.16_78.mkv
[ -s biter/s798.88_96.mkv ] || ffmpeg -v error -y -ss 798.880 -i "$K" -frames:v 96 -t 3.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s798.88_96.mkv
[ -s biter/s804.16_179.mkv ] || ffmpeg -v error -y -ss 804.160 -i "$K" -frames:v 179 -t 7.160 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s804.16_179.mkv
[ -s biter/s812.20_106.mkv ] || ffmpeg -v error -y -ss 812.200 -i "$K" -frames:v 106 -t 4.240 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s812.20_106.mkv
[ -s biter/s817.76_47.mkv ] || ffmpeg -v error -y -ss 817.760 -i "$K" -frames:v 47 -t 1.880 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s817.76_47.mkv
[ -s biter/s819.80_138.mkv ] || ffmpeg -v error -y -ss 819.800 -i "$K" -frames:v 138 -t 5.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s819.80_138.mkv
[ -s biter/s826.04_26.mkv ] || ffmpeg -v error -y -ss 826.040 -i "$K" -frames:v 26 -t 1.040 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s826.04_26.mkv
[ -s biter/s827.36_77.mkv ] || ffmpeg -v error -y -ss 827.360 -i "$K" -frames:v 77 -t 3.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s827.36_77.mkv
[ -s biter/s830.76_30.mkv ] || ffmpeg -v error -y -ss 830.760 -i "$K" -frames:v 30 -t 1.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s830.76_30.mkv
[ -s biter/s832.64_27.mkv ] || ffmpeg -v error -y -ss 832.640 -i "$K" -frames:v 27 -t 1.080 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s832.64_27.mkv
[ -s biter/s834.56_34.mkv ] || ffmpeg -v error -y -ss 834.560 -i "$K" -frames:v 34 -t 1.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s834.56_34.mkv
[ -s biter/s836.52_19.mkv ] || ffmpeg -v error -y -ss 836.520 -i "$K" -frames:v 19 -t 0.760 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s836.52_19.mkv
[ -s biter/s837.48_48.mkv ] || ffmpeg -v error -y -ss 837.480 -i "$K" -frames:v 48 -t 1.920 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s837.48_48.mkv
[ -s biter/s839.80_34.mkv ] || ffmpeg -v error -y -ss 839.800 -i "$K" -frames:v 34 -t 1.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s839.80_34.mkv
[ -s biter/s841.44_42.mkv ] || ffmpeg -v error -y -ss 841.440 -i "$K" -frames:v 42 -t 1.680 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s841.44_42.mkv
[ -s biter/s843.44_103.mkv ] || ffmpeg -v error -y -ss 843.440 -i "$K" -frames:v 103 -t 4.120 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s843.44_103.mkv
[ -s biter/s848.48_80.mkv ] || ffmpeg -v error -y -ss 848.480 -i "$K" -frames:v 80 -t 3.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s848.48_80.mkv
[ -s biter/s852.92_40.mkv ] || ffmpeg -v error -y -ss 852.920 -i "$K" -frames:v 40 -t 1.600 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s852.92_40.mkv
[ -s biter/s855.16_116.mkv ] || ffmpeg -v error -y -ss 855.160 -i "$K" -frames:v 116 -t 4.640 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s855.16_116.mkv
[ -s biter/s860.44_166.mkv ] || ffmpeg -v error -y -ss 860.440 -i "$K" -frames:v 166 -t 6.640 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s860.44_166.mkv
[ -s biter/s867.28_132.mkv ] || ffmpeg -v error -y -ss 867.280 -i "$K" -frames:v 132 -t 5.280 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s867.28_132.mkv
[ -s biter/s873.92_108.mkv ] || ffmpeg -v error -y -ss 873.920 -i "$K" -frames:v 108 -t 4.320 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s873.92_108.mkv
[ -s biter/s879.72_93.mkv ] || ffmpeg -v error -y -ss 879.720 -i "$K" -frames:v 93 -t 3.720 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s879.72_93.mkv
[ -s biter/s998.00_28.mkv ] || ffmpeg -v error -y -ss 998.000 -i "$K" -frames:v 28 -t 1.120 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s998.00_28.mkv
[ -s biter/s999.48_13.mkv ] || ffmpeg -v error -y -ss 999.480 -i "$K" -frames:v 13 -t 0.520 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s999.48_13.mkv
[ -s biter/s1000.32_89.mkv ] || ffmpeg -v error -y -ss 1000.320 -i "$K" -frames:v 89 -t 3.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1000.32_89.mkv
[ -s biter/s1004.48_72.mkv ] || ffmpeg -v error -y -ss 1004.480 -i "$K" -frames:v 72 -t 2.880 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1004.48_72.mkv
[ -s biter/s1007.56_164.mkv ] || ffmpeg -v error -y -ss 1007.560 -i "$K" -frames:v 164 -t 6.560 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1007.56_164.mkv
[ -s biter/s1014.36_55.mkv ] || ffmpeg -v error -y -ss 1014.360 -i "$K" -frames:v 55 -t 2.200 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1014.36_55.mkv
[ -s biter/s1016.76_224.mkv ] || ffmpeg -v error -y -ss 1016.760 -i "$K" -frames:v 224 -t 8.960 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1016.76_224.mkv
[ -s biter/s1025.96_121.mkv ] || ffmpeg -v error -y -ss 1025.960 -i "$K" -frames:v 121 -t 4.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1025.96_121.mkv
[ -s biter/s1031.76_99.mkv ] || ffmpeg -v error -y -ss 1031.760 -i "$K" -frames:v 99 -t 3.960 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1031.76_99.mkv
[ -s biter/s1035.88_76.mkv ] || ffmpeg -v error -y -ss 1035.880 -i "$K" -frames:v 76 -t 3.040 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1035.88_76.mkv
[ -s biter/s1039.16_94.mkv ] || ffmpeg -v error -y -ss 1039.160 -i "$K" -frames:v 94 -t 3.760 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1039.16_94.mkv
[ -s biter/s1043.08_153.mkv ] || ffmpeg -v error -y -ss 1043.080 -i "$K" -frames:v 153 -t 6.120 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1043.08_153.mkv
[ -s biter/s1050.36_172.mkv ] || ffmpeg -v error -y -ss 1050.360 -i "$K" -frames:v 172 -t 6.880 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1050.36_172.mkv
[ -s biter/s1058.16_133.mkv ] || ffmpeg -v error -y -ss 1058.160 -i "$K" -frames:v 133 -t 5.320 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1058.16_133.mkv
[ -s biter/s1102.04_409.mkv ] || ffmpeg -v error -y -ss 1102.040 -i "$K" -frames:v 409 -t 16.360 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1102.04_409.mkv
[ -s biter/s1118.56_96.mkv ] || ffmpeg -v error -y -ss 1118.560 -i "$K" -frames:v 96 -t 3.840 -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/s1118.56_96.mkv
cat > liste.txt <<'SLUTT'
file biter/s24.96_259.mkv
file biter/s141.72_138.mkv
file biter/s147.88_172.mkv
file biter/s177.84_138.mkv
file biter/s189.64_90.mkv
file biter/s193.44_161.mkv
file biter/s212.64_321.mkv
file biter/s225.64_119.mkv
file biter/s230.72_114.mkv
file biter/s235.52_102.mkv
file biter/s240.48_107.mkv
file biter/s245.00_35.mkv
file biter/s247.84_50.mkv
file biter/s306.96_47.mkv
file biter/s309.24_6.mkv
file biter/s310.16_7.mkv
file biter/s310.72_121.mkv
file biter/s315.80_158.mkv
file biter/s322.32_80.mkv
file biter/s332.40_225.mkv
file biter/s341.56_160.mkv
file biter/s359.56_36.mkv
file biter/s361.12_58.mkv
file biter/s370.12_215.mkv
file biter/s394.68_395.mkv
file biter/s415.12_77.mkv
file biter/s418.44_229.mkv
file biter/s427.76_120.mkv
file biter/s433.12_58.mkv
file biter/s435.60_32.mkv
file biter/s437.64_13.mkv
file biter/s438.68_16.mkv
file biter/s439.68_62.mkv
file biter/s443.08_182.mkv
file biter/s450.76_81.mkv
file biter/s454.40_84.mkv
file biter/s459.12_125.mkv
file biter/s464.28_38.mkv
file biter/s597.52_73.mkv
file biter/s600.60_96.mkv
file biter/s605.28_70.mkv
file biter/s609.24_75.mkv
file biter/s612.40_40.mkv
file biter/s627.84_38.mkv
file biter/s629.56_105.mkv
file biter/s635.76_26.mkv
file biter/s638.84_90.mkv
file biter/s654.52_200.mkv
file biter/s662.64_56.mkv
file biter/s665.04_226.mkv
file biter/s674.72_76.mkv
file biter/s688.28_14.mkv
file biter/s689.56_188.mkv
file biter/s697.48_59.mkv
file biter/s713.36_130.mkv
file biter/s774.16_253.mkv
file biter/s787.12_101.mkv
file biter/s791.36_81.mkv
file biter/s795.16_78.mkv
file biter/s798.88_96.mkv
file biter/s804.16_179.mkv
file biter/s812.20_106.mkv
file biter/s817.76_47.mkv
file biter/s819.80_138.mkv
file biter/s826.04_26.mkv
file biter/s827.36_77.mkv
file biter/s830.76_30.mkv
file biter/s832.64_27.mkv
file biter/s834.56_34.mkv
file biter/s836.52_19.mkv
file biter/s837.48_48.mkv
file biter/s839.80_34.mkv
file biter/s841.44_42.mkv
file biter/s843.44_103.mkv
file biter/s848.48_80.mkv
file biter/s852.92_40.mkv
file biter/s855.16_116.mkv
file biter/s860.44_166.mkv
file biter/s867.28_132.mkv
file biter/s873.92_108.mkv
file biter/s879.72_93.mkv
file biter/s998.00_28.mkv
file biter/s999.48_13.mkv
file biter/s1000.32_89.mkv
file biter/s1004.48_72.mkv
file biter/s1007.56_164.mkv
file biter/s1014.36_55.mkv
file biter/s1016.76_224.mkv
file biter/s1025.96_121.mkv
file biter/s1031.76_99.mkv
file biter/s1035.88_76.mkv
file biter/s1039.16_94.mkv
file biter/s1043.08_153.mkv
file biter/s1050.36_172.mkv
file biter/s1058.16_133.mkv
file biter/s1102.04_409.mkv
file biter/s1118.56_96.mkv
SLUTT
ffmpeg -v error -y -f concat -safe 0 -i liste.txt -c copy opptak.mkv
ffprobe -v error -show_entries format=duration -of csv=p=0 opptak.mkv
