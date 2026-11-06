#!/usr/bin/env python3
"""Lyden til animasjonsdelen av Kinetisk energi: tale fra det klippede opptaket + effekter.
Bruk: python3 lyd.py <tale.wav> <ut.wav>
Plystring, klunk, motor, bremsehvin og krasj lages her (syntetisk). Tider i T (klippet), M(T) = tid i animasjonen."""
import sys, numpy as np, soundfile as sf
from pathlib import Path
H = Path(__file__).resolve().parent; LYD = H.parents[1] / '_verktoy' / 'lyd'
import json
O = json.load(open(H / 'klipp' / 'edl_utkast1.json')); N = json.load(open(H / 'klipp' / 'edl.json'))
KLIPP = [(a['nT0'], a['nT0'] + a['lengde'], b['nT0'], b['lengde'], a['start'] - b['start']) for a, b in zip(O, N)]
def R(T):   # tid i klippet til utkast 1 → tid i nytt klipp
    for a, b, n, l, d in KLIPP:
        if T < b: return n + min(max(T - a + d, 0), l)
    return KLIPP[-1][2] + KLIPP[-1][3]
KALD, TITTEL, HOVED = 6.0, 1.6, round(N[-1]['nT0'] + N[-1]['lengde'], 2)
M = lambda T: KALD + TITTEL + R(T)
LENGDE = KALD + TITTEL + HOVED
sr = 48000; rng = np.random.default_rng(7)
t_ = lambda d: np.arange(int(d * sr)) / sr
def env(n, a=0.01, r=0.05):
    e = np.ones(n); na, nr = int(a * sr), int(r * sr)
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e
def lp(x, k):   # enkel lavpass (glidende snitt)
    return np.convolve(x, np.ones(k) / k, mode='same')

def plystring():   # en liten fornøyd melodi med vibrato
    noter = [(784, .28), (988, .28), (1175, .42), (988, .22), (1319, .5), (1175, .3), (988, .55)]
    ut = []
    for f, d in noter:
        t = t_(d); fr = f * (1 + 0.012 * np.sin(2 * np.pi * 6 * t)); ph = 2 * np.pi * np.cumsum(fr) / sr
        x = np.sin(ph) * env(len(t), .03, .06) + 0.04 * rng.standard_normal(len(t)) * env(len(t), .03, .06)
        ut.append(x)
    return 0.22 * np.concatenate(ut)
def klunk():
    t = t_(0.35); x = np.sin(2 * np.pi * (180 - 120 * t) * t) * np.exp(-t * 18) + 0.3 * lp(rng.standard_normal(len(t)), 20) * np.exp(-t * 40)
    return 0.8 * x
def motor(d, f0=45, f1=110):   # brum som stiger
    t = t_(d); f = np.linspace(f0, f1, len(t)); ph = 2 * np.pi * np.cumsum(f) / sr
    x = (np.sign(np.sin(ph)) * 0.5 + np.sin(2 * ph) * 0.5) * (1 + 0.3 * np.sin(2 * np.pi * 9 * t))
    return 0.25 * lp(x, 30) * env(len(t), .08, .4)
def hvin(d):     # bremsehvin
    t = t_(d); x = np.sin(2 * np.pi * (2400 + 150 * np.sin(2 * np.pi * 7 * t)) * t) + 0.5 * np.sin(2 * np.pi * 3100 * t)
    return 0.07 * x * env(len(t), .05, .3) * (1 - 0.5 * t / d)
def krasj():
    t = t_(1.4); s = rng.standard_normal(len(t))
    bom = np.sin(2 * np.pi * (70 - 30 * t) * t) * np.exp(-t * 5)
    knas = lp(s, 3) * np.exp(-t * 6) * 0.6
    klirr = sum(np.sin(2 * np.pi * f * t) * np.exp(-(t - d0).clip(0) * 9) * (t > d0) for f, d0 in [(3200, .05), (4100, .12), (2700, .2), (5200, .28), (3600, .36)]) * 0.12
    return 0.9 * (bom + knas + klirr)
def rygge():     # «pip pip» når bilen rygger
    t = t_(0.18); p = 0.15 * np.sin(2 * np.pi * 1500 * t) * env(len(t), .005, .02)
    z = np.zeros(int(0.18 * sr)); return np.concatenate([p, z, p, z, p])

sr_ = sr
tale, _ = sf.read(sys.argv[1], dtype='float32')
if tale.ndim > 1: tale = tale.mean(1)
ut = np.zeros(int(LENGDE * sr) + sr, np.float32)
def legg(x, t, v=1.0):
    if x.ndim > 1: x = x.mean(1)
    i = int(t * sr); n = min(len(x), len(ut) - i); ut[i:i + n] += x[:n] * v
legg(tale, M(0))
EFF = {n: sf.read(LYD / f'{n}.wav', dtype='float32')[0] for n in ('svisj', 'pop', 'boing')}
# kald start
legg(plystring(), 0.35); legg(klunk(), 3.35); legg(EFF['boing'], 3.65, .35); legg(motor(1.9), 4.1, 1.0); legg(EFF['svisj'], 4.9, .35)
# tittelkort
legg(EFF['svisj'], KALD - 0.3, .3)
# A: dytt
legg(EFF['svisj'], M(1.6), .35); legg(EFF['pop'], M(1.7), .25)
# viskelær-overganger
for s in (25.76, 44.36, 105.16, 140.04, 170.40, 199.76): legg(EFF['svisj'], M(s) - .3, .35)
# pop for stempler og bokser
for T in (61.2, 62.6, 65.5, 67.4, 79.6, 141.4, 160.3, 168.2, 189.0, 214.0): legg(EFF['pop'], M(T), .25)
for T in (60.6, 62.0, 64.9): legg(EFF['svisj'], M(T), .2)
# F: motor ved eksemplet (svakt), G: bremsing, rygging, krasj
legg(motor(2.6, 60, 90) * 0.5, M(199.9)); legg(hvin(2.6), M(202.95))
legg(rygge(), M(208.4)); legg(motor(1.4, 70, 160), M(209.6)); legg(krasj(), M(211.0)); legg(EFF['boing'], M(211.4), .35)
ut = ut[:int(LENGDE * sr)]
sf.write(sys.argv[2], np.clip(np.stack([ut, ut], 1), -1, 1), sr)
print('lyd:', sys.argv[2], round(LENGDE, 2), 's')
