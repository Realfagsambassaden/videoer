#!/usr/bin/env python3
"""Setter sammen den ferdige videoen: animasjonen (tavla) + læreren fra grønnskjermopptaket nede til høyre,
med lyden fra opptaket.

Bruk:
  python3 _verktoy/sett_sammen.py --anim <mappe>/<mappe>.mp4 --opptak <opptak.mov> --ut <mappe>/<mappe>-ferdig.mp4
  python3 _verktoy/sett_sammen.py ... --stillbilde 42     # bare ett bilde ved 42 s, for å sjekke nøkkelen og plasseringen
  python3 _verktoy/sett_sammen.py --opptak <opptak.mov> --utklipp 42 --ut <mappe>/person.png
                                                       # læreren klippet ut (gjennomsiktig PNG) ved 42 s, til miniatyrbildet

Valg:
  --farge 0x3fae4a   grønnfargen som skal fjernes (standard: måles automatisk i hjørnene av første bilde)
  --likhet 0.10      hvor lik grønnfargen en piksel må være for å fjernes (øk litt, f.eks. 0.13, hvis det blir
                     grønne rester; senk hvis hud eller klær blir gjennomsiktige – sjekk med --stillbilde)
  --blanding 0.03    myk overgang i kanten
  --hoyde 680        hvor høy læreren blir i bildet (piksler av 1080). Sonen er 660 høy; litt over er greit
                     når læreren står nederst og hodet er under y = 420.
  --midt 1610        hvor midten av opptaket havner vannrett (1610 = midt i sonen x 1300–1920).
                     Står læreren ikke midt i opptaket, juster dette eller bruk --beskjaer.
  --forskyv 0        flytt opptaket i tid (sekunder) i forhold til animasjonen, hvis de ikke starter likt
  --beskjaer v:h     skjær bort deler av opptaket (andel av bredden til venstre og høyre), f.eks. 0.25:0.25,
                     hvis grønnskjermen ikke dekker hele bildet

Animasjonen bør være like lang som opptaket (sett scenelengdene i anim.html etter tider.json).
Lyden normaliseres (loudnorm) til YouTube-nivå.
"""
import argparse, subprocess, sys, tempfile
from pathlib import Path


def mal_farge(opptak, tid=0.5):
    """Måler grønnfargen som medianen av pikslene i de fire hjørnene i ett bilde."""
    from PIL import Image
    import statistics
    with tempfile.TemporaryDirectory() as td:
        png = Path(td) / 'f.png'
        subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(tid), '-i', str(opptak), '-frames:v', '1', str(png)], check=True)
        im = Image.open(png).convert('RGB'); w, h = im.size; d = max(8, w // 20)
        px = []
        for (x0, y0) in [(0, 0), (w - d, 0), (0, h - d), (w - d, h - d)]:
            c = im.crop((x0, y0, x0 + d, y0 + d)); px += [c.getpixel((i, j)) for i in range(d) for j in range(d)]
        r, g, b = (int(statistics.median(c)) for c in zip(*px))
    if not (g > r + 20 and g > b + 20):
        print(f'ADVARSEL: hjørnefargen ({r},{g},{b}) ser ikke grønn ut – oppgi --farge selv.', file=sys.stderr)
    return f'0x{r:02x}{g:02x}{b:02x}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--anim')
    ap.add_argument('--opptak', required=True)
    ap.add_argument('--ut', required=True)
    ap.add_argument('--farge')
    ap.add_argument('--likhet', type=float, default=0.10)
    ap.add_argument('--blanding', type=float, default=0.03)
    ap.add_argument('--hoyde', type=int, default=680)
    ap.add_argument('--midt', type=int, default=1610)
    ap.add_argument('--forskyv', type=float, default=0.0)
    ap.add_argument('--beskjaer', default='0:0')
    ap.add_argument('--stillbilde', type=float)
    ap.add_argument('--utklipp', type=float, help='lag gjennomsiktig PNG av læreren ved dette tidspunktet')
    a = ap.parse_args()
    if a.utklipp is None and not a.anim:
        ap.error('--anim trengs (unntatt med --utklipp)')

    farge = a.farge or mal_farge(a.opptak)
    print('Grønnfarge:', farge)
    v, h = (float(x) for x in a.beskjaer.split(':'))
    crop = f'crop=iw*(1-{v}-{h}):ih:iw*{v}:0,' if (v or h) else ''
    person = (f'[1:v]{crop}chromakey={farge}:{a.likhet}:{a.blanding},despill=type=green,'
              f'scale=-2:{a.hoyde},format=yuva420p[p]')
    if a.utklipp is not None:
        f = f'{crop}chromakey={farge}:{a.likhet}:{a.blanding},despill=type=green,format=rgba'
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', str(a.utklipp), '-i', a.opptak, '-frames:v', '1', '-vf', f, a.ut], check=True)
        print('Ferdig:', a.ut); return
    lag = f'{person};[0:v][p]overlay=x={a.midt}-w/2:y=H-h:shortest=0:eof_action=pass[v]'
    inn = ['-i', a.anim]
    if a.forskyv: inn += ['-itsoffset', str(a.forskyv)]
    inn += ['-i', a.opptak]

    if a.stillbilde is not None:
        cmd = ['ffmpeg', '-y', '-v', 'error', '-ss', str(a.stillbilde)] + inn[:2] + ['-ss', str(a.stillbilde)] + inn[2:] + \
              ['-filter_complex', lag, '-map', '[v]', '-frames:v', '1', a.ut]
    else:
        tmp = str(Path(a.ut).with_suffix('.tmp.mp4'))
        cmd = ['ffmpeg', '-y', '-v', 'error', '-stats'] + inn + ['-filter_complex', lag, '-map', '[v]', '-map', '1:a?',
               '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast',
               '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-shortest', tmp]
    print(' '.join(cmd))
    subprocess.run(cmd, check=True)
    if a.stillbilde is None:
        Path(tmp).replace(a.ut)
    print('Ferdig:', a.ut)


if __name__ == '__main__':
    sys.exit(main())
