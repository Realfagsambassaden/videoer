// Lager YouTube-miniatyrbilde (thumbnail) etter fast mal, fra <videomappe>/thumbnail.json.
//   node _verktoy/thumbnail.js <videomappe>        → <videomappe>/thumbnail.jpg (2560×1440, under 2 MB)
//   npm run thumbnail -- <videomappe>
//
// thumbnail.json (alle stier relativt til videomappa):
// {
//   "emne": "Mekanikk",                 liten håndskrevet merkelapp øverst til venstre (område/emne)
//   "tittel": "POTENSIELL",             stor hvit tittel (1–2 ord; lang tittel blir automatisk mindre)
//   "tittel2": "ENERGI",                valgfri andre linje i samme stil
//   "undertittel": "lagret arbeid",     grønn, lysende (kort!)
//   "person": "person.png",             læreren klippet ut (sett_sammen.py --utklipp), gjennomsiktig PNG
//   "beskjaer_person": [0.25, 0.75],    valgfri: hvilken del av utklippet (andel av bredden) som skal brukes
//   "tegning": "tegning.png",           valgfri: nøkkeltegning eller eksperiment (PNG/SVG, gjennomsiktig) nede til venstre
//   "formel": "E_p = ½kx²"              valgfri: nøkkelformel i håndskrift nede i midten
// }
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const mappe = path.resolve(process.argv[2] || '');
  const cfgFil = path.join(mappe, 'thumbnail.json');
  if (!fs.existsSync(cfgFil)) { console.error('Fant ikke ' + cfgFil); process.exit(1); }
  const c = JSON.parse(fs.readFileSync(cfgFil, 'utf8'));
  const V = path.join(__dirname);                      // _verktoy
  const url = p => 'file://' + path.resolve(mappe, p);
  const font = fs.existsSync(path.join(V, 'ArchitectsDaughter-Regular.ttf')) ? 'ArchitectsDaughter-Regular.ttf' : 'ComicNeue-Bold.ttf';
  const lang = Math.max((c.tittel || '').length, (c.tittel2 || '').length);
  const tSize = lang <= 6 ? 210 : lang <= 9 ? 160 : lang <= 12 ? 125 : 100;
  const [b0, b1] = c.beskjaer_person || [0, 1];
  const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
  @font-face{font-family:Hand;src:url(file://${V}/${font})}
  @font-face{font-family:Mont;font-weight:900;src:url(file://${V}/Montserrat-Black.ttf)}
  html,body{margin:0;width:1280px;height:720px;overflow:hidden;background:#0d1110}
  .a{position:absolute}
  #bg{inset:0;background:url(file://${V}/tavle-bakgrunn.webp) center/cover;opacity:.22}
  #glod{right:-120px;top:40px;width:820px;height:820px;background:radial-gradient(circle,rgba(110,240,74,.28),rgba(110,240,74,0) 65%)}
  #emne{left:40px;top:22px;font:42px Hand;color:#ecefe6}
  #emne:after{content:'';display:block;height:5px;margin-top:4px;background:#6ef04a;border-radius:3px;box-shadow:0 0 10px #6ef04a}
  #tittel{left:30px;top:${c.tittel2 ? 85 : 110}px;font:900 ${tSize}px/0.95 Mont;color:#fff;letter-spacing:-3px;text-shadow:0 6px 18px rgba(0,0,0,.7);max-width:820px}
  #under{left:40px;font:900 ${Math.round(tSize * 0.62)}px/1 Mont;color:#6ef04a;text-shadow:0 0 18px rgba(110,240,74,.85),0 0 40px rgba(110,240,74,.45)}
  #person{right:-10px;bottom:0;height:700px;filter:drop-shadow(0 0 3px #6ef04a) drop-shadow(0 0 16px rgba(110,240,74,.9)) drop-shadow(0 0 36px rgba(110,240,74,.5))}
  #tegning{left:30px;bottom:22px;max-width:520px;max-height:190px}
  #formel{left:40px;bottom:30px;font:58px Hand;color:#ecefe6;text-shadow:0 2px 8px #000;white-space:nowrap}
  #logo{right:22px;bottom:14px;height:96px}
  </style></head><body>
  <div class="a" id="bg"></div><div class="a" id="glod"></div>
  ${c.tegning ? `<img class="a" id="tegning" src="${url(c.tegning)}">` : ''}
  ${c.formel ? `<div class="a" id="formel">${c.formel}</div>` : ''}
  ${c.person ? `<canvas class="a" id="person"></canvas>` : ''}
  <div class="a" id="emne">${c.emne || ''}</div>
  <div class="a" id="tittel">${c.tittel || ''}${c.tittel2 ? '<br>' + c.tittel2 : ''}</div>
  <div class="a" id="under">${c.undertittel || ''}</div>
  <img class="a" id="logo" src="file://${V}/drnormann-logo.svg">
  <script>
  window.klar = (async () => {
    await document.fonts.ready;
    const t = document.getElementById('tittel').getBoundingClientRect();
    const u = document.getElementById('under'); u.style.top = (t.bottom + 6) + 'px';
    const ub = u.getBoundingClientRect().bottom + 12;
    const tg = document.getElementById('tegning'), fo = document.getElementById('formel');
    if (tg) {
      await tg.decode().catch(() => {});
      const plass = 720 - 22 - ub;                       // høyden som er ledig under undertittelen
      if (tg.getBoundingClientRect().height > plass) tg.style.maxHeight = Math.max(80, plass) + 'px';
      if (fo) fo.style.left = (tg.getBoundingClientRect().right + 28) + 'px';
    }
    ${c.person ? `
    const im = new Image(); im.src = ${JSON.stringify(url(c.person))}; await im.decode();
    const sx = im.width * ${b0}, sw = im.width * (${b1} - ${b0});
    // beskjær bort tomme (gjennomsiktige) rader nederst og øverst
    const cv = document.getElementById('person'); cv.width = sw; cv.height = im.height;
    cv.getContext('2d').drawImage(im, sx, 0, sw, im.height, 0, 0, sw, im.height);
    cv.style.width = (700 * sw / im.height) + 'px';` : ''}
    return true;
  })();
  </script></body></html>`;
  const tmp = path.join(mappe, '.thumbnail.html');
  fs.writeFileSync(tmp, html);
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 2 });
  await page.goto('file://' + tmp);
  await page.evaluate(() => window.klar);
  const ut = path.join(mappe, 'thumbnail.jpg');
  await page.screenshot({ path: ut, type: 'jpeg', quality: 88 });
  await browser.close();
  fs.unlinkSync(tmp);
  console.log('Ferdig:', ut, Math.round(fs.statSync(ut).size / 1024) + ' kB');
})();
