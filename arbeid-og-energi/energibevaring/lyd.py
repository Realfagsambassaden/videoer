#!/usr/bin/env python3
"""Lyden til Energibevaring: tale fra det klippede opptaket + effekter. Bruk: python3 lyd.py <tale.wav> <ut.wav>"""
import sys, numpy as np, soundfile as sf
from pathlib import Path
LYD = Path(__file__).resolve().parents[2] / '_verktoy' / 'lyd'
KALD, TITTEL, LENGDE_KLIPP = 10.4, 1.6, 406.8
M = lambda T: T if T < KALD else KALD + TITTEL + (T - KALD)
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
for T in (7.0, 92.6, 95.5, 131.0, 222.2, 261.0, 318.4, 341.1, 357.2, 368.6, 383.9): legg(E['pop'], M(T), .25)
legg(E['boing'], M(53.0), .35); legg(E['boing'], M(143.2), .45)
for T in (336.4,): legg(E['svisj'], M(T), .2)
sf.write(sys.argv[2], np.clip(np.stack([ut, ut], 1)[:int((LENGDE_KLIPP + TITTEL) * sr)], -1, 1), sr)
print('lyd', sys.argv[2])
