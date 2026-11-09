#!/usr/bin/env python3
"""Lyden til Energibevaring: tale fra det klippede opptaket + effekter. Bruk: python3 lyd.py <tale.wav> <ut.wav>"""
import sys, numpy as np, soundfile as sf
from pathlib import Path
LYD = Path(__file__).resolve().parents[2] / '_verktoy' / 'lyd'
import json
H = Path(__file__).resolve().parent
O = json.load(open(H / 'klipp' / 'edl_utkast1.json')); N = json.load(open(H / 'klipp' / 'edl.json'))
ns = {d['start']: d for d in N}
KLIPP = [(o['nT0'], o['nT0'] + o['lengde'], ns[o['start']]['nT0'], ns[o['start']]['lengde']) for o in O]
def R(T):   # tid i klippet til utkast 1 → tid i nytt klipp (samme som R() i innhold.js)
    for a, b, n, l in KLIPP:
        if T < b: return n + min(max(T - a, 0), l)
    return KLIPP[-1][2] + KLIPP[-1][3]
KUTT0, KUTT1 = 119.68, 132.56   # utkast 3: fjær-sammenpressingen kuttet (som C() i innhold.js)
C = lambda T2: T2 if T2 < KUTT0 else KUTT0 if T2 < KUTT1 else T2 - (KUTT1 - KUTT0)
KALD, TITTEL, LENGDE_KLIPP = 10.4, 1.6, round(N[-1]['nT0'] + N[-1]['lengde'] - (KUTT1 - KUTT0), 2)
MN = lambda Tn: Tn if Tn < KALD else KALD + TITTEL + (Tn - KALD)
M = lambda T: MN(C(R(T)))
sr = 48000
tale, _ = sf.read(sys.argv[1], dtype='float32')
if tale.ndim > 1: tale = tale.mean(1)
ut = np.zeros(int((LENGDE_KLIPP + TITTEL) * sr) + sr, np.float32)
def legg(x, t, v=1.0):
    if x.ndim > 1: x = x.mean(1)
    i = int(t * sr); n = min(len(x), len(ut) - i); ut[i:i + n] += x[:n] * v
k = int(KALD * sr); legg(tale[:k], 0); legg(tale[k:], M(KALD))
E = {n: sf.read(LYD / f'{n}.wav', dtype='float32')[0] for n in ('svisj', 'pop', 'boing')}
legg(E['svisj'], KALD - 0.3, .3)
for s in (38.3, 72.2, 116.2, 197.9, 236.2, 326.4, 386.4): legg(E['svisj'], M(s) - .3, .35)
for T in (7.0, 92.6, 95.5, 183.3, 222.2, 261.0, 318.4, 341.1, 357.2, 368.6, 383.9): legg(E['pop'], M(T), .25)
legg(E['boing'], M(53.0), .35); legg(E['boing'], M(143.2), .45)
for T in (336.4,): legg(E['svisj'], M(T), .2)
sf.write(sys.argv[2], np.clip(np.stack([ut, ut], 1)[:int((LENGDE_KLIPP + TITTEL) * sr)], -1, 1), sr)
print('lyd', sys.argv[2])
