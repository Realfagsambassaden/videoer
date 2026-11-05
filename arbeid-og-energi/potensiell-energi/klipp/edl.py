# Klippeliste for «Potensiell energi»: kildetider i opptaket (MEG.mov), finjustert til stille punkter.
import json, numpy as np, soundfile as sf
lyd, sr = sf.read('/home/claude/work/asr/lyd16k.wav', dtype='float32')
vad = json.load(open('/home/claude/work/asr/tekst.json'))   # korte taleavsnitt (VAD)
KLIPP = [  # (start, slutt, merke, handling) – handling=True: ikke stram inn pauser (læreren gjør noe)
 (0.2, 12.4, 'kald', True), (14.5, 16.5, 'kald', True),
 (19.3, 23.9, 'a1', False), (26.4, 36.4, 'a2', True), (48.1, 56.5, 'a3', False), (63.3, 65.8, 'a4', False),
 (66.6, 78.3, 'a5', False), (78.3, 81.0, 'a6', True), (102.3, 106.9, 'a7', False), (107.9, 109.6, 'a8', False),
 (160.3, 173.5, 'b1', True), (174.4, 184.4, 'b2', False), (192.1, 200.4, 'b3', False), (213.4, 219.8, 'b4', False),
 (258.2, 266.3, 'c1', False), (276.1, 278.05, 'c2', False), (280.6, 286.0, 'c3', False), (289.7, 293.7, 'c4', False),
 (306.3, 322.0, 'c5', False), (329.7, 341.5, 'c6', False), (342.3, 343.75, 'c7', False), (591.3, 593.1, 'c8', False),
 (344.62, 346.0, 'c9', False),
 (376.6, 401.6, 'd1', False), (421.8, 439.3, 'd2', False), (442.8, 455.9, 'd3', False),
 (513.4, 527.7, 'e1', False), (537.8, 545.0, 'e2', True), (549.6, 555.0, 'e2', True), (616.0, 628.4, 'e3', False), (556.3, 557.55, 'e4', False),
]
def rms(t): i = int(t * sr); w = lyd[max(0, i - 160):i + 160]; return float(np.sqrt(np.mean(w * w))) if len(w) else 0
def snap(t, r=0.12):
    c = np.arange(t - r, t + r + 1e-9, 0.01); return float(c[np.argmin([rms(x) for x in c])])
ut = []
for s, e, m, h in KLIPP:
    s, e = snap(s), snap(e)
    deler = [(s, e)]
    if not h:   # stram inn pauser over 0.85 s inne i klippet til ca. 0.5 s
        stille = [tuple(map(float, l.split())) for l in open('stille.txt')]
        deler = []; cur = s
        for a, b in stille:
            if a > s + 0.2 and b < e - 0.2 and b - a > 0.85:
                deler.append((cur, a + 0.25)); cur = b - 0.25
        deler.append((cur, e))
    for a, b in deler: ut.append({'start': round(a, 3), 'slutt': round(b, 3), 'merke': m})
t = 0
for d in ut: d['ny'] = round(t, 3); t += d['slutt'] - d['start']
json.dump(ut, open('edl.json', 'w'), indent=1)
print(len(ut), 'biter, lengde', round(t, 1), 's')
from collections import OrderedDict
o = OrderedDict()
for d in ut: o.setdefault(d['merke'], [d['ny'], 0]); o[d['merke']][1] = round(d['ny'] + d['slutt'] - d['start'], 2)
for k, v in o.items(): print(k, v)
