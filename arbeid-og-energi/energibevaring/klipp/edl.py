# Klippeliste for Energibevaring. Tider i lyd16k.wav (lydsporet); fil-tid = lydtid + 0.08.
# Hvert utvalg (a, b, hel, hale): hel=True beholder alt (rekvisitter/gester), ellers deles det i taleøyer
# og pauser over 0.45 s strammes inn. Bruk: python3 edl.py <lyd16k.wav>
import json, math, sys
import numpy as np, soundfile as sf
U = [
 # kald start: ballen slippes for tredje gang, spretter, «Hvorfor kommer den aldri tilbake helt opp dit den startet?»
 (24.9, 34.94, True, 0.3),
 # 1 energien bytter form
 (141.6, 154.46, False, 0), (177.76, 183.10, False, 0), (189.56, 199.08, False, 0.5),
 # 2 Dashman i rampa (med «idealisert»)
 (212.56, 249.06, False, 0.5),
 # 3 eksempel: rampa 2 m
 (306.9, 308.58, False, 0), (310.66, 325.24, False, 0), (332.34, 347.68, False, 0), (359.48, 363.18, False, 0), (370.08, 377.94, False, 0.5),
 # 4 fjærkraften: fjæra presses (hel), fjærkanonen, høyden
 (394.62, 407.38, True, 0), (415.04, 432.30, False, 0), (433.04, 441.88, False, 0), (443.02, 465.52, False, 0),
 (597.44, 607.80, False, 0), (609.18, 613.74, False, 0), (627.76, 633.50, False, 0), (635.70, 636.52, False, 0), (638.78, 641.68, False, 0.5),
 # 5 hvor ble det av energien
 (654.44, 677.50, False, 0), (688.20, 688.62, False, 0), (689.48, 699.56, False, 0), (713.30, 717.80, False, 0.5),
 # 6 konservative krefter
 (774.08, 784.02, False, 0), (787.04, 816.18, False, 0), (817.70, 851.42, False, 0), (852.86, 882.86, False, 0.3),
 (997.92, 1056.66, False, 0.3), (1058.12, 1063.22, False, 0.5),
 # avslutning
 (1102.0, 1121.6, False, 0.6),
]
lyd, sr = sf.read(sys.argv[1] if len(sys.argv) > 1 else 'lyd16k.wav', dtype='float32')
h = 160; db = 20 * np.log10(np.array([np.sqrt((lyd[i:i + h] ** 2).mean()) for i in range(0, len(lyd) - h, h)]) + 1e-9)
def oyer(a, b, thr=-50, gap=0.45):
    t = db[int(a * 100):int(b * 100)] > thr; ut = []; st = None; sil = 0
    for k, v in enumerate(t):
        if v:
            if st is None: st = k
            sil = 0; en = k
        elif st is not None:
            sil += 1
            if sil >= gap * 100: ut.append([a + st / 100, a + en / 100 + 0.01]); st = None
    if st is not None: ut.append([a + st / 100, a + en / 100 + 0.01])
    return ut
OFF = 0.08; G = 0.04
biter = []
for a, b, hel, hale in U:
    deler = [[a, b]] if hel else [[max(a, x - 0.12), min(b, y) + 0.18] for x, y in oyer(a - 0.05, b + 0.05)]
    deler[-1][1] += hale
    for x, y in deler: biter.append((x, y))
ut = []; nT = 0.0
for x, y in biter:
    s = math.floor((x + OFF) / G) * G; e = math.ceil((y + OFF) / G) * G
    if ut and s < ut[-1]['start'] + ut[-1]['lengde'] - 1e-6: s = round(ut[-1]['start'] + ut[-1]['lengde'], 2)
    n = round((e - s) / G)
    if n < 3: continue
    ut.append(dict(kilde=[round(x, 2), round(y, 2)], start=round(s, 2), frames=n, lengde=round(n * G, 2), nT0=round(nT, 2)))
    nT += n * G
json.dump(ut, open('edl.json', 'w'), indent=1)
print(len(ut), 'biter, total', round(nT, 2), 's')
with open('kutt.sh', 'w') as f:
    f.write('set -e\nK="../Meg_Energibevaring.mov"\nmkdir -p biter\n')
    for i, d in enumerate(ut):
        f.write(f'[ -s biter/c{i:03d}.mkv ] || ffmpeg -v error -y -ss {d["start"]:.3f} -i "$K" -frames:v {d["frames"]} -t {d["lengde"]:.3f} -c:v libx264 -crf 17 -preset veryfast -pix_fmt yuv420p -r 25 -c:a pcm_s16le -ar 48000 -ac 1 biter/c{i:03d}.mkv\n')
    f.write('ls biter/c*.mkv | sed "s/^/file /" > liste.txt\nffmpeg -v error -y -f concat -safe 0 -i liste.txt -c copy opptak.mkv\nffprobe -v error -show_entries format=duration -of csv=p=0 opptak.mkv\n')
