# Utkast 5: ekstrataken (ut-tid 181.56–192.08) står 84 px lenger til høyre og 14 px høyere enn resten.
# Flytter den på plass (kanten fylles med grønt) før komponer.py.
ffmpeg -y -i opptak_v_orig.mkv -filter_complex "[0]split[a][b];[b]crop=1196:706:84:0,pad=1280:720:0:14,fillborders=top=14:right=84:mode=smear[s];[a][s]overlay=0:0:enable='between(t,181.55,192.07)'" -c:v libx264 -crf 12 -preset veryfast -pix_fmt yuv420p -r 25 opptak_v.mkv
