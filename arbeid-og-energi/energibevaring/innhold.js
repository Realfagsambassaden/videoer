// ---------- Energibevaring: innholdet. Tider i T = tid i klippet til utkast 1 (klipp/edl_utkast1.json, 406.8 s). ----------
// Klippet er endret etterpå (klipp/edl.json, 409.8 s): KLIPP oversetter gammel T → ny T (R), og tilbake (Rinv).
// Tn = tid i det nye klippet. Scener: kald start (0–10.4 s, læreren stor) → tittelkort (1.6 s) → hoved.
const KLIPP = [[0.0,10.36,0.0,10.36],[10.36,15.88,10.36,5.52],[15.88,22.76,15.88,6.88],[22.76,28.28,22.76,5.52],[28.28,31.88,28.28,3.6],[31.88,38.32,31.88,6.44],[38.32,51.16,38.32,12.84],[51.16,55.92,51.16,4.76],[55.92,60.48,55.92,4.56],[60.48,64.56,60.48,4.08],[64.56,68.84,64.56,4.28],[68.84,70.24,68.84,1.4],[70.24,72.24,70.24,2.0],[72.24,74.12,72.24,1.88],[74.12,78.96,74.64,4.84],[78.96,85.28,79.48,6.32],[85.28,88.48,85.8,3.2],[88.48,97.48,89.0,9.0],[97.48,103.88,98.0,6.4],[103.88,105.32,104.4,1.44],[105.32,107.64,105.84,2.32],[107.64,116.24,108.16,8.6],[116.24,129.04,116.76,15.8],[129.04,132.12,132.56,3.08],[132.12,141.28,135.64,9.16],[141.28,146.08,144.8,4.8],[146.08,148.4,149.6,2.32],[148.4,149.68,151.92,1.28],[149.68,150.2,153.2,0.52],[150.2,150.84,153.72,0.64],[150.84,153.32,154.36,2.48],[153.32,160.6,156.84,7.28],[160.6,163.84,164.12,3.24],[163.84,167.2,167.36,3.36],[167.2,172.2,170.72,5.0],[172.2,173.72,175.72,1.52],[173.72,176.64,177.24,2.92],[176.64,180.48,180.16,3.84],[180.48,183.28,184.0,2.8],[183.28,186.28,186.8,3.0],[186.28,187.88,189.8,1.6],[187.88,189.4,191.4,1.52],[189.4,193.6,192.92,4.2],[193.6,194.64,197.12,1.04],[194.64,198.24,198.16,3.6],[198.24,206.24,201.76,8.0],[206.24,208.48,209.76,2.24],[208.48,217.52,212.0,9.04],[217.52,220.56,221.04,3.04],[220.56,221.12,224.08,0.56],[221.12,228.64,224.64,7.52],[228.64,231.0,232.16,2.36],[231.0,236.2,234.52,5.2],[236.2,246.32,239.72,10.12],[246.32,250.36,249.84,4.04],[250.36,253.6,253.88,3.24],[253.6,256.72,257.12,3.12],[256.72,260.56,260.24,3.84],[260.56,267.72,264.08,7.16],[267.72,271.96,271.24,4.24],[271.96,273.84,275.48,1.88],[273.84,279.36,277.36,5.52],[279.36,280.4,282.88,1.04],[280.4,283.48,283.92,3.08],[283.48,284.68,287.0,1.2],[284.68,285.76,288.2,1.08],[285.76,287.12,289.28,1.36],[287.12,287.88,290.64,0.76],[287.88,289.8,291.4,1.92],[289.8,291.16,293.32,1.36],[291.16,292.84,294.68,1.68],[292.84,296.96,296.36,4.12],[296.96,300.16,300.48,3.2],[300.16,301.76,303.68,1.6],[301.76,306.4,305.28,4.64],[306.4,313.04,309.92,6.64],[313.04,318.32,316.56,5.28],[318.32,322.64,321.84,4.32],[322.64,326.36,326.16,3.72],[326.36,327.48,329.88,1.12],[327.48,328.0,331.0,0.52],[328.0,331.56,331.52,3.56],[331.56,334.44,335.08,2.88],[334.44,341.0,337.96,6.56],[341.0,343.2,344.52,2.2],[343.2,352.16,346.72,8.96],[352.16,357.0,355.68,4.84],[357.0,360.96,360.52,3.96],[360.96,364.0,364.48,3.04],[364.0,367.76,367.52,3.76],[367.76,373.88,371.28,6.12],[373.88,380.76,377.4,6.88],[380.76,386.6,384.28,5.32],[386.6,402.96,389.6,16.36],[402.96,406.8,405.96,3.84]];
const R = T => { for (const [a, b, n, l] of KLIPP) if (T < b) return n + Math.min(Math.max(T - a, 0), l); const k = KLIPP[KLIPP.length - 1]; return k[2] + k[3]; };
const Rinv = Tn => { for (const [a, b, n, l] of KLIPP) if (Tn < n + l) return a + Math.min(Math.max(Tn - n, 0), b - a); return 406.8; };
// Utkast 3: biten der læreren presser sammen fjæra (T2 119.68–132.56 i utkast 2-klippet) er kuttet bort: C() og Cinv().
const KUTT0 = 119.68, KUTT1 = 132.56, KL = KUTT1 - KUTT0;
const C = T2 => T2 < KUTT0 ? T2 : T2 < KUTT1 ? KUTT0 : T2 - KL;
const Cinv = T3 => T3 < KUTT0 ? T3 : T3 + KL;
const KALD = 10.4, TITTEL = 1.6, HOVED = 409.8 - KL - KALD;
const MN = Tn => Tn < KALD ? Tn : KALD + TITTEL + (Tn - KALD);   // ny klipp-tid → animasjonstid
const M = T => MN(C(R(T)));                                          // gammel klipp-tid → animasjonstid
const SLUTT = KALD + TITTEL + HOVED;
window.S = [['kald', KALD], ['tittel', TITTEL], ['hoved', HOVED]];
const START = [0, KALD, KALD + TITTEL];
const SEKSJON = [M(38.3), M(72.2), M(116.2), M(197.9), M(236.2), M(326.4), M(386.4)];
const SKAKER = [];
const Tg = G => Rinv(Cinv(G < KALD ? G : G - TITTEL));   // gammel klipp-tid
const Tng = G => G < KALD ? G : G - TITTEL;         // ny klipp-tid
const fs = 'font-size:54px';
const brok = (a, b) => `<span class="brok"><span>${a}</span><span>${b}</span></span>`;
const p2 = '<span class="p">2</span>';
const halv = brok(1, 2);
const rot = x => `<span class="rot"><svg class="rs" viewBox="0 0 10 20" preserveAspectRatio="none"><path d="M0.5 12 L3 10.5 L6 19 L10 0.4" fill="none" stroke="currentColor" stroke-width="3.4" vector-effect="non-scaling-stroke" stroke-linejoin="round" stroke-linecap="round"/></svg><span class="ru">${x}</span></span>`;   // rottegn med strek over hele uttrykket

// søyler (energi) – h: liste av [navn, verdi 0..1, farge]
function soyler(x, y, H, verdier, sum) {
  let h = '';
  verdier.forEach(([navn, v, farge], i) => {
    const xx = x + i * 90, hh = Math.max(0, v) * H;
    h += `<rect x="${xx}" y="${y - hh}" width="60" height="${hh}" fill="${farge}" opacity=".85" rx="4"/>`;
    h += `<text x="${xx + 30}" y="${y + 42}" text-anchor="middle" font-family="Hand" font-size="34" fill="${farge}">${navn}</text>`;
  });
  h += `<path d="M${x - 10} ${y} L${x + verdier.length * 90 - 20} ${y}" stroke="#ecefe6" stroke-width="3"/>`;
  if (sum) h += `<path d="M${x - 10} ${y - H} L${x + verdier.length * 90 - 20} ${y - H}" stroke="#eee462" stroke-width="3" stroke-dasharray="10 8"/><text x="${x + verdier.length * 90 - 10}" y="${y - H + 10}" font-family="Hand" font-size="30" fill="#eee462">E<tspan font-size="20" dy="6">tot</tspan></text>`;
  return h;
}
const Ek = ['E<tspan font-size="22" dy="6">k</tspan>', 0, '#f19c2c'], Ep = ['E<tspan font-size="22" dy="6">p</tspan>', 0, '#56d7b8'];
const ep = v => ['E<tspan font-size="22" dy="6">p</tspan>', v, '#56d7b8'], ek = v => ['E<tspan font-size="22" dy="6">k</tspan>', v, '#f19c2c'];

// halvrør-rampe og Dashman på skateboard (lærerens tegning)
function rampe(cx, cy, r, op = 1) {
  return `<g opacity="${op}"><path d="M${cx - r - 160} ${cy} L${cx - r} ${cy} A${r} ${r} 0 0 0 ${cx + r} ${cy} L${cx + r + 160} ${cy}" stroke="#ecefe6" stroke-width="5" fill="none"/></g>`;
}
function skater(cx, cy, r, th, s = 1) {   // th = vinkel fra bunnen (rad), positiv mot høyre; brettet ligger på rampa
  const x = cx + r * Math.sin(th), y = cy + r * Math.cos(th), rot = -(th + 0.785) * 180 / Math.PI;
  // dash_ned.png (241×192) er tegnet på vei ned venstre side (normal 45° mot høyre); brettets midtpunkt ca. (60,160)
  return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${0.62 * s})"><image href="elementer/dash_ned.png" x="-60" y="-165" width="241" height="192"/></g>`;
}

// --- Kald start: ballen spretter lavere og lavere ---
stempel('?', 1500, 250, 7.0, KALD, -8, 'font-size:220px');
skriv('Hvorfor kommer den ikke helt opp igjen?', 60, 60, 6.9, KALD, 't', 2.4, { css: 'font-size:56px;color:#eee462' });

// --- Tittelkort ---
lag('<img src="thumbnail.jpg" style="width:1920px;height:1080px">', 0, 0, KALD, KALD + TITTEL, 'tittelkort');

// --- A: energien bytter form (T 10.4–38.3) ---
const A0 = M(10.4), A1 = SEKSJON[0];
skriv('ENERGIBEVARING', 90, 60, A0 + 0.1, A1, 'h1', 1.2);
egen(A0, A1, (s, G) => {
  const T = Tg(G);
  // ballen faller med økende fart (y ∝ t²), flere ganger, og blir liggende nederst til slutt.
  // Syklus 1.7 s: 0.3 s stille øverst, 1.0 s fall, 0.4 s nede. Skygger hver 0.1 s viser at den går fortere og fortere.
  const SYK = 1.7, N = 5, t0 = T - 16.2, k = Math.min(Math.floor(Math.max(t0, 0) / SYK), N - 1);
  const tf = t0 < 0 ? 0 : Math.min(t0 - k * SYK - 0.3, 1.0), uu = klemt(tf), yb = 420 + 440 * uu * uu;
  let h = `<path d="M260 860 L700 860" stroke="#ecefe6" stroke-width="4"/>`;
  h += `<path d="M260 390 L700 390" stroke="#9aa49e" stroke-width="2" stroke-dasharray="8 8"/><text x="710" y="400" font-family="Hand" font-size="34" fill="#9aa49e">h</text>`;
  for (let s2 = 0.1; s2 < tf - 0.02; s2 += 0.1) h += `<circle cx="480" cy="${420 + 440 * s2 * s2 - 30}" r="30" fill="none" stroke="#ecefe6" stroke-width="3" opacity=".22"/>`;
  h += `<circle cx="480" cy="${yb - 30}" r="30" fill="none" stroke="#ecefe6" stroke-width="5"/>`;
  if (uu > 0.03) h += pilsvg(545, yb - 30 - 50 * uu, 545, yb - 30 + 50 * uu, '#f19c2c', 5) + `<text x="565" y="${yb - 18}" font-family="Hand" font-size="40" fill="#f19c2c">v</text>`;   // pila midt på ballen
  const f = (yb - 420) / 440;
  h += soyler(820, 840, 380, [ep(1 - f), ek(f)], true);
  s.innerHTML = h;
});
skriv('E<sub>p</sub> = mgh', 90, 200, M(12.3), A1, 'f', 1.0, { css: fs + ';color:#56d7b8' });
skriv('→ E<sub>k</sub> = ' + halv + 'mv' + p2, 90, 290, M(21.3), A1, 'f', 1.4, { css: fs + ';color:#f19c2c' });
skriv('Energien forsvinner ikke –<br>den bare bytter form!', 1010, 170, M(28.3), A1, 't', 2.4, { w: 820 });
skriv('→ dette kaller vi <span style="color:#6ef04a">ENERGIBEVARING</span>', 1010, 310, M(35.8), A1, 't', 1.6);

// --- B: Dashman i rampa (T 38.3–72.2) ---
const B0 = SEKSJON[0], B1 = SEKSJON[1];
const RX = 700, RY = 420, RR = 300;
const thB = T => { if (T < 42.4) return -1.45; const w = 2 * Math.PI / 7.0; return -1.45 * Math.cos(w * (T - 42.4)); };
egen(B0, B1, (s, G) => {
  const T = Tg(G), th = thB(T), hh = 1 - Math.cos(th), h0 = 1 - Math.cos(1.45);
  let h = rampe(RX, RY, RR) + skater(RX, RY, RR - 6, th);
  h += soyler(110, 860, 300, [ep(hh / h0), ek(1 - hh / h0)], true);
  s.innerHTML = h;
});
skriv('Dashman i skaterampa', 90, 60, B0 + 0.2, B1, 'h2', 1.2);
stempel('wiii!', 980, 380, M(53.0), M(55.6), -8, 'font-size:70px');
skriv('E<sub>k</sub> + E<sub>p</sub> = konstant', 420, 830, M(60.6), B1, 'f', 1.6, { css: fs + ';color:#6ef04a' });
skriv('mekanisk energi: &nbsp;E<sub>mek</sub> = E<sub>k</sub> + E<sub>p</sub>', 420, 765, M(62.4), B1, 'tl', 1.4, { css: 'font-size:38px;color:#56d7b8' });
lag('<div style="background:#eee462;color:#0d1110;padding:6px 18px;font:400 36px Hand;transform:rotate(-3deg)">idealisert: ingen friksjon,<br>ingen luftmotstand</div>', 640, 920, M(64.7), B1, 'stempel', { rot: -3 });

// --- C: eksempel, rampa 2.0 m (T 72.2–116.2) ---
const C0 = SEKSJON[1], C1 = SEKSJON[2];
skriv('EKSEMPEL', 90, 60, C0 + 0.2, C1, 'h2', 0.8);
const CX = 1000, CY = 400, CR = 200;
egen(C0, C1, (s, G) => {
  const T = Tg(G);
  let th = -1.5; if (T > 83.0) th = -1.5 + 1.5 * glatt((T - 83.0) / 1.6);
  let h = rampe(CX, CY, CR) + skater(CX, CY, CR - 5, th, 0.85);
  h += `<path d="M${CX - CR - 70} ${CY} L${CX - CR - 70} ${CY + CR}" stroke="#f19c2c" stroke-width="4"/><path d="M${CX - CR - 85} ${CY} l30 0 M${CX - CR - 85} ${CY + CR} l30 0" stroke="#f19c2c" stroke-width="4"/>`;
  h += `<text x="${CX - CR - 190}" y="${CY + CR / 2}" font-family="Hand" font-size="46" fill="#f19c2c">2.0 m</text>`;
  if (T > 105.4) h += `<g opacity="${klemt((T - 105.4) / 0.4)}">` + pilsvg(CX - 40, CY + CR + 40, CX + 140, CY + CR + 40, '#6ef04a', 7) + `<text x="${CX - 10}" y="${CY + CR + 100}" font-family="Hand" font-size="42" fill="#6ef04a">6.3 m/s</text></g>`;
  s.innerHTML = h;
});
skriv('E<sub>p</sub> = mgh', 90, 170, M(76.9), C1, 'f', 1.0, { css: fs + ';color:#56d7b8' });
skriv('E<sub>k</sub> = ' + halv + 'mv' + p2, 90, 250, M(85.4), C1, 'f', 1.2, { css: fs + ';color:#f19c2c' });
skriv('<span style="color:#56d7b8"><span class="stryk tykk">m<i></i></span>gh</span> = <span style="color:#f19c2c">' + halv + '<span class="stryk tykk">m<i></i></span>v' + p2 + '</span>', 90, 360, M(88.5), C1, 'f', 1.6, { css: fs, stryk: M(92.6) });
stempel('hokus pokus!', 330, 440, M(95.5), M(97.6), -6, 'font-size:56px');
skriv('v = ' + rot('2gh'), 90, 470, M(99.6), C1, 'f', 1.2, { css: fs });
skriv('= ' + rot('2 · 9.81 m/s' + p2 + ' · 2.0 m') + ' ≈ 6.3 m/s', 90, 560, M(104.5), C1, 'f', 2.0, { css: 'font-size:40px;color:#6ef04a' });
skriv('Ingen krefter – bare energibevaring!', 90, 680, M(107.7), C1, 't', 2.0, { css: 'color:#eee462' });

// --- D: fjærkraften og fjærkanonen (T 116.2–197.9) ---
const D0 = SEKSJON[2], D1 = SEKSJON[3];
skriv('FJÆRKRAFTEN', 90, 60, D0 + 0.2, D1, 'h2', 1.0);
skriv('Fjærenergi: &nbsp;E<sub>p</sub> = ' + halv + 'kx' + p2, 90, 160, M(124.5), D1, 'f', 1.6, { css: fs + ';color:#56d7b8' });
// fjærkanonen: de to tegningene har like store kanonrør (65.5 × 171 px); skalert likt og plassert så røret står stille
const FKS = 300 / 316, FKX = 836, FKY = 433;                    // fk_hihi: rør x 203–268.5, topp 134
const RORX = FKX + 235.75 * FKS, RORY = FKY + 134 * FKS;          // rørets midtlinje og munning
lag('<img src="elementer/fk_hihi_tom.png" style="width:300px">', FKX, FKY, M(130.4), M(143.2), 'fade');   // lærerens tegning uten den gule fjæra
lag(`<img src="elementer/fk_skudd_tom.png" style="width:${351 * FKS}px">`, RORX - 271.25 * FKS, RORY - 12 * FKS, M(143.2), D1, 'fade');
stempel('PJONG!', 1110, 470, M(143.2), M(144.6), 8, 'font-size:70px');
skriv('k = 200 N/m', 90, 270, M(133.8), D1, 'tl', 0.8);
skriv('x = 5.0 cm', 90, 330, M(140.0), D1, 'tl', 0.8);
skriv('m = 20 g', 90, 390, M(145.2), D1, 'tl', 0.6);
skriv('Hvor høyt? 🤔', 90, 460, M(147.0), D1, 't', 1.0, { css: 'color:#eee462' });
// kula skytes opp og faller ned i kanonen igjen (presser fjæra sammen på nytt), i løkke. Søylene følger kula.
// Fra T = 172.3 («kula på toppen») blir den stående øverst.
const FK0 = 143.4, FKP = 6.675, FKTOPP = 172.3;
function fkTilstand(T) {   // → [y (kula), fjær, Ek, Ep, c (sammenpressing 0–1)]
  const y0 = RORY - 16, hm = 300, ytopp = c => y0 + 95 * c;
  if (T >= FKTOPP) return [y0 - hm, 0, 0, 1, 0];
  if (T < FK0) { const c = glatt((T - 134.0) / 6.0); return [ytopp(c), c * c, 0, 0, c]; }   // Dashman presser fjæra sammen
  const t = (T - FK0) % FKP;
  if (t < 0.15) { const c = 1 - t / 0.15; return [ytopp(c), c * c, 1 - c * c, 0, c]; }       // fjæra skyter kula ut
  if (t < 2.35) { const u = (t - 0.15) / 2.2, ep = 1 - (1 - u) * (1 - u); return [y0 - hm * ep, 0, 1 - ep, ep, 0]; }
  if (t < 4.55) { const w = (t - 2.35) / 2.2, ep = 1 - w * w; return [y0 - hm * ep, 0, 1 - ep, ep, 0]; }
  const c = glatt((t - 4.55) / 0.5); return [ytopp(c), c * c, 1 - c * c, 0, c];               // ned i røret: fjæra presses sammen igjen
}
function fjaer(c) {   // tegnet fjær i kanonrøret, sammenpressing c (0 = avspent, 1 = presset sammen)
  const yb = RORY + 158, yt = RORY + 95 * c, n = 9, w = 21; let d = `M${RORX} ${yb}`;
  for (let i = 1; i <= 2 * n; i++) d += ` L${RORX + (i % 2 ? -w : w)} ${yb - (yb - yt) * i / (2 * n)}`;
  d += ` L${RORX} ${yt}`;
  return `<path d="${d}" stroke="#eee462" stroke-width="4" fill="none" stroke-linejoin="round"/><path d="M${RORX - 24} ${yt} l48 0" stroke="#eee462" stroke-width="5"/>`;
}
egen(M(130.4), D1, (s, G) => {
  const T = Tg(G), [y, fj, ek_, ep_, c] = fkTilstand(T), top = RORY - 16 - 300;
  let h = T >= 143.2 ? `<path d="M${RORX - 60} ${top} l250 0" stroke="#f19c2c" stroke-width="3" stroke-dasharray="8 8"/>` : '';
  if (T > 195.3) h += `<text x="${RORX + 205}" y="${top + 12}" font-family="Hand" font-size="42" fill="#f19c2c">h ≈ 1.3 m</text>`;
  h += fjaer(c) + `<circle cx="${RORX}" cy="${y}" r="16" fill="#0d1110" stroke="#ecefe6" stroke-width="5"/>`;
  if (T > 134.5 && T < 141.5 && c > 0.15) h += `<text x="${RORX + 50}" y="${RORY + 70}" font-family="Hand" font-size="34" fill="#eee462">x</text>` + pilsvg(RORX + 40, RORY + 2, RORX + 40, RORY + 95 * c, '#eee462', 3);
  if (T > 161.3) h += `<g opacity="${klemt((T - 161.3) / 0.4)}">` + soyler(560, 470, 190, [['fjær', fj, '#eee462'], ek(ek_), ep(ep_)], true) + '</g>';
  s.innerHTML = h;
});
stempel('ENERGIBEVARING!', 90, 560, M(183.3), D1, -3, 'font-size:64px;color:#6ef04a');
skriv(halv + 'kx' + p2 + ' = mgh', 90, 650, M(184.4), D1, 'f', 1.4, { css: fs });
skriv('h = ' + brok('kx' + p2, '2mg'), 90, 740, M(189.5), D1, 'f', 1.2, { css: fs });
skriv('= ' + brok('200 N/m · (0.050 m)' + p2, '2 · 0.020 kg · 9.81 m/s' + p2) + ' ≈ 1.3 m', 90, 860, M(194.5), D1, 'f', 2.0, { css: 'font-size:44px;color:#6ef04a' });

// --- E: hvor ble det av energien? (T 197.9–236.2) ---
const E0 = SEKSJON[3], E1 = SEKSJON[4];
skriv('HVOR BLE DET AV ENERGIEN?', 90, 60, E0 + 0.2, E1, 'h2', 1.4);
egen(E0, E1, (s, G) => {   // ballen slippes øverst (når læreren slipper sin) og spretter lavere og lavere
  const T = Tg(G), t = Math.max(0, T - 207.4), H0 = 330, Y = 860 - 30, X = 330;
  let y = Y - H0, hk = 1, tt = t, n = 0, epa = 1; const KR = 0.7;   // epa = andel av den mekaniske energien som er potensiell
  if (T >= 207.4) {
    // første fall fra toppen (halv bue), så sprett med 70 % av energien igjen hver gang
    const d0 = 0.6; if (tt < d0) { const u = tt / d0; y = Y - H0 * (1 - u * u); epa = 1 - u * u; }
    else { tt -= d0; n = 1; hk = KR;
      while (n < 14) { const dur = 1.2 * Math.sqrt(hk); if (tt < dur) { const u = tt / dur, z = 4 * u * (1 - u); y = Y - H0 * hk * z; epa = z; break; } tt -= dur; hk *= KR; n++; }
      if (n >= 14) { y = Y; epa = 0; hk = 0; } }
  }
  let h = `<path d="M120 860 L540 860" stroke="#ecefe6" stroke-width="4"/><path d="M120 ${Y - H0} L540 ${Y - H0}" stroke="#9aa49e" stroke-width="2" stroke-dasharray="8 8"/>`;
  h += `<circle cx="${X}" cy="${y}" r="28" fill="none" stroke="#ecefe6" stroke-width="5"/>`;
  // søyler: mekanisk energi (E_p nederst, E_k oppå), varme, lyd, og summen stablet. Stiplet linje = startenergien.
  const mek = hk, tap = 1 - mek, BX = 620, BY = 880, BH = 320, sub = (b) => `E<tspan font-size="22" dy="6">${b}</tspan><tspan dy="-6"> </tspan>`;
  const rekt = (x, y0, hh, farge) => hh > 0.5 ? `<rect x="${x}" y="${y0 - hh}" width="60" height="${hh}" fill="${farge}" opacity=".85" rx="4"/>` : '';
  const cols = [[BX, [[mek * epa, '#56d7b8'], [mek * (1 - epa), '#f19c2c']]], [BX + 120, [[tap * 0.85, '#e0573d']]], [BX + 200, [[tap * 0.15, '#9aa49e']]],
                [BX + 320, [[mek * epa, '#56d7b8'], [mek * (1 - epa), '#f19c2c'], [tap * 0.85, '#e0573d'], [tap * 0.15, '#9aa49e']]]];
  for (const [x, deler] of cols) { let yy = BY; for (const [v, f] of deler) { h += rekt(x, yy, v * BH, f); yy -= v * BH; } }
  h += `<path d="M${BX - 10} ${BY} L${BX + 390} ${BY}" stroke="#ecefe6" stroke-width="3"/>`;
  h += `<text x="${BX + 30}" y="${BY + 40}" text-anchor="middle" font-family="Hand" font-size="30" fill="#ecefe6"><tspan fill="#56d7b8">${sub('p')}</tspan>+ <tspan fill="#f19c2c">${sub('k')}</tspan></text>`;
  h += `<text x="${BX + 150}" y="${BY + 40}" text-anchor="middle" font-family="Hand" font-size="30" fill="#e0573d">varme</text>`;
  h += `<text x="${BX + 230}" y="${BY + 40}" text-anchor="middle" font-family="Hand" font-size="30" fill="#9aa49e">lyd</text>`;
  h += `<text x="${BX + 350}" y="${BY + 40}" text-anchor="middle" font-family="Hand" font-size="30" fill="#eee462">sum</text>`;
  h += `<path d="M${BX - 10} ${BY - BH} L${BX + 390} ${BY - BH}" stroke="#eee462" stroke-width="3" stroke-dasharray="10 8"/><text x="${BX - 10}" y="${BY - BH - 14}" font-family="Hand" font-size="32" fill="#eee462">startenergi</text>`;
  s.innerHTML = h;
});
skriv('friksjon og luftmotstand …', 90, 170, M(211.9), E1, 't', 1.4);
skriv('Energien er egentlig bevart! 👍', 90, 250, M(222.2), E1, 't', 1.6, { css: 'color:#6ef04a' });
skriv('Den går over til varme, lyd, …', 90, 330, M(225.0), E1, 't', 1.6);
skriv('«energitap»', 90, 410, M(230.0), E1, 't', 0.8, { css: 'color:#eee462' });

// --- F: konservative krefter (T 236.2–326.4) ---
const F0 = SEKSJON[4], F1 = SEKSJON[5];
skriv('Når er energien bevart?', 90, 60, F0 + 0.2, F1, 'h2', 1.2);
skriv('For den spesielt interesserte 🤓', 90, 150, M(246.3), F1, 'tl', 1.2, { css: 'color:#9aa49e' });
skriv('KONSERVATIVE KREFTER', 90, 220, M(258.9), F1, 'f', 1.4, { css: 'font-size:56px;color:#eee462;letter-spacing:.05em' });
lag('', 70, 310, M(260.7), F1, 'boks', { cls: 'boks gronnboks', w: 520, css: 'height:120px;padding:4px 26px' });
skriv('F = −' + brok('dE<sub>p</sub>', 'dx'), 100, 320, M(261.0), F1, 'f', 1.6, { css: 'font-size:62px' });
skriv('(i 3D: <span class="v">F</span> = −<span style="font-family:\'DejaVu Sans\',serif;font-size:.9em">∇</span>E<sub>p</sub>)', 720, 385, M(264.4), F1, 'tl', 1.2, { css: 'color:#b4bdb7;font-size:48px' });
skriv('⇒ energien er bevart', 640, 300, M(269.3), F1, 't', 1.2, { css: 'color:#6ef04a' });
// tyngden
skriv('Tyngden: &nbsp;E<sub>p</sub> = mgh', 90, 490, M(273.9), F1, 't', 1.4, { css: 'color:#56d7b8' });
skriv(brok('dE<sub>p</sub>', 'dh') + ' = mg', 90, 570, M(280.5), F1, 'f', 1.0, { css: 'font-size:48px' });
skriv('F = −mg &nbsp;↓', 380, 580, M(285.9), F1, 'f', 1.0, { css: 'font-size:48px;color:#6ef04a' });
// fjæra
skriv('Fjæra: &nbsp;E<sub>p</sub> = ' + halv + 'kx' + p2, 90, 700, M(300.2), F1, 't', 1.4, { css: 'color:#eee462' });
skriv(brok('dE<sub>p</sub>', 'dx') + ' = kx', 90, 780, M(306.5), F1, 'f', 1.0, { css: 'font-size:48px' });
skriv('F = −kx', 380, 790, M(311.8), F1, 'f', 1.0, { css: 'font-size:48px;color:#6ef04a' });
skriv('Begge er konservative ✓', 640, 880, M(318.4), F1, 't', 1.4, { css: 'color:#6ef04a' });

// --- G: hvorfor er energien bevart? utledningen (T 326.4–386.4) ---
const G0 = SEKSJON[5], G1 = SEKSJON[6];
skriv('Hvorfor?', 90, 60, G0 + 0.2, G1, 'h2', 0.8);
const U1 = M(337.0), U2 = M(341.6);
skriv('W = ∫ <span id="t_F">F</span> dx', 90, 180, M(331.7), U1, 'f', 1.2, { css: fs });
skriv('F = <span id="s_F">−' + brok('dE<sub>p</sub>', 'dx') + '</span>', 1000, 170, M(334.4), G1, 'f', 1.0, { css: 'font-size:48px;color:#56d7b8' });
lag('W = ∫ <span style="color:#56d7b8">−' + brok('dE<sub>p</sub>', '<span class="stryk">dx<i></i></span>') + '</span> <span class="stryk">dx<i></i></span>', 90, 180, U1, G1, 'popp', { css: fs, cls: 'f', stryk: M(341.1) });
fly('−' + brok('dE<sub>p</sub>', 'dx'), '#s_F', '#t_F', M(336.4), 0.6, 'font-size:48px;color:#56d7b8');
skriv('= −∫ dE<sub>p</sub> = −ΔE<sub>p</sub>', 120, 290, M(345.3), G1, 'f', 1.6, { css: fs });
skriv('Arbeid-energi-setningen: &nbsp;W = ΔE<sub>k</sub>', 90, 400, M(349.0), G1, 't', 2.4, { css: 'color:#f19c2c' });
stempel('Holy moly!', 760, 470, M(357.2), M(359.4), -6, 'font-size:64px');
skriv('ΔE<sub>k</sub> = −ΔE<sub>p</sub>', 90, 500, M(358.5), G1, 'f', 1.4, { css: fs });
lag('', 70, 600, M(368.4), G1, 'boks', { cls: 'boks gronnboks', w: 560, css: 'height:110px;padding:4px 26px' });
skriv('ΔE<sub>k</sub> + ΔE<sub>p</sub> = 0', 100, 610, M(368.6), G1, 'f', 1.4, { css: 'font-size:60px' });
skriv('E<sub>mek</sub> = E<sub>k</sub> + E<sub>p</sub> = konstant 🎉', 90, 750, M(375.8), G1, 't', 1.6, { css: 'color:#6ef04a' });
skriv('(den mekaniske energien er bevart)', 90, 825, M(377.2), G1, 'tl', 1.4, { css: 'color:#6ef04a' });
stempel('I am so sorry 🙈', 700, 880, M(383.9), G1, -4, 'font-size:50px');

// --- H: avslutning (T 386.4–406.8) ---
const H0 = SEKSJON[6], H1 = SLUTT;
skriv('ENERGIBEVARING', 90, 60, H0 + 0.2, H1, 'h1', 1.0);
skriv('Energi kan ikke oppstå eller bli borte –<br>bare bytte form.', 90, 190, M(387.3), H1, 't', 2.4, { w: 1000 });
lag('', 70, 360, M(392.6), H1, 'boks', { cls: 'boks gronnboks', w: 960, css: 'height:150px;padding:6px 30px' });
skriv('Konservative krefter (tyngde, fjær):', 100, 370, M(392.8), H1, 'tl', 1.4);
skriv('E<sub>mek</sub> = E<sub>k</sub> + E<sub>p</sub> = konstant', 100, 430, M(399.0), H1, 'f', 1.2, { css: 'color:#6ef04a' });
skriv('Prøv deg på noen oppgaver! ✏️', 90, 600, M(403.6), H1, 't', 1.2);
lag('<img src="../../_verktoy/fh-logo-linje.png" style="height:60px">', 90, 700, M(404.6), H1, 'fade');
egen(H0, H1, (s, G) => { const T = Tg(G), th = -1.2 * Math.cos(2 * Math.PI / 6 * (T - 386)); s.innerHTML = rampe(820, 760, 170, 0.9) + skater(820, 760, 170 - 4, th, 0.6); });
