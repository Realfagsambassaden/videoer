# Manus: Endelige differanser

**Tema: Partielle differensialligninger · undertema: Endelige differanser · ca. 3.5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.3)
**Format:** animert Dashman nede til høyre, bare stemmen din. Les sitatblokkene; **[Dashman: …]** og *På skjermen* er for meg.

Tre idéer: (1) en derivert blir en differanse mellom naboverdier, (2) et randverdiproblem blir et lineært ligningssystem, (3) i tid marsjerer vi steg for steg – men tidssteget må ikke være for stort.

---

### 0. Kald start (ca. 6 s)

> En datamaskin kan ikke derivere. Den kan bare legge sammen, trekke fra, gange og dele. Så hvordan i all verden løser den en differensialligning?

**[Dashman: gruble → spm]**
*På skjermen:* En kalkulator med knappene + − × ÷ og et grått «d/dx» som blir strøket over (lyd: «dunk»).

### 1. Derivert → differanse (0:00–1:00)

> Triks nummer én: Vi legger et rutenett med avstand h, og ser bare på verdiene i punktene: U i minus én, U i og U i pluss én.
> Den deriverte er stigningstallet. Det kan vi tilnærme med en sekant: U i pluss én minus U i minus én, delt på to h.
> Og den andrederiverte – krumningen – er hvor mye stigningen *endrer seg*: U i pluss én, minus to U i, pluss U i minus én, delt på h i andre.
> Den siste skal vi bruke hele tiden. Den sier rett og slett: Hvor mye skiller punktet seg fra gjennomsnittet av naboene sine?

**[Dashman: peker_tavla → skrive → lyspaere (ved «gjennomsnittet av naboene»)]**
*På skjermen:* Tittel «Endelige differanser» (oransje). En glatt kurve, så prikker på et rutenett med «h» mellom (pop for hver prikk). Tre prikker lyser: U_{i−1}, U_i, U_{i+1}. En tangent i midtpunktet og en sekant mellom ytterpunktene som nesten faller sammen: «u′ ≈ (U_{i+1} − U_{i−1})/(2h)». Så: «u″ ≈ (U_{i+1} − 2U_i + U_{i−1})/h²» i grønn boks (stablede brøker). Til slutt en liten tegning: midtpunktet sammenlignet med en stiplet linje mellom naboene, avstanden i gult: «avvik fra naboene».

### 2. Randverdiproblem → ligningssystem (1:00–2:00)

> Ta u dobbeltderivert lik minus to på intervallet fra null til én, med u lik null i begge ender. Vi deler i fire, så vi har tre ukjente punkter.
> I hvert punkt bytter vi u dobbeltderivert med differansen. Da får vi tre vanlige ligninger med tre ukjente – og hver ligning inneholder bare et punkt og naboene dets. Matrisen blir tridiagonal.
> Løser vi den, får vi null komma én åtte sju fem, null komma to fem, og null komma én åtte sju fem. Nøyaktig den eksakte løsningen, x ganger én minus x!
> I to dimensjoner er det samme triks, bare med fire naboer: fempunktsformelen. Og blir systemet stort, kan vi løse det iterativt: Hvert punkt oppdaterer seg om og om igjen fra naboene sine, til alt står stille.

**[Dashman: skrive → overrasket (ved «nøyaktig») → peker_opp (ved fire naboer) → noytral_kopp]**
*På skjermen:* Intervallet [0, 1] med to røde randpunkter «u = 0» og tre blå ukjente U₁, U₂, U₃ (h = 0.25). Tre ligninger bygges én og én (pop): «(0 − 2U₁ + U₂)/h² = −2» osv. Matrisen tegnes med tall bare på de tre diagonalene (−2, 1, 1), resten tomme ruter: «tridiagonal». Løsningen dukker opp i punktene og en stiplet parabel x(1 − x) går gjennom alle tre: «eksakt ✓» (pling). Så en 2D-rute med et pluss-formet stensil (−1, −1, 4, −1, −1): «fempunktsformelen». Til slutt et lite varmekart som «roer seg» iterasjon for iterasjon (tikk-lyder) med teksten «Jacobi / Gauss-Seidel».

### 3. Marsjere i tid – og stabilitet (2:00–3:15)

> Varmeligningen har også tid. Da gjør vi det samme i rommet, og så tar vi små skritt fram i tid: Den nye verdien er den gamle, pluss delta t ganger krumningen.
> Men pass på! Forholdet r, delta t delt på h i andre, må være høyst en halv.
> Med r lik null komma fire smelter en varm flekk pent ut. Med r lik null komma seks begynner punktene å hoppe opp og ned – og etter førti steg er tallene oppe i millioner.
> For bølgeligningen bruker vi samme idé to ganger, både i tid og i rom. Det kalles leapfrog-metoden – og den har sin egen grense: c delta t delt på h, høyst én.

**[Dashman: peker_tavla → svette (ved r = 0.6) → hoho_x (ved «millioner») → peker_opp]**
*På skjermen:* En stav i elleve punkter med en varm «firkantbølge» i midten. Grønn boks: «U_i^{n+1} = U_i^n + r(U_{i+1}^n − 2U_i^n + U_{i−1}^n), r = Δt/h²». Gul lapp: «r ≤ ½». To ruter side om side, tikk-lyd for hvert tidssteg: venstre «r = 0.4» – kurven glattes pent ut; høyre «r = 0.6» – kurven blir sagtakket, utslagene vokser, aksen må zoome ut (lyd: alarm), og et tall som ruller opp mot «1 800 000». Til slutt en liten frosk som hopper over et tidsnivå: «leapfrog: U^{n+1} fra U^n og U^{n−1}, cΔt/h ≤ 1».

### 4. Avslutning (3:15–3:30)

> Endelige differanser: deriverte blir differanser, randverdiproblemer blir ligningssystemer, og i tid marsjerer vi – med passe små steg. Prøv deg på noen oppgaver!

**[Dashman: tada]**
*På skjermen:* Tre ikoner: tre prikker med sekant, en tridiagonal matrise, en klokke med «r ≤ ½». Fysikkhjelp-logoen.

---

**Tall (regnet i Python):** u″ = −2, u(0) = u(1) = 0, h = 0.25: U = 0.1875, 0.25, 0.1875 = x(1 − x) i nodene (sentraldifferansen er eksakt for andregradspolynomer). Varmeligningen med h = 0.1, U = 100 i nodene 3–7 og 0 ellers, 40 steg: Δt = 0.004 (r = 0.4) gir maks 18.3; Δt = 0.006 (r = 0.6) gir svingende verdier opp mot 1.8 · 10⁶.
