// ---------- Energibevaring: innholdet. Tider i T = tid i det klippede opptaket (klipp/edl.json, 406.8 s). ----------
// Scener: kald start (opptaket 0–10.4 s, læreren stor) → tittelkort (1.6 s) → hoved (opptaket fra 10.4 s).
const KALD = 10.4, TITTEL = 1.6, HOVED = 406.8 - KALD;
const M = T => T < KALD ? T : KALD + TITTEL + (T - KALD);
const SLUTT = KALD + TITTEL + HOVED;
window.S = [['kald', KALD], ['tittel', TITTEL], ['hoved', HOVED]];
const START = [0, KALD, KALD + TITTEL];
const SEKSJON = [M(38.3), M(72.2), M(116.2), M(197.9), M(236.2), M(326.4), M(386.4)];
const SKAKER = [];
const Tg = G => G < KALD ? G : G - TITTEL;   // tid i klippet
const fs = 'font-size:54px';
const brok = (a, b) => `<span class="brok"><span>${a}</span><span>${b}</span></span>`;
const p2 = '<span class="p">2</span>';
const halv = brok(1, 2);

// søyler (energi) – h: liste av [navn, verdi 0..1, farge]
function soyler(x, y, H, verdier, sum) {
  let h = '';
  verdier.forEach(([navn, v, farge], i) => {
    const xx = x + i * 90, hh = Math.max(0, v) * H;
    h += `<rect x="${xx}" y="${y - hh}" width="60" height="${hh}" fill="${farge}" opacity=".85" rx="4"/>`;
    h += `<text x="${xx + 30}" y="${y + 42}" text-anchor="middle" font-family="Hand" font-size="34" fill="${farge}">${navn}</text>`;
  });
  h += `<path d="M${x - 10} ${y} L${x + verdier.length * 90 - 20} ${y}" stroke="#ecefe6" stroke-width="3"/>`;
  if (sum) h += `<path d="M${x - 10} ${y - H} L${x + verdier.length * 90 - 20} ${y - H}" stroke="#eee462" stroke-width="3" stroke-dasharray="10 8"/><text x="${x + verdier.length * 90 - 10}" y="${y - H + 10}" font-family="Hand" font-size="30" fill="#eee462">sum</text>`;
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
  const u = glatt((T - 16.2) / 10.2), yb = lerp(420, 860, u * u);   // ballen faller sakte (sakte film)
  let h = `<path d="M260 860 L700 860" stroke="#ecefe6" stroke-width="4"/>`;
  h += `<path d="M260 390 L700 390" stroke="#9aa49e" stroke-width="2" stroke-dasharray="8 8"/><text x="710" y="400" font-family="Hand" font-size="34" fill="#9aa49e">h</text>`;
  h += `<circle cx="480" cy="${yb - 30}" r="30" fill="none" stroke="#ecefe6" stroke-width="5"/>`;
  if (u > 0.05 && u < 1) h += `<path d="M480 ${yb - 80} l0 -${60 * u}" stroke="#ecefe6" stroke-width="3" opacity=".6"/>`;
  const f = (yb - 420) / 440;
  h += soyler(820, 840, 380, [ep(1 - f), ek(f)], T > 28.2);
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
  h += soyler(110, 860, 300, [ep(hh / h0), ek(1 - hh / h0)], T > 60.4);
  s.innerHTML = h;
});
skriv('Dashman i skaterampa', 90, 60, B0 + 0.2, B1, 'h2', 1.2);
stempel('wiii!', 980, 380, M(53.0), M(55.6), -8, 'font-size:70px');
skriv('E<sub>k</sub> + E<sub>p</sub> = konstant', 420, 830, M(60.6), B1, 'f', 1.6, { css: fs + ';color:#6ef04a' });
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
skriv('<span class="stryk">m<i></i></span>gh = ' + halv + '<span class="stryk">m<i></i></span>v' + p2, 90, 360, M(88.5), C1, 'f', 1.6, { css: fs, stryk: M(92.6) });
stempel('hokus pokus!', 330, 440, M(95.5), M(97.6), -6, 'font-size:56px');
skriv('v = √(2gh)', 90, 470, M(99.6), C1, 'f', 1.2, { css: fs });
skriv('= √(2 · 9.81 m/s' + p2 + ' · 2.0 m) ≈ 6.3 m/s', 90, 560, M(104.5), C1, 'f', 2.0, { css: 'font-size:40px;color:#6ef04a' });
skriv('Ingen krefter – bare energibevaring!', 90, 680, M(107.7), C1, 't', 2.0, { css: 'color:#eee462' });

// --- D: fjærkraften og fjærkanonen (T 116.2–197.9) ---
const D0 = SEKSJON[2], D1 = SEKSJON[3];
skriv('FJÆRKRAFTEN', 90, 60, D0 + 0.2, D1, 'h2', 1.0);
skriv('Fjærenergi: &nbsp;E<sub>p</sub> = ' + halv + 'kx' + p2, 90, 160, M(124.5), D1, 'f', 1.6, { css: fs + ';color:#56d7b8' });
lag('<img src="elementer/fk_hihi.png" style="width:300px">', 520, 470, M(130.4), M(143.2), 'fade');
stempel('HIHI!', 540, 420, M(131.0), M(133.0), -6, 'font-size:56px');
lag('<img src="elementer/fk_skudd.png" style="width:330px">', 500, 500, M(143.2), M(182.6), 'fade');
stempel('PJONG!', 780, 420, M(143.2), M(144.6), 8, 'font-size:70px');
skriv('k = 200 N/m', 90, 270, M(133.8), D1, 'tl', 0.8);
skriv('x = 5.0 cm', 90, 330, M(140.0), D1, 'tl', 0.8);
skriv('m = 20 g', 90, 390, M(145.2), D1, 'tl', 0.6);
skriv('Hvor høyt? 🤔', 90, 460, M(147.0), D1, 't', 1.0, { css: 'color:#eee462' });
egen(M(143.2), D1, (s, G) => {   // kula skytes opp og faller ned igjen; søyler fjær → E_p
  const T = Tg(G), t = (T - 143.4) % 6, y0 = 520, hmax = 330;
  const u = t / 2.2, y = t < 2.2 ? y0 - hmax * (1 - (1 - u) * (1 - u)) : y0 - hmax * Math.max(0, 1 - Math.pow((t - 2.2) / 2.2, 2));
  let h = `<path d="M${790} ${y0 - hmax} l220 0" stroke="#f19c2c" stroke-width="3" stroke-dasharray="8 8"/>`;
  if (T > 195.3) h += `<text x="1040" y="${y0 - hmax + 12}" font-family="Hand" font-size="42" fill="#f19c2c">h ≈ 1.3 m</text>`;
  h += `<circle cx="${767}" cy="${y}" r="16" fill="none" stroke="#ecefe6" stroke-width="5"/>`;
  if (T > 161.3) { const k = glatt((T - 163.0) / 10); h += soyler(900, 900, 260, [['fjær', 1 - k, '#eee462'], ep(k)], true); }
  s.innerHTML = h;
});
skriv('Energibevaring: &nbsp;' + halv + 'kx' + p2 + ' = mgh', 90, 560, M(183.3), D1, 'f', 2.0, { css: fs });
skriv('h = ' + brok('kx' + p2, '2mg'), 90, 660, M(189.5), D1, 'f', 1.2, { css: fs });
skriv('= ' + brok('200 N/m · (0.050 m)' + p2, '2 · 0.020 kg · 9.81 m/s' + p2) + ' ≈ 1.3 m', 90, 780, M(194.5), D1, 'f', 2.0, { css: 'font-size:46px;color:#6ef04a' });

// --- E: hvor ble det av energien? (T 197.9–236.2) ---
const E0 = SEKSJON[3], E1 = SEKSJON[4];
skriv('HVOR BLE DET AV ENERGIEN?', 90, 60, E0 + 0.2, E1, 'h2', 1.4);
egen(E0, E1, (s, G) => {   // ballen spretter lavere og lavere, en bit går over til varme/lyd
  const T = Tg(G), t = Math.max(0, T - 205.0);
  let y = 860, hk = 1, tt = t, n = 0; const H0 = 360;
  while (n < 8) { const dur = 1.2 * Math.sqrt(hk); if (tt < dur) { const u = tt / dur; y = 860 - 30 - H0 * hk * 4 * u * (1 - u); break; } tt -= dur; hk *= 0.6; n++; }
  let h = `<path d="M150 860 L700 860" stroke="#ecefe6" stroke-width="4"/><path d="M150 ${860 - 30 - H0} L700 ${860 - 30 - H0}" stroke="#9aa49e" stroke-width="2" stroke-dasharray="8 8"/>`;
  h += `<circle cx="420" cy="${y}" r="28" fill="none" stroke="#ecefe6" stroke-width="5"/>`;
  const tap = T < 205 ? 0 : 1 - Math.pow(0.6, Math.min(n, 6));
  h += soyler(780, 880, 330, [['mek.', 1 - tap, '#56d7b8'], ['varme', tap * 0.85, '#e0573d'], ['lyd', tap * 0.15, '#9aa49e']], T > 222.2);
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
skriv('(i 3D: F⃗ = −∇E<sub>p</sub>)', 640, 400, M(264.4), F1, 'tl', 1.2, { css: 'color:#9aa49e;font-size:34px' });
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
skriv('E<sub>k</sub> + E<sub>p</sub> = konstant – bevart! 🎉', 90, 760, M(375.8), G1, 't', 2.0, { css: 'color:#6ef04a' });
stempel('I am so sorry 🙈', 700, 880, M(383.9), G1, -4, 'font-size:50px');

// --- H: avslutning (T 386.4–406.8) ---
const H0 = SEKSJON[6], H1 = SLUTT;
skriv('ENERGIBEVARING', 90, 60, H0 + 0.2, H1, 'h1', 1.0);
skriv('Energi kan ikke oppstå eller bli borte –<br>bare bytte form.', 90, 190, M(387.3), H1, 't', 2.4, { w: 1000 });
lag('', 70, 360, M(392.6), H1, 'boks', { cls: 'boks gronnboks', w: 960, css: 'height:150px;padding:6px 30px' });
skriv('Konservative krefter (tyngde, fjær):', 100, 370, M(392.8), H1, 'tl', 1.4);
skriv('E<sub>k</sub> + E<sub>p</sub> = konstant', 100, 430, M(399.0), H1, 'f', 1.2, { css: 'color:#6ef04a' });
skriv('Prøv deg på noen oppgaver! ✏️', 90, 600, M(403.6), H1, 't', 1.2);
lag('<img src="../../_verktoy/fh-logo-linje.png" style="height:60px">', 90, 700, M(404.6), H1, 'fade');
egen(H0, H1, (s, G) => { const T = Tg(G), th = -1.2 * Math.cos(2 * Math.PI / 6 * (T - 386)); s.innerHTML = rampe(820, 760, 170, 0.9) + skater(820, 760, 170 - 4, th, 0.6); });
