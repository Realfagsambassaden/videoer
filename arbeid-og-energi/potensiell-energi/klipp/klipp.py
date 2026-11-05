# Lager det klippede opptaket fra edl.json: python3 klipp.py <kilde> <ut.mkv> [crf]
import json, subprocess, sys, os
ed = json.load(open('edl.json')); kilde, ut = sys.argv[1], sys.argv[2]; crf = sys.argv[3] if len(sys.argv) > 3 else '20'
os.makedirs('biter', exist_ok=True); liste = []
for i, d in enumerate(ed):
    s, e = d['start'], d['slutt']; L = e - s; b = f'biter/b{i:02d}.mkv'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{s:.3f}', '-i', kilde, '-t', f'{L:.3f}', '-vf', 'fps=30',
                    '-af', f'afade=t=in:d=0.012,afade=t=out:st={L-0.015:.3f}:d=0.015', '-c:v', 'libx264', '-crf', crf, '-preset', 'veryfast',
                    '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-ar', '48000', b], check=True)
    liste.append(f"file '{os.path.abspath(b)}'")
open('biter/liste.txt', 'w').write('\n'.join(liste))
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', 'biter/liste.txt', '-c', 'copy', ut], check=True)
