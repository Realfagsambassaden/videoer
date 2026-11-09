#!/usr/bin/env python3
"""Utkast 3: lyden til opptaket (klippet etter edl.json, så fjær-sammenpressingen 119.68–132.56 kuttet bort, se
sett.sh) med «vil» lagt inn over stammingen. Bruk: python3 dubb.py <opptak2.mkv> <tale.wav>
«Da vil» ble hørt som «dall»: «Da» står (T 74.12–74.36), «vil» hentes fra «Det vil si» (T 251.44–251.63) og
legges over T 74.36–74.64 (resten stille)."""
import sys, subprocess, numpy as np, soundfile as sf
sr = 48000
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', sys.argv[1], '-vn', '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, np.float32).copy()
i = lambda t: int(round(t * sr))
vil = x[i(251.44):i(251.63)].copy(); f = i(0.012); vil[:f] *= np.linspace(0, 1, f); vil[-f:] *= np.linspace(1, 0, f)
x[i(74.36):i(74.64)] = 0; x[i(74.37):i(74.37) + len(vil)] = vil
sf.write(sys.argv[2], x, sr); print('tale:', sys.argv[2], len(x) / sr, 's')
