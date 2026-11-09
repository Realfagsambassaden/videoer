#!/usr/bin/env python3
"""Felles klippeverktøy for korte videoer (TikTok/Reels/Shorts), 1080×1920, 30 bilder/s.
Bruk: python3 korte/_tiktok/lag.py korte/<slug>   (leser <slug>/klipp.json)
klipp.json: {"kilder": {navn: sti}, "biter": [...], "slutt": 2.8, "ut": "filnavn.mp4"}
bit: {"k": kilde, "fra": s, "til": s, "fart": 1, "zoom": "none|punch|inn|ut|puls", "lyd": true,
      "utsnitt": null (stående kilde) | "boks" (liggende bilde på uskarp bakgrunn) | x (0–1, midten av stående utsnitt av liggende kilde),
      "skala": 1 (ekstra innzoom av utsnittet), "y": 0.5 (vertikal midte ved skala>1),
      "tekst": [[t0, t1, "tekst"]] (kildetid), "stempler": [[t, "tekst", varighet_ut, stil]] (t i kildetid, varighet i sekunder i ferdig video)}
Stiler: topp, midt, emoji, forklar, forklar2. Stempler med FAIL gir trombone, BOING/KRÆSJ/SPLÆSJ gir boing, ellers pop."""
import json, subprocess, sys, os, numpy as np, soundfile as sf
HER = os.path.dirname(os.path.abspath(__file__)); VERKTOY = os.path.join(HER, '..', '..', '_verktoy')
M = sys.argv[1]; C = json.load(open(os.path.join(M, 'klipp.json'))); FPS = 30
os.chdir(M); os.makedirs('tmp', exist_ok=True)
def dims(f):
    o = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height:stream_side_data=rotation', '-of', 'json', f], capture_output=True, text=True).stdout
    s = json.loads(o)['streams'][0]; w, h = s['width'], s['height']
    rot = next((abs(int(float(d['rotation']))) for d in (s.get('side_data_list') or []) if 'rotation' in d), 0)
    return (h, w) if rot in (90, 270) else (w, h)
def zoom(z, n):
    return {'punch': "if(lt(on,10),1.28-0.2*on/10,1.08)", 'inn': f"1.0+0.15*on/{n}", 'ut': f"1.15-0.15*on/{n}",
            'puls': "1.06+0.08*abs(sin(on/30*3.1416*0.45))"}.get(z, "1.0")
ut = 0.0; tekst = []; stempler = []; kutt = []
for i, b in enumerate(C['biter']):
    src = C['kilder'][b['k']]; a, e, s = b['fra'], b['til'], b.get('fart', 1.0)
    n = int(round((e - a) / s * FPS)); d = n / FPS; W, H = dims(src)
    us = b.get('utsnitt'); sk = b.get('skala', 1.0)
    pre = f"setpts=(PTS-STARTPTS)/{s},fps={FPS},"
    zp = f"zoompan=z='{zoom(b.get('zoom','none'), n)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS}"
    if us == 'boks':
        fh = b.get('forhold', W / H); ch2 = int(H / sk) // 2 * 2; cw2 = min(W, int(ch2 * fh)) // 2 * 2; cx = b.get('x', 0.5)
        x0 = int(min(max(cx * W - cw2 / 2, 0), W - cw2)); y0 = int(min(max(b.get('y', 0.5) * H - ch2 / 2, 0), H - ch2))
        fg_h = int(round(1080 * ch2 / cw2 / 2) * 2)
        fc = (f"[0:v]{pre}crop={cw2}:{ch2}:{x0}:{y0},split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.15[bg];"
              f"[b]scale=1080:{fg_h}[fg];[bg][fg]overlay=0:(H-h)/2-80,{zp},format=yuv420p[v]")
    else:
        if us is None:   # stående kilde
            cw, ch = (W, int(W * 16 / 9)) if H / W >= 16 / 9 else (int(H * 9 / 16), H)
            cx = 0.5
        else:
            ch = H; cw = int(H * 9 / 16); cx = us
        cw2, ch2 = int(cw / sk) // 2 * 2, int(ch / sk) // 2 * 2
        x0 = int(min(max(cx * W - cw2 / 2, 0), W - cw2)); y0 = int(min(max(b.get('y', 0.5) * H - ch2 / 2, 0), H - ch2))
        fc = f"[0:v]{pre}crop={cw2}:{ch2}:{x0}:{y0},scale=1080:1920,{zp},format=yuv420p[v]"
    if b.get('lyd', True):
        af = (f"atempo={s}," if s != 1 else '') + "highpass=f=90,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,aresample=48000"
        inn = ['-ss', str(a), '-t', str(e - a), '-i', src]; amap = ['-map', '0:a']
    else:
        af = "anull"; inn = ['-ss', str(a), '-t', str(e - a), '-i', src, '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']; amap = ['-map', '1:a']
    af += f",apad,atrim=end={d}"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inn, '-filter_complex', fc, '-map', '[v]', *amap, '-frames:v', str(n), '-af', af, '-ac', '2', '-ar', '48000',
                    '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast', '-c:a', 'pcm_s16le', f'tmp/bit{i:02d}.mkv'], check=True)
    f = lambda T: ut + (T - a) / s
    for t0, t1, tt in b.get('tekst', []): tekst.append([round(f(t0), 3), round(min(f(t1), ut + d), 3), tt])
    for t0, tt, v, stil in b.get('stempler', []): stempler.append([round(f(t0), 3), round(min(v, ut + d - f(t0)), 2), tt, stil])
    kutt.append(round(ut, 3)); ut += d
L = ut + C.get('slutt', 2.8)
D = {'lengde': L, 'slutt': ut, 'tekst': tekst, 'stempler': stempler, 'kutt': kutt}
json.dump(D, open('overlay.json', 'w'), ensure_ascii=False, indent=1)
open('tmp/liste.txt', 'w').write(''.join(f"file 'bit{i:02d}.mkv'\n" for i in range(len(C['biter']))))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'tmp/liste.txt', '-c', 'copy', 'tmp/grunn.mkv'], check=True)
if '--uten-overlay' in sys.argv: print('lengde', round(L, 2)); sys.exit()
# tekstlaget
subprocess.run(['node', os.path.join(HER, 'rendre.js'), os.path.abspath('overlay.json'), os.path.abspath('tmp/overlay.mov')] + [a for a in sys.argv[2:] if a[0].isdigit()],
               check=True, env={**os.environ, 'NODE_PATH': os.path.join(HER, '..', '..', 'node_modules')})
if any(a[0].isdigit() for a in sys.argv[2:]): sys.exit()
# lyd
sr = 48000
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'tmp/grunn.mkv', '-vn', '-ac', '1', '-ar', '48000', 'tmp/tale.wav'], check=True)
tale, _ = sf.read('tmp/tale.wav', dtype='float32'); lyd = np.zeros(int(L * sr) + sr, np.float32); lyd[:len(tale)] += tale
def les(nm): x, r = sf.read(os.path.join(VERKTOY, 'lyd', nm), dtype='float32'); return x.mean(1) if x.ndim > 1 else x
def legg(x, t, v=1): i = max(0, int(t * sr)); k = min(len(x), len(lyd) - i); lyd[i:i + k] += x[:k] * v
def trombone():
    out = []
    for fq, du in [(311, .38), (293, .38), (277, .38), (262, 1.3)]:
        t = np.arange(int(du * sr)) / sr; vib = 1 + (0.03 * np.sin(2 * np.pi * 6 * t) if du > 1 else 0)
        ph = 2 * np.pi * np.cumsum(fq * vib * (1 - 0.02 * t)) / sr; x = sum(np.sin(k * ph) / k for k in range(1, 8))
        e = np.minimum(1, t / 0.04) * np.minimum(1, (du - t) / 0.12); out.append(np.convolve(x * e, np.ones(6) / 6, 'same'))
    return 0.18 * np.concatenate(out)
svisj, pop, boing = les('svisj.wav'), les('pop.wav'), les('boing.wav')
for k in kutt[1:]: legg(svisj, k - 0.15, .3)
for t0, v, tx, stil in stempler:
    if 'FAIL' in tx: legg(trombone(), t0, 1.0)
    elif any(w in tx for w in ('BOING', 'KRÆSJ', 'SPLÆSJ', 'BOM')): legg(boing, t0, .4)
    elif stil not in ('forklar', 'forklar2') or True: legg(pop, t0, .3)
legg(svisj, ut - 0.1, .4); m = les('outro_musikk.wav'); legg(m[:int(2.9 * sr)], ut, 1.6)
sf.write('tmp/lyd.wav', np.clip(lyd[:int(L * sr)], -1, 1), sr)
UT = C.get('ut', os.path.basename(os.path.abspath('.')) + '_tiktok.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'tmp/grunn.mkv', '-i', 'tmp/overlay.mov', '-i', 'tmp/lyd.wav', '-filter_complex',
                "[0:v]tpad=stop_mode=clone:stop_duration=5[b];[b][1:v]overlay=shortest=1,format=yuv420p[v]", '-map', '[v]', '-map', '2:a',
                '-c:v', 'libx264', '-crf', '19', '-preset', 'medium', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', 'tmp/' + UT], check=True)
print('ferdig', UT, round(L, 2), 's')
