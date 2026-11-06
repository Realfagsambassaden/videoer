#!/usr/bin/env python3
"""TikTok/Reels/Shorts: «Kopp opp ned» (luft holder colaen i glasset). 1080×1920, 30 bilder/s.
Lager bitene (zoom/fart), tekstlaget (overlay.json → overlay.html rendres med Playwright) og lyden."""
import json, subprocess, numpy as np, soundfile as sf
A, B = '5884.mov', '5885.mov'
# (kilde, fra, til, fart, zoom, teksting [(t0, t1, tekst, hvem)] i kildetid, stempler [(t, tekst, varighet, stil)] i kildetid)
BITER = [
 (B, 31.0, 35.2, 1.0, 'punch', [], [(31.1, 'KÅFFER DET?! 🤯', 4.0, 'topp')]),
 (A, 0.3, 3.8, 1.0, 'punch', [(0.4, 3.1, 'Visste du at luft faktisk kan holde opp vann?'), (3.15, 3.75, 'Nei.')], []),
 (A, 19.4, 20.9, 1.0, 'punch', [(19.45, 20.1, 'Eller cola?'), (20.2, 20.85, 'Nei.')], [(19.5, '🥤', 1.4, 'emoji')]),
 (A, 22.2, 25.0, 1.0, 'none', [(22.25, 23.5, 'Da kan jeg vise deg.'), (23.6, 24.95, 'Jeg har nemlig et glass her.')], []),
 (A, 53.6, 58.3, 1.0, 'inn', [(53.7, 54.6, 'Sånn ja, bra.'), (55.0, 56.6, 'Hva tror du skjer nå?')], [(56.8, '🤔', 1.4, 'emoji')]),
 (A, 63.5, 68.6, 1.0, 'inn', [], [(64.6, 'FAIL 😩', 1.6, 'midt'), (66.2, 'For mye kullsyre! 🫧', 2.4, 'topp')]),
 (B, 0.0, 5.4, 1.0, 'punch', [(0.05, 2.9, 'Det var litt for mye bobler i den brusen, så vi må få det ut.'), (3.6, 5.3, 'Rister på den, så åpner jeg.')], [(0.1, 'Prøve på nytt! 🔁', 2.6, 'topp')]),
 (B, 22.0, 31.0, 1.0, 'none', [(22.05, 25.0, 'Så nå skal jeg lære deg litt fysikk her.'), (25.1, 26.2, 'Ok, Bjørn.'), (26.5, 28.3, 'Ja vel, Gaupe.')], [(26.6, '🐻', 1.6, 'emoji'), (28.0, '🐆', 1.4, 'emoji')]),
 (B, 33.0, 41.2, 1.0, 'puls', [], [(33.2, '🤯🤯🤯', 1.6, 'emoji'), (35.0, 'Lufta presser tallerkenen OPP ⬆️💨', 6.0, 'forklar'), (37.4, '… mye hardere enn colaen presser NED ⬇️', 3.8, 'forklar2')]),
 (B, 44.4, 49.6, 1.0, 'puls', [], [(48.7, 'SPLÆSJ! 💦', 1.0, 'midt')]),
 (B, 52.4, 56.6, 1.0, 'punch', [(52.5, 54.2, 'Mer på fysikkhjelp.no'), (54.3, 56.4, 'Mindre på kjemihjelp.no 😜')], []),
]
SLUTTKORT = 3.0
FPS = 30

def zoomuttrykk(z, n):
    # z = zoomfaktor som funksjon av utbilde 'on' (0..n-1)
    if z == 'punch': return "if(lt(on,10),1.28-0.2*on/10,1.08)"
    if z == 'inn': return f"1.0+0.18*on/{n}"
    if z == 'puls': return "1.06+0.08*abs(sin(on/30*3.1416*0.45))"
    return "1.0"

ut_t = 0.0; plan = []; tekst = []; stempler = []; kutt = []
for i, (src, a, b, s, z, tx, st) in enumerate(BITER):
    d = (b - a) / s; n = int(round(d * FPS))
    zp = f"zoompan=z='{zoomuttrykk(z, n)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS}"
    vf = f"setpts=(PTS-STARTPTS)/{s},fps={FPS},scale=1080:1920,{zp},format=yuv420p"
    af = f"atempo={s}," if s != 1 else ''
    af += "highpass=f=90,afftdn=nf=-28,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,aresample=48000"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a), '-t', str(b - a), '-i', src, '-vf', vf, '-frames:v', str(n),
                    '-af', af, '-ac', '2', '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast', '-c:a', 'pcm_s16le', f'bit{i:02d}.mkv'], check=True)
    f = lambda T: ut_t + (T - a) / s
    for t0, t1, tt in tx: tekst.append([round(f(t0), 3), round(f(t1), 3), tt])
    for t0, tt, v, stil in st: stempler.append([round(f(t0), 3), round(v, 2), tt, stil])
    kutt.append(round(ut_t, 3)); ut_t += n / FPS
LENGDE = ut_t + SLUTTKORT
json.dump({'lengde': LENGDE, 'slutt': ut_t, 'tekst': tekst, 'stempler': stempler, 'kutt': kutt}, open('overlay.json', 'w'), ensure_ascii=False, indent=1)
open('liste.txt', 'w').write(''.join(f"file 'bit{i:02d}.mkv'\n" for i in range(len(BITER))))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'liste.txt', '-c', 'copy', 'grunn.mkv'], check=True)
print('lengde', round(LENGDE, 2), 's, kutt', kutt)
