# Klippeliste for Kinetisk energi. Tider i lyd16k.wav (lydsporet); fil-tid = lydtid + 0.08.
# (a, b, ekstra hale) – a/b er taleøyene; polstring 0.15 før og 0.20 etter.
import json, math
B = [
 (26.0, 32.75, 0), (34.05, 37.06, 0),              # dytt + «Når jeg tar og dytter … Arbeid er overføring av energi»
 (39.78, 41.78, 0), (42.70, 45.77, 0),             # Hvor ble det av energien nå? Jo, den ligger lagret i bevegelsen
 (52.02, 60.48, 0.5),                              # Energi som et legeme har …
 (68.50, 70.10, 0), (71.62, 87.31, 0.5),           # Tenk at bilen står stille … F dx
 (106.25, 112.25, 0), (113.81, 118.61, 0),         # Newton 2, a = dv/dt
 (188.11, 216.57, 0), (218.55, 223.33, 0),         # m dv/dt · v dt … graf … areal under grafen
 (232.60, 238.85, 0), (252.89, 261.29, 0.5),       # trekant, ½ g h, ½mv²
 (271.33, 277.15, 0), (278.44, 286.65, 0),         # kinetisk energi
 (290.71, 293.13, 0), (294.21, 301.16, 0), (302.22, 305.46, 0),
 (326.77, 333.41, 0.5),                            # arbeid-energi-setningen
 (360.48, 365.36, 0), (366.37, 367.62, 0), (369.70, 379.71, 0),
 (392.12, 404.31, 0.5),                            # nerdete + poenget
 (441.42, 447.20, 0), (448.20, 450.39, 0), (454.88, 458.55, 0),
 (459.75, 469.51, 0), (470.70, 476.30, 0.5),       # eksempel
 (512.37, 521.41, 0), (526.89, 532.30, 0),         # stoppe bilen, kollisjon, «Gikk det bra, eller?»
 (538.95, 542.20, 0), (544.76, 545.16, 0.6),       # Ok, det var kinetisk energi. Prøv deg på noen oppgaver. Snakkes.
]
OFF = 0.08; G = 0.04
ut = []; nT = 0.0
for a, b, hale in B:
    s = math.floor((a - 0.15 + OFF) / G) * G
    e = math.ceil((b + 0.20 + hale + OFF) / G) * G
    if ut and s < ut[-1]['start'] + ut[-1]['lengde']:   # overlapp med forrige: start der den sluttet
        s = ut[-1]['start'] + ut[-1]['lengde']
    n = round((e - s) / G)
    ut.append(dict(kilde=[a, b], start=round(s, 2), frames=n, lengde=round(n * G, 2), nT0=round(nT, 2)))
    nT += n * G
json.dump(ut, open('edl.json', 'w'), indent=1)
print(len(ut), 'biter, total', round(nT, 2), 's')
with open('kutt.sh', 'w') as f:
    f.write('set -e\nK="../Meg.mov"\nmkdir -p biter\n')
    for i, d in enumerate(ut):
        f.write(f'ffmpeg -v error -y -ss {d["start"]:.3f} -i "$K" -frames:v {d["frames"]} -t {d["lengde"]:.3f} -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c{i:02d}.mkv\n')
    f.write('ls biter/*.mkv | sed "s/^/file /" > liste.txt\nffmpeg -v error -y -f concat -safe 0 -i liste.txt -c copy opptak.mkv\nffprobe -v error -show_entries format=duration -of csv=p=0 opptak.mkv\n')
