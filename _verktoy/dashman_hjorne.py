#!/usr/bin/env python3
"""Animert Dashman nede i høyre hjørne, oppå en ferdig tavlevideo.
Bruk: python3 _verktoy/dashman_hjorne.py <tavle.mp4> <tale.wav> <poser.json> <ut.mp4> [--start S]
- poser.json: [[t, "positur", speil(0/1)], ...] i sekunder i tavlevideoen (fra og med t gjelder posituren).
  Valgfritt "ekstra": [[t0, t1, "lyspaere"|"svette_a"|"spm"|"utrop"], ...] som dict {"poser": [...], "ekstra": [...]}.
- tale.wav: lyden som hører til tavlevideoen fra --start (s) (standard 0); munnen følger lyden.
Riggen hentes fra Dashman-repoet (../dashman/rigg ved siden av videoer, eller DASHMAN_RIGG)."""
import json, os, sys, subprocess, numpy as np, soundfile as sf
from PIL import Image, ImageFilter
from scipy import ndimage
a = sys.argv[1:]; START = 0.0
if '--start' in a: i = a.index('--start'); START = float(a[i + 1]); del a[i:i + 2]
TAVLE, TALE, POSER, UT = a
RIGG = os.environ.get('DASHMAN_RIGG') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'dashman', 'rigg')
R = json.load(open(f'{RIGG}/rigg.json'))
P = json.load(open(POSER)); EKSTRA = []
if isinstance(P, dict): EKSTRA = P.get('ekstra', []); P = P['poser']
W, H = 1920, 1080; FPS = 30; HOYDE = 600; BUNN = 1062; MIDT = 1600
info = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', TAVLE], capture_output=True, text=True).stdout
N = int(float(info) * FPS)
x, sr = sf.read(TALE, dtype='float32')
if x.ndim > 1: x = x.mean(1)
def munn(i):
    t = i / FPS - START
    if t < 0: return 'lukket'
    s = x[int(t * sr):int((t + 1 / FPS) * sr)]
    if len(s) < 32: return 'lukket'
    d = 20 * np.log10(np.sqrt((s ** 2).mean()) + 1e-9)
    if d < -38: return 'lukket'
    X = np.abs(np.fft.rfft(s * np.hanning(len(s)))); f = np.fft.rfftfreq(len(s), 1 / sr); m = (f > 100) & (f < 5000)
    c = (X[m] * f[m]).sum() / (X[m].sum() + 1e-9)
    return 'o' if c < 700 else 'aapen' if c < 1500 else 'smil_tenner'
form = [munn(i) for i in range(N)]
for i in range(1, N - 1):
    if form[i - 1] == form[i + 1] != form[i]: form[i] = form[i - 1]
MUNN = {k: Image.open(f'{RIGG}/deler/munn_{k}.png') for k in ('lukket', 'o', 'aapen', 'smil_tenner')}
OYNE_L = Image.open(f'{RIGG}/deler/oyne_lukket_v.png')
EKS = {}
def tykk(im, k=3):
    al = im.split()[3].filter(ImageFilter.MaxFilter(k)); out = Image.new('RGBA', im.size, (236, 239, 230, 0)); out.putalpha(al); return out
BUF = {}
def pose(n, m, blunk):
    key = (n, m, blunk)
    if key in BUF: return BUF[key]
    im = Image.open(f'{RIGG}/deler/{n}.png').convert('RGBA'); arr = np.asarray(im).copy(); r = R.get(n, {})
    lab, _ = ndimage.label(arr[..., 3] > 40, structure=np.ones((3, 3)))
    if 'munn' in r and m: 
        for k in r['munn_komp']: arr[lab == k, 3] = 0
    if blunk and 'oyne' in r:
        for k in r['oyne_komp']: arr[lab == k, 3] = 0
    im = Image.fromarray(arr)
    if 'munn' in r and m:
        mm = MUNN[m]; x0, y0, x1, y1 = r['munn']; w = int((x1 - x0) * {'lukket': 1.0, 'smil_tenner': 0.9, 'o': 0.55, 'aapen': 0.8}[m]); w = max(w, 10)
        mm = mm.resize((w, max(4, int(mm.height * w / mm.width))), Image.LANCZOS)
        im.alpha_composite(mm, (int((x0 + x1) / 2 - mm.width / 2), int((y0 + y1) / 2 - mm.height / 2)))
    if blunk and 'oyne' in r:
        x0, y0, x1, y1 = r['oyne']; o = OYNE_L.resize((int((x1 - x0) * 0.45), max(4, int(OYNE_L.height * (x1 - x0) * 0.45 / OYNE_L.width))))
        for cx in (x0 + (x1 - x0) * 0.27, x0 + (x1 - x0) * 0.73): im.alpha_composite(o, (int(cx - o.width / 2), int((y0 + y1) / 2 - o.height / 3)))
    im = tykk(im); BUF[key] = im; return im
rng = np.random.default_rng(3); BLUNK = []; t = 1.5
while t < N / FPS: BLUNK.append(t); t += rng.uniform(2.5, 5.5)
P = sorted(P)
dek = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', TAVLE, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-r', str(FPS), '-'], stdout=subprocess.PIPE)
enk = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', UT], stdin=subprocess.PIPE)
for i in range(N):
    raw = dek.stdout.read(W * H * 3)
    if len(raw) < W * H * 3: break
    fr = Image.frombytes('RGB', (W, H), raw).convert('RGBA'); t = i / FPS
    cur = [p for p in P if p[0] <= t]; st, n, sp = cur[-1] if cur else (0, 'noytral', 0)
    r = R.get(n, {}); bl = any(0 <= t - b < 0.13 for b in BLUNK)
    im = pose(n, form[i] if 'munn' in r else None, bl)
    if sp: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    sk = HOYDE / max(im.height, 540) * (1 + 0.006 * np.sin(2 * np.pi * t / 3.1))
    hopp = -16 * (1 - (t - st) / 0.18) if 0 < t - st < 0.18 and st > 0 else 0
    im2 = im.resize((max(1, int(im.width * sk)), max(1, int(im.height * sk))), Image.LANCZOS).rotate(1.2 * np.sin(2 * np.pi * t / 4.3), resample=Image.BICUBIC, expand=True)
    x0 = int(MIDT - im2.width / 2); y0 = int(BUNN - im2.height + hopp)
    fr.alpha_composite(im2, (x0, y0))
    for e0, e1, en in EKSTRA:
        if e0 <= t < e1:
            if en not in EKS: EKS[en] = tykk(Image.open(f'{RIGG}/deler/{en}.png').convert('RGBA'))
            e = EKS[en]; s2 = 110 / max(e.height, 1); e = e.resize((int(e.width * s2), int(e.height * s2)))
            fr.alpha_composite(e, (int(MIDT + 70), int(y0 - 40 - 10 * np.sin(6 * (t - e0)))))
    enk.stdin.write(fr.convert('RGB').tobytes())
enk.stdin.close(); enk.wait(); dek.terminate()
print('ferdig:', UT, N, 'bilder')
