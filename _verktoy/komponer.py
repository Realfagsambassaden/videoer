#!/usr/bin/env python3
"""Setter læreren (grønnskjerm) inn i animasjonen med en mykere nøkkel enn ffmpeg-chromakey, som tåler at
grønnfargen varierer over bildet. Lager bare bildet (uten lyd).

Bruk: python3 komponer.py --anim anim.mp4 --opptak klippet.mkv --ut bilde.mp4 --plan plan.json
plan.json: liste med {"fra": G0, "til": G1, "opptak": T0, "hoyde": 680, "midt": 1660}  (G = tid i animasjonen,
T0 = tid i opptaket ved G0). Utenfor planen vises bare animasjonen."""
import argparse, json, subprocess, numpy as np

def nokkel(rgb, t0=18, t1=48):
    r, g, b = rgb[..., 0].astype(np.int16), rgb[..., 1].astype(np.int16), rgb[..., 2].astype(np.int16)
    m = np.maximum(r, b); gronn = g - m
    a = 1 - np.clip((gronn - t0) / (t1 - t0), 0, 1)          # 1 = læreren, 0 = grønnskjerm
    g2 = np.minimum(g, m + 6)                                   # fjern grønt skjær i kantene
    ut = np.stack([r, g2, b], -1).clip(0, 255).astype(np.uint8)
    return ut, a.astype(np.float32)

def skaler(img, h):
    from PIL import Image
    H, W = img.shape[:2]; w = round(W * h / H)
    return np.asarray(Image.fromarray(img).resize((w, h), Image.BILINEAR))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--anim'); ap.add_argument('--opptak'); ap.add_argument('--ut'); ap.add_argument('--plan')
    ap.add_argument('--crf', default='18'); a = ap.parse_args()
    plan = json.load(open(a.plan)); fps = 30
    W, H = 1920, 1080
    anim = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', a.anim, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    opp = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', a.opptak, '-vf', 'fps=30', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    ow, oh = map(int, subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', a.opptak], capture_output=True, text=True).stdout.strip().split(','))
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                           '-c:v', 'libx264', '-crf', a.crf, '-preset', 'veryfast', '-pix_fmt', 'yuv420p', a.ut], stdin=subprocess.PIPE)
    opp_i = 0; siste = None; n = 0
    def les_opp(til):
        nonlocal opp_i, siste
        while opp_i <= til:
            b = opp.stdout.read(ow * oh * 3)
            if len(b) < ow * oh * 3: return siste
            siste = np.frombuffer(b, np.uint8).reshape(oh, ow, 3); opp_i += 1
        return siste
    while True:
        b = anim.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        bilde = np.frombuffer(b, np.uint8).reshape(H, W, 3).copy(); G = n / fps
        for p in plan:
            if p['fra'] <= G < p['til']:
                ramme = les_opp(round((p['opptak'] + G - p['fra']) * fps))
                if ramme is None: break
                rgb, al = nokkel(ramme)
                h = p['hoyde']; rgb = skaler(rgb, h); al = skaler((al * 255).astype(np.uint8), h).astype(np.float32) / 255
                w = rgb.shape[1]; x0 = round(p['midt'] - w / 2); y0 = H - h
                xa, xb = max(0, x0), min(W, x0 + w); ya, yb = max(0, y0), min(H, y0 + h)
                rs = rgb[ya - y0:yb - y0, xa - x0:xb - x0]; als = al[ya - y0:yb - y0, xa - x0:xb - x0, None]
                bit = bilde[ya:yb, xa:xb].astype(np.float32)
                bilde[ya:yb, xa:xb] = (bit * (1 - als) + rs * als).astype(np.uint8)
                break
        enc.stdin.write(bilde.tobytes()); n += 1
        if n % 900 == 0: print(f'{n / fps:.0f} s', flush=True)
    enc.stdin.close(); enc.wait(); print('ferdig', n, 'bilder')

if __name__ == '__main__':
    main()
