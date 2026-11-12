# Manus: Endelige differanser

**Tema: Partielle differensialligninger · undertema: Endelige differanser · ca. 4 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.3)
**Format:** animert Dashman nede til høyre, bare stemmen din. Les sitatblokkene; **[Dashman: …]** og *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md` (kartet, faste farger, formler som bygges). Gangen er alltid fra det generelle til det konkrete.

Tre idéer: (1) en derivert blir en differanse mellom naboverdier, (2) et randverdiproblem blir et lineært ligningssystem, (3) i tid marsjerer vi steg for steg – eksplisitt (direkte, men med små steg) eller implisitt (et ligningssystem per steg, men stabilt).

---

### 0. Kald start (ca. 6 s)
*Kartet:* lyser på «numerisk metode → endelige differanser».

> En datamaskin kan ikke derivere. Den kan bare legge sammen, trekke fra, gange og dele. Så hvordan i all verden løser den en differensialligning?

**[Dashman: gruble → spm]**
*På skjermen:* En kalkulator med knappene + − × ÷ og et grått «d/dx» som blir strøket over (lyd: «dunk»).

### 1. Derivert → differanse (0:00–1:00)
*Kartet:* lyser på «endelige differanser».

> Triks nummer én: Vi legger et rutenett med avstand h, og ser bare på verdiene i punktene: U i minus én, U i og U i pluss én.
> Den deriverte er stigningstallet. Det kan vi tilnærme med en sekant: U i pluss én minus U i minus én, delt på to h.
> Og den andrederiverte – krumningen – er hvor mye stigningen *endrer seg*: U i pluss én, minus to U i, pluss U i minus én, delt på h i andre.
> Den siste skal vi bruke hele tiden. Den sier rett og slett: Hvor mye skiller punktet seg fra gjennomsnittet av naboene sine?

**[Dashman: peker_tavla → skrive → lyspaere (ved «gjennomsnittet av naboene»)]**
*På skjermen:* Tittel «Endelige differanser» (oransje). En glatt kurve, så prikker på et rutenett med «h» mellom (pop for hver prikk). Tre prikker lyser: U_{i−1}, U_i, U_{i+1}. En tangent i midtpunktet og en sekant mellom ytterpunktene som nesten faller sammen: «u′ ≈ (U_{i+1} − U_{i−1})/(2h)». Så: «u″ ≈ (U_{i+1} − 2U_i + U_{i−1})/h²» i grønn boks (stablede brøker). Til slutt en liten tegning: midtpunktet sammenlignet med en stiplet linje mellom naboene, avstanden i gult: «avvik fra naboene».

### 2. Randverdiproblem → ligningssystem (1:00–2:00)
*Kartet:* lyser på «RVP: ligningssystem».

> Ta u dobbeltderivert lik minus to på intervallet fra null til én, med u lik null i begge ender. Vi deler i fire, så vi har tre ukjente punkter.
> I hvert punkt bytter vi u dobbeltderivert med differansen. Da får vi tre vanlige ligninger med tre ukjente – og hver ligning inneholder bare et punkt og naboene dets. Matrisen blir tridiagonal.
> Løser vi den, får vi null komma én åtte sju fem, null komma to fem, og null komma én åtte sju fem. Nøyaktig den eksakte løsningen, x ganger én minus x!
> I to dimensjoner er det samme triks, bare med fire naboer: fempunktsformelen. Og blir systemet stort, kan vi løse det iterativt: Hvert punkt oppdaterer seg om og om igjen fra naboene sine, til alt står stille.

**[Dashman: skrive → overrasket (ved «nøyaktig») → peker_opp (ved fire naboer) → noytral_kopp]**
*På skjermen:* Intervallet [0, 1] med to røde randpunkter «u = 0» og tre blå ukjente U₁, U₂, U₃ (h = 0.25). Tre ligninger bygges én og én (pop): «(0 − 2U₁ + U₂)/h² = −2» osv. Matrisen tegnes med tall bare på de tre diagonalene (−2, 1, 1), resten tomme ruter: «tridiagonal». Løsningen dukker opp i punktene og en stiplet parabel x(1 − x) går gjennom alle tre: «eksakt ✓» (pling). Så en 2D-rute med et pluss-formet stensil (−1, −1, 4, −1, −1): «fempunktsformelen». Til slutt et lite varmekart som «roer seg» iterasjon for iterasjon (tikk-lyder) med teksten «Jacobi / Gauss-Seidel».

### 3. Marsjere i tid: eksplisitt og implisitt (2:00–3:40)
*Kartet:* lyser på «tid: eksplisitt · implisitt».

> Varmeligningen, u t lik alfa u x x, har også tid. Da gjør vi det samme i rommet, og så tar vi små skritt fram i tid. Spørsmålet er bare: *Hvilke* verdier bruker vi i krumningen – de vi har *nå*, eller de vi skal finne i *neste* steg?
> Bruker vi verdiene vi har nå, er skjemaet *eksplisitt*. Den nye verdien i hvert punkt regnes ut direkte fra tre kjente naboer: den gamle verdien, pluss alfa delta t ganger krumningen. Ett punkt om gangen – raskt og enkelt.
> Men pass på! Forholdet r, alfa delta t delt på h i andre, må være høyst en halv. Med r lik null komma fire smelter en varm flekk pent ut. Med r lik null komma seks begynner punktene å hoppe opp og ned – og etter førti steg er tallene oppe i millioner.
> Bruker vi i stedet verdiene i *neste* steg, er skjemaet *implisitt*. Da inneholder hver ligning tre *ukjente* naboer, så vi kan ikke regne ut punktene ett og ett. Vi må løse et ligningssystem – akkurat som randverdiproblemet – i hvert eneste tidssteg. Det koster mer, men til gjengjeld er det stabilt uansett hvor store tidssteg vi tar.
> Kort sagt: Eksplisitt er billig per steg, men krever små steg. Implisitt er dyrt per steg, men tåler store steg.

**[Dashman: peker_tavla → spm (ved «hvilke verdier») → svette (ved r = 0.6) → hoho_x (ved «millioner») → lyspaere (ved «implisitt») → skuldre (ved «koster mer») → noytral_kopp]**
*På skjermen:* En stav i elleve punkter med en varm «firkantbølge» i midten. Et rutenett med tid oppover: rad n (kjent, hvit) og rad n+1 (ukjent, tom).
- **Eksplisitt:** Tre fylte prikker i rad n, piler som samles i ett tomt punkt i rad n+1 – formet som en pil oppover (lyd: «pling» når punktet fylles). Punktene i rad n+1 fylles ett og ett fra venstre. Grønn boks: «U_i^{n+1} = U_i^n + r(U_{i+1}^n − 2U_i^n + U_{i−1}^n), r = αΔt/h²». Gul lapp: «r ≤ ½». To ruter side om side, tikk-lyd for hvert tidssteg: venstre «r = 0.4» – kurven glattes pent ut; høyre «r = 0.6» – kurven blir sagtakket, utslagene vokser, aksen må zoome ut (lyd: alarm), og et tall som ruller opp mot «1 800 000».
- **Implisitt:** Én fylt prikk i rad n, og tre tomme punkter i rad n+1 som er bundet sammen med strek – formen snus opp ned. Alle punktene i rad n+1 lenkes sammen i en kjede, og en tridiagonal matrise spretter opp (pop) for hvert tidssteg. Grønn boks: «U_i^{n+1} − r(U_{i+1}^{n+1} − 2U_i^{n+1} + U_{i−1}^{n+1}) = U_i^n». Lapp: «stabil for alle Δt ✓».
- Til slutt en liten tabell: «eksplisitt: billig per steg · krever små steg» og «implisitt: ligningssystem per steg · tåler store steg».

### 4. Avslutning (3:40–3:55)
*Kartet:* lyser på «endelige differanser (hele grenen)».

> Endelige differanser: deriverte blir differanser, randverdiproblemer blir ligningssystemer, og i tid marsjerer vi – eksplisitt med små steg, eller implisitt med et ligningssystem i hvert steg. Prøv deg på noen oppgaver!

**[Dashman: tada]**
*På skjermen:* Tre ikoner: tre prikker med sekant, en tridiagonal matrise, og de to tidsstensilene (pil opp og pil ned) side om side. Fysikkhjelp-logoen.

---

**Tall (regnet i Python):** u″ = −2, u(0) = u(1) = 0, h = 0.25: U = 0.1875, 0.25, 0.1875 = x(1 − x) i nodene (sentraldifferansen er eksakt for andregradspolynomer). Varmeligningen med α = 1, h = 0.1, U = 100 i nodene 3–7 og 0 ellers, 40 steg: Δt = 0.004 (r = 0.4) gir maks 18.3; Δt = 0.006 (r = 0.6) gir svingende verdier opp mot 1.8 · 10⁶.
