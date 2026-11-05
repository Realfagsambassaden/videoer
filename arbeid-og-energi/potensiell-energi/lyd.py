#!/usr/bin/env python3
"""Lager lyden til animasjonsdelen: talen fra det klippede opptaket + lydeffekter (svisj, pop, boing).
Bruk: python3 lyd.py <tale.wav> <ut.wav>   (tider i G = animasjonstid; T = tid i det klippede opptaket)"""
import sys, numpy as np, soundfile as sf
from pathlib import Path
LYD = Path(__file__).resolve().parents[2] / '_verktoy' / 'lyd'
sr = 48000; LENGDE = 250.433; M = lambda T: T + 2.6; D = 244.92
tale, _ = sf.read(sys.argv[1], dtype='float32')
ut = np.zeros((int(LENGDE * sr), 2), np.float32)
def legg(x, t, v=1.0):
    i = int(t * sr); n = min(len(x), len(ut) - i); ut[i:i + n] += x[:n] * v
legg(tale[:int(14.5 * sr)], 0)
legg(tale[int(14.5 * sr):], 17.1)
EFF = {n: sf.read(LYD / f'{n}.wav', dtype='float32')[0] for n in ('svisj', 'pop', 'boing')}
for n, t, v in [('pop', 14.6, .25), ('svisj', 16.85, .35), ('pop', M(51.6), .3), ('boing', M(72.3), .4), ('boing', M(143.4), .4),
                ('svisj', M(60.53) - .3, .35), ('svisj', M(98.63) - .3, .35), ('svisj', M(149.92) - .3, .35), ('svisj', M(203.06) - .3, .35),
                ('svisj', D - .3, .35), ('pop', D + .15, .25), ('pop', D + 1.15, .25), ('pop', D + 2.25, .25), ('boing', D + 2.75, .5), ('svisj', D + 2.95, .3)]:
    legg(EFF[n], t, v)
sf.write(sys.argv[2], np.clip(ut, -1, 1), sr)
print('lyd:', sys.argv[2])
