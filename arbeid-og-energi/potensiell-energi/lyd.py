#!/usr/bin/env python3
"""Lager lyden til animasjonsdelen: talen fra det klippede opptaket + lydeffekter (svisj, pop, boing).
Bruk: python3 lyd.py <tale.wav> <ut.wav>
Tider for effektene skrives i T = tid i FØRSTE klipp (klipp/edl.json); R() oversetter til nytt klipp (klipp/edl2.json),
akkurat som M() i anim.mal.html."""
import sys, json, numpy as np, soundfile as sf
from pathlib import Path
H = Path(__file__).resolve().parent; LYD = H.parents[1] / '_verktoy' / 'lyd'
KLIPP = [(d['gT0'], d['gT1'], d['nT0']) for d in json.load(open(H / 'klipp' / 'edl2.json'))]
def R(T):
    for a, b, n in KLIPP:
        if T < a: return n
        if T <= b: return n + T - a
    a, b, n = KLIPP[-1]; return n + b - a
KALD, TITTEL, HOVED, DASH = 14.5, 1.6, 217.45, 5.5
M = lambda T: R(T) + TITTEL
LENGDE = KALD + TITTEL + HOVED + DASH; D = KALD + TITTEL + HOVED
sr = 48000
tale, _ = sf.read(sys.argv[1], dtype='float32')
if tale.ndim > 1: tale = tale.mean(1)
ut = np.zeros(int(LENGDE * sr) + sr, np.float32)
def legg(x, t, v=1.0):
    if x.ndim > 1: x = x.mean(1)
    i = int(t * sr); n = min(len(x), len(ut) - i); ut[i:i + n] += x[:n] * v
legg(tale[:int(KALD * sr)], 0)
legg(tale[int(KALD * sr):], KALD + TITTEL)
EFF = {n: sf.read(LYD / f'{n}.wav', dtype='float32')[0] for n in ('svisj', 'pop', 'boing')}
for n, t, v in [('svisj', KALD + TITTEL - 0.3, .3), ('pop', M(51.6), .3), ('boing', M(71.95), .45), ('svisj', M(71.95) + 0.05, .25), ('boing', M(144.2), .45),
                ('svisj', M(60.53) - .3, .35), ('svisj', M(98.63) - .3, .35), ('svisj', M(149.92) - .3, .35), ('svisj', M(203.06) - .3, .35),
                ('svisj', D - .3, .35), ('pop', D + .15, .25), ('pop', D + 1.15, .25), ('pop', D + 2.25, .25), ('boing', D + 2.75, .5), ('svisj', D + 2.95, .3)]:
    legg(EFF[n], t, v)
ut = ut[:int(LENGDE * sr)]
sf.write(sys.argv[2], np.clip(np.stack([ut, ut], 1), -1, 1), sr)
print('lyd:', sys.argv[2], round(LENGDE, 2), 's')
