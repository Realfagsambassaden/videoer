#!/usr/bin/env python3
"""Lager anim.html fra anim.mal.html ved å sette inn lærerens tegninger fra elementer/*.svg som <template>."""
from pathlib import Path
H = Path(__file__).resolve().parent
mal = (H / 'anim.mal.html').read_text(encoding='utf-8')
t = ''.join(f'<template id="svg-{f.stem}">{f.read_text(encoding="utf-8")}</template>\n' for f in sorted((H / 'elementer').glob('*.svg')))
(H / 'anim.html').write_text(mal.replace('<!--SVG-->', t), encoding='utf-8')
print('anim.html laget')
