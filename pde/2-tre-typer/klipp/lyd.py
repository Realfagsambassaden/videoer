# Lyden til hoveddelen: talen (film2_tale.wav) + pop/svisj fra effekter.json. Kjør fra videomappa.
import sys, json, numpy as np, soundfile as sf
tale, ut = sys.argv[1], sys.argv[2]
x, sr = sf.read(tale, dtype='float32')
if x.ndim > 1: x = x.mean(1)
VT = '../../_verktoy/lyd/'
for t, f in json.load(open('klipp/effekter.json')):
    e, er = sf.read(VT + f + '.wav', dtype='float32')
    if e.ndim > 1: e = e.mean(1)
    if er != sr: e = np.interp(np.arange(0, len(e), er / sr), np.arange(len(e)), e)
    i = int(t * sr); e = e[:max(0, len(x) - i)] * (0.30 if f == 'svisj' else 0.45)
    x[i:i + len(e)] += e
sf.write(ut, np.stack([x, x], 1), sr, subtype='PCM_16')
