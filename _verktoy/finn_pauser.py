#!/usr/bin/env python3
"""Finner taleavsnitt og pauser i et opptak, så animasjonen kan legges i takt med det læreren sier.

Bruk:
  python3 _verktoy/finn_pauser.py <opptak.mov> [--pause 0.7] [--terskel -35]

Skriver en tabell over taleavsnitt (start–slutt i sekunder) og pauser lengre enn --pause sekunder,
og lagrer resultatet som tider.json ved siden av opptaket. Pausene mellom manusavsnittene er
de lengste, så de er de naturlige skjøtene mellom scenene i anim.html.
--terskel er lydnivået (dB) som regnes som stillhet; øk mot -30 hvis det er støy i rommet.
"""
import argparse, json, re, subprocess, sys
from pathlib import Path


def varighet(fil):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(fil)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('opptak')
    ap.add_argument('--pause', type=float, default=0.7, help='minste pause i sekunder')
    ap.add_argument('--terskel', type=float, default=-35, help='stillhet under dette nivået (dB)')
    a = ap.parse_args()
    fil = Path(a.opptak)
    T = varighet(fil)
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', str(fil), '-vn',
                        '-af', f'silencedetect=noise={a.terskel}dB:d={a.pause}', '-f', 'null', '-'],
                       capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r.stderr)]
    ends = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r.stderr)]
    pauser = []
    for i, s in enumerate(starts):
        e = ends[i] if i < len(ends) else T
        pauser.append((round(s, 2), round(e, 2)))
    tale, t0 = [], 0.0
    for s, e in pauser:
        if s - t0 > 0.05: tale.append((round(t0, 2), round(s, 2)))
        t0 = e
    if T - t0 > 0.05: tale.append((round(t0, 2), round(T, 2)))

    print(f'Opptak: {fil.name}  ({T:.1f} s)')
    print('Taleavsnitt:')
    for i, (s, e) in enumerate(tale, 1):
        print(f'  {i:2d}. {s:7.2f} – {e:7.2f}  ({e - s:5.1f} s)')
    print(f'Pauser over {a.pause} s (lengste først – sannsynlige sceneskift):')
    for s, e in sorted(pauser, key=lambda p: p[0] - p[1])[:12]:
        print(f'  {s:7.2f} – {e:7.2f}  ({e - s:4.1f} s)')
    ut = fil.with_name(fil.stem + '-tider.json')
    ut.write_text(json.dumps({'opptak': fil.name, 'varighet': T, 'tale': tale, 'pauser': pauser}, indent=1), encoding='utf-8')
    print(f'Lagret: {ut}')


if __name__ == '__main__':
    sys.exit(main())
