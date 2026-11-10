#!/usr/bin/env python3
"""Utkast 4: lyden til opptak3.mkv (se lag_opptak3.sh) med «Da vil» satt sammen.
Bruk: python3 dubb.py <opptak3.mkv> <tale.wav>
Biten T 74.12–74.80 er klippet fra stammingen (fil 309.24, 17 bilder). Første «Da» (hel, med naturlig utklang)
beholdes (0–0.48 s), og «vil» hentes fra «Det vil si» (T 248.68–248.87) og legges rett etter.
(Utkast 3 kuttet «Da» midt i vokalen og hadde digital stillhet – læreren hørte noe rart.)"""
import sys, subprocess, numpy as np, soundfile as sf
sr = 48000
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', sys.argv[1], '-vn', '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, np.float32).copy()
i = lambda t: int(round(t * sr))
vil = x[i(248.68):i(248.87)].copy(); f = i(0.012); vil[:f] *= np.linspace(0, 1, f); vil[-f:] *= np.linspace(1, 0, f)
a, b = i(74.12 + 0.44), i(74.12 + 0.50)
x[a:b] *= np.linspace(1, 0, b - a)
rom = x[i(74.00):i(74.10)]                         # romtone i stedet for digital stillhet
for k in range(b, i(74.80), len(rom)):
    n = min(len(rom), i(74.80) - k); x[k:k + n] = rom[:n]
k = i(74.12 + 0.49); x[k:k + len(vil)] += vil
sf.write(sys.argv[2], x, sr); print('tale:', sys.argv[2], len(x) / sr, 's')
