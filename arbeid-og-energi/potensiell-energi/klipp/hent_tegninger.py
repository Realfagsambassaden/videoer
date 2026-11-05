# Henter ut lærerens streker fra PDF-sidene (via pdftocairo-SVG) per element, etter område og farge.
import re, json, xml.etree.ElementTree as ET
NS = '{http://www.w3.org/2000/svg}'
def mat(t):
    M = [1, 0, 0, 1, 0, 0]
    for f, args in re.findall(r'(matrix|translate|scale)\(([^)]*)\)', t or ''):
        v = [float(x) for x in re.split(r'[ ,]+', args.strip())]
        if f == 'translate': m = [1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0]
        elif f == 'scale': m = [v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0]
        else: m = v
        M = mul(M, m)
    return M
def mul(a, b):
    return [a[0]*b[0]+a[2]*b[1], a[1]*b[0]+a[3]*b[1], a[0]*b[2]+a[2]*b[3], a[1]*b[2]+a[3]*b[3], a[0]*b[4]+a[2]*b[5]+a[4], a[1]*b[4]+a[3]*b[5]+a[5]]
def les(p):
    rot = ET.parse(f'svg/s{p}.svg').getroot(); ut = []
    ider = {e.get('id'): e for e in rot.iter() if e.get('id')}
    def gaa(el, M, arv, maskert, inn=False):
        tag = el.tag.replace(NS, '')
        if tag in ('mask', 'clipPath', 'symbol', 'filter') and not inn: return
        if tag == 'defs':   # pdftocairo legger lag med gjennomsiktighet her som «compositing-group»
            for c in el:
                if (c.get('id') or '').startswith('compositing-group'):
                    t = c.attrib.pop('transform', None); gaa(c, M, arv, True, True)
                    if t: c.set('transform', t)
            return
        if tag == 'use':
            ref = (el.get('{http://www.w3.org/1999/xlink}href') or el.get('href') or '')[1:]
            if ref in ider:
                M2 = mul(M, mat(el.get('transform'))); M2 = mul(M2, [1, 0, 0, 1, float(el.get('x', 0)), float(el.get('y', 0))])
                gaa(ider[ref], M2, arv, maskert, True)
            return
        M2 = mul(M, mat(el.get('transform')))
        arv2 = dict(arv); 
        for k in ('fill', 'stroke', 'stroke-width', 'fill-opacity', 'stroke-opacity', 'opacity'):
            if el.get(k) is not None: arv2[k] = el.get(k)
        if tag == 'path' and el.get('d'):
            d = el.get('d'); tall = [float(x) for x in re.findall(r'-?\d+\.?\d*(?:e-?\d+)?', d)]
            pts = [(M2[0]*x+M2[2]*y+M2[4], M2[1]*x+M2[3]*y+M2[5]) for x, y in zip(tall[0::2], tall[1::2])]
            if not pts: return
            xs, ys = [q[0] for q in pts], [q[1] for q in pts]
            st = arv2.get('stroke'); fi = arv2.get('fill', 'black')
            fyll = (st in (None, 'none')) and fi != 'none'
            col = fi if fyll else st
            a = ' '.join(f'{k}="{v}"' for k, v in el.attrib.items() if k not in ('d', 'transform'))
            for k in ('fill', 'stroke', 'stroke-width', 'fill-opacity'):
                if k in arv2 and k not in el.attrib: a += f' {k}="{arv2[k]}"'
            a += f' transform="matrix({",".join(f"{v:.5f}" for v in M2)})" d="{d}"'
            if fyll and maskert: a += ' fill-opacity="0.55"'
            ut.append({'a': a, 'bb': [min(xs), min(ys), max(xs), max(ys)], 'col': col, 'fyll': fyll, 'op': float(arv2.get('fill-opacity', 1)) if fyll else 1})
        for c in el: gaa(c, M2, arv2, maskert or el.get('mask') is not None, inn and tag not in ('mask',))
    gaa(rot, [1, 0, 0, 1, 0, 0], {}, False)
    sett = set(); unik = []
    for e in ut:
        d = e['a'].split(' d="')[1]
        if d in sett: continue
        sett.add(d); unik.append(e)
    return unik
HVIT = 'rgb(98.823547%, 98.823547%, 98.823547%)'
def velg(p, x0, y0, x1, y1, hvit=False):
    ut = []
    for e in les(p):
        cx, cy = (e['bb'][0] + e['bb'][2]) / 2, (e['bb'][1] + e['bb'][3]) / 2
        w, h = e['bb'][2] - e['bb'][0], e['bb'][3] - e['bb'][1]
        if not (x0 <= cx <= x1 and y0 <= cy <= y1): continue
        if w > 600 or h > 380: continue
        if e['col'] == HVIT and not hvit: continue
        if e['op'] < 0.5: continue
        ut.append(e)
    return ut
def svg(navn, elementer, x0, y0, x1, y1):
    deler = []
    for e in elementer:
        a = e['a']
        if not e['fyll']: a = 'pathLength="1" ' + a
        deler.append(f'<path class="{"f" if e["fyll"] else "s"}" {a}/>')
    return f'<svg class="tegn" id="{navn}" viewBox="{x0} {y0} {x1-x0} {y1-y0}" data-w="{x1-x0}" data-h="{y1-y0}">' + ''.join(deler) + '</svg>'
EL = {
  'fjaer':   (2, 450, 30, 652, 205, False),
  'graf1':   (2, 262, 95, 432, 268, False),
  'pilbue':  (2, 335, 168, 400, 215, True),
  'baller':  (7, 410, 45, 640, 300, True),
  'bakke':   (7, 445, 305, 640, 330, True),
  'graf2':   (7, 265, 160, 460, 335, False),
  'dash1':   (6, 55, 50, 145, 195, True),
  'dash2':   (6, 280, 22, 482, 170, True),
  'dash3':   (6, 375, 228, 592, 392, True),
}
if __name__ == '__main__':
    html = []
    for n, (p, x0, y0, x1, y1, hv) in EL.items():
        e = velg(p, x0, y0, x1, y1, hvit=hv); print(n, len(e))
        html.append(svg(n, e, x0, y0, x1, y1))
    open('elementer.html', 'w').write('\n'.join(html))
