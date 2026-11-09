#!/usr/bin/env python3
"""TikTok/Reels/Shorts: «Gjennom jorda» (ArtiFyssik ep. 1, Ken og Ben). 1080×1920, 30 bilder/s.
Kilde: TidGjennomJorda.mp4 (4K, uten tekst), beskåret til stående → kilde.mov. Tider under er i kildetid."""
import json, subprocess
K = 'kilde.mov'; FPS = 30
# (fra, til, fart, zoom, lyd, teksting [(t0,t1,tekst)], stempler [(t,tekst,varighet,stil)])
BITER = [
 (11.25, 14.55, 1.0, 'punch', True, [(11.35, 14.3, 'Hvordan komme seg til Kina gjennom jordkloden?')],
     [(11.3, 'Hoppe GJENNOM jorda? 🌍⬇️', 3.2, 'topp')]),
 (17.85, 25.4, 1.0, 'none', True, [(17.9, 19.9, 'Poenget er: vi bare suger bort all luft.'), (19.95, 22.9, 'Så alle menneskene dør egentlig på grunn av eksperimentet.'),
     (23.0, 25.3, 'Riktig. Det er en antakelse.')], [(21.2, '💀', 1.4, 'emoji'), (23.1, 'Antakelse ✅', 1.9, 'topp')]),
 (26.45, 30.25, 2.0, 'inn', False, [], [(26.6, '🇳🇴 ➡️ 🇨🇳', 3.4, 'topp')]),
 (55.9, 59.95, 1.0, 'punch', True, [(56.02, 57.3, 'Hvilken kraft er det som virker?'), (57.53, 58.9, 'Gravitasjonskraften.'), (58.95, 59.88, 'Halleluja.')],
     [(59.0, '🙏', 1.0, 'emoji')]),
 (62.0, 134.0, 14.4, 'none', False, [], [(62.5, 'Regner … 🧮', 70, 'topp'), (70.0, 'Inni jorda drar tyngden deg mot sentrum', 64, 'forklar'),
     (98.0, '… som en fjær: du svinger fram og tilbake 🔁', 36, 'forklar2')]),
 (135.9, 146.95, 1.0, 'none', True, [(135.95, 137.7, 'Jeg har funnet ut at det tar'), (137.94, 139.5, '5068 sekunder.'), (139.73, 140.95, 'Så vi må dele det på to.'),
     (141.0, 142.9, '2500 sekunder derfra til dit.'), (142.95, 144.3, 'Og i minutter så er jo det …'), (144.35, 145.2, 'Cirka 42.'),
     (145.25, 146.0, 'Alt er 42.'), (146.05, 146.9, 'Alt er rundt 42.')],
     [(144.4, '42 MIN ⏱️', 2.0, 'midt'), (146.0, '🤯', 0.95, 'emoji')]),
 (147.0, 150.25, 1.0, 'punch', True, [(147.06, 150.15, 'Hvis dere fortsatt ikke har skjønt hvor viktig fysikk er …')], []),
]
SLUTTKORT = 2.8
def zoom(z, n):
    return {'punch': "if(lt(on,10),1.28-0.2*on/10,1.08)", 'inn': f"1.0+0.15*on/{n}"}.get(z, "1.0")
ut = 0.0; tekst = []; stempler = []; kutt = []
for i, (a, b, s, z, lyd, tx, st) in enumerate(BITER):
    n = int(round((b - a) / s * FPS)); d = n / FPS
    zp = f"zoompan=z='{zoom(z, n)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS}"
    vf = f"setpts=(PTS-STARTPTS)/{s},fps={FPS},{zp},format=yuv420p"
    if lyd:
        af = (f"atempo={s}," if s != 1 else '') + "highpass=f=90,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,aresample=48000"
        inn = ['-ss', str(a), '-t', str(b - a), '-i', K]; amap = []
    else:
        af = "anull"; inn = ['-ss', str(a), '-t', str(b - a), '-i', K, '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']; amap = ['-map', '0:v', '-map', '1:a']
    af += f",apad,atrim=end={d}"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inn, *amap, '-vf', vf, '-frames:v', str(n), '-af', af, '-ac', '2',
                    '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast', '-c:a', 'pcm_s16le', f'bit{i:02d}.mkv'], check=True)
    f = lambda T: ut + (T - a) / s
    for t0, t1, tt in tx: tekst.append([round(f(t0), 3), round(f(t1), 3), tt])
    for t0, tt, v, stil in st: stempler.append([round(f(t0), 3), round(min(v / s, d - (f(t0) - ut)), 2), tt, stil])
    kutt.append(round(ut, 3)); ut += d
json.dump({'lengde': ut + SLUTTKORT, 'slutt': ut, 'tekst': tekst, 'stempler': stempler, 'kutt': kutt}, open('overlay.json', 'w'), ensure_ascii=False, indent=1)
open('liste.txt', 'w').write(''.join(f"file 'bit{i:02d}.mkv'\n" for i in range(len(BITER))))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'liste.txt', '-c', 'copy', 'grunn.mkv'], check=True)
print('lengde', round(ut + SLUTTKORT, 2), 's, kutt', kutt)
