#!/usr/bin/env python3
"""Limer innhold.js inn i anim.html (mellom «Energibevaring: innholdet» og «tegning av et bilde»). Bruk: python3 bygg.py"""
from pathlib import Path
H = Path(__file__).resolve().parent
a = (H / 'anim.html').read_text().split('\n'); inn = (H / 'innhold.js').read_text().rstrip('\n').split('\n')
i = next(k for k, l in enumerate(a) if l.startswith('// ---------- Energibevaring: innholdet'))
j = next(k for k, l in enumerate(a) if l.startswith('// ---------- tegning av et bilde'))
(H / 'anim.html').write_text('\n'.join(a[:i] + inn + [''] + a[j:]))
print('anim.html bygd')
