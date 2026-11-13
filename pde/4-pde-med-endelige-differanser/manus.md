# Manus: Kunsten å løse PDE-er med endelige differanser

**Tema: Partielle differensialligninger · undertema: Endelige differanser · ca. 3.5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.3)
**Format:** du på video foran grønnskjerm nede til høyre, tavla bak. Les sitatblokkene (nesten ordrett er greit); **[Du: …]** er ting du gjør, *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md`.

Tre idéer: (1) et randverdiproblem blir et lineært ligningssystem (tridiagonal matrise), (2) i tid marsjerer vi steg for steg – eksplisitt (direkte, men r ≤ ½ fordi den nye verdien er et vektet gjennomsnitt), (3) implisitt (et ligningssystem per steg, men stabilt).

---

### 0. Start (0:00–0:15)
*Kartet:* lyser på «endelige differanser».

> Med endelige differanser kan vi bytte ut deriverte med differanser mellom naboverdier. Nå skal vi bruke det til å løse differensialligninger. Men da trenger vi i tillegg betingelser.

**[Du: peker på den grønne boksen.]**
*På skjermen:* Tittel «Kunsten å løse PDE-er med endelige differanser» (oransje). Den grønne boksen «u″(x_i) ≈ (U_{i+1} − 2U_i + U_{i−1})/h²» med de tre prikkene under.

### 1. Randverdiproblem → ligningssystem (0:15–1:30)
*Kartet:* lyser på «RVP: ligningssystem».

> La oss se på et randverdiproblem først. En strømledning henger mellom to stolper. Krumningen, u x x, er her tilnærmet konstant – la oss si lik to – og utslaget i endene, altså på randen, er null: u av null lik u av én lik null. Vi deler intervallet i fire, så vi har tre ukjente punkter.
> I hvert punkt bytter vi u x x med differansen. Da får vi tre vanlige ligninger med tre ukjente – og hver ligning inneholder bare et punkt og naboene dets. Matrisen blir tridiagonal.
> Løser vi den, får vi minus null komma én åtte sju fem, minus null komma to fem, og minus null komma én åtte sju fem – ledningen henger ned. Nøyaktig den eksakte løsningen, x ganger x minus én!
> I to dimensjoner er det samme triks, bare med fire naboer: fempunktsformelen. Og blir systemet stort, kan vi løse det iterativt: Hvert punkt oppdaterer seg om og om igjen fra naboene sine, til alt står stille.

**[Du: viser en hengende ledning med hånda (en bue nedover) mellom to «stolper» (de to pekefingrene). Ved «nøyaktig»: løftede øyenbryn. Ved «fire naboer»: fire fingre.]**
*På skjermen:* To stolper med en ledning som henger mellom dem (kritt). Under: intervallet [0, 1] med to oransje randpunkter «u = 0» og tre turkise ukjente U₁, U₂, U₃ (h = 0.25). «u_xx = 2» øverst. Tre ligninger bygges én og én (pop): «(0 − 2U₁ + U₂)/h² = 2», «(U₁ − 2U₂ + U₃)/h² = 2», «(U₂ − 2U₃ + 0)/h² = 2». Matrisen tegnes med tall bare på de tre diagonalene (−2 på diagonalen, 1 ved siden av), resten tomme ruter: «tridiagonal». Løsningen dukker opp i punktene (−0.1875, −0.25, −0.1875), punktene synker ned, og en stiplet parabel x(x − 1) går gjennom alle tre: «eksakt ✓» (pling). Så en 2D-rute med et pluss-formet stensil (−1, −1, 4, −1, −1): «fempunktsformelen». Til slutt et lite varmekart som «roer seg» iterasjon for iterasjon (tikk-lyder) med teksten «Jacobi / Gauss-Seidel».

### 2. Marsjere i tid: eksplisitt og implisitt (1:30–3:10)
*Kartet:* lyser på «tid: eksplisitt · implisitt».

> Varmeligningen, u t lik alfa u x x, har også tid. Da gjør vi det samme i rommet, og så tar vi små skritt fram i tid. Spørsmålet er bare: *Hvilke* verdier bruker vi i krumningen – de vi har *nå*, eller de vi skal finne i *neste* steg?
> Bruker vi verdiene vi har nå, er skjemaet *eksplisitt*. Den nye verdien i hvert punkt regnes ut direkte fra tre kjente naboer: den gamle verdien, pluss alfa delta t ganger krumningen. Ett punkt om gangen – raskt og enkelt.
> Men pass på! Forholdet r, alfa delta t delt på h i andre, må være høyst en halv. *Hvorfor* en halv? Skriv om formelen: Den nye verdien er r ganger venstre nabo, pluss én minus to r ganger seg selv, pluss r ganger høyre nabo – et vektet gjennomsnitt. Så lenge vektene er positive, kan det ikke oppstå nye topper. Men er r større enn en halv, blir vekten på punktet selv negativ: Jo varmere nå, jo kaldere neste gang. Med r lik null komma fire smelter en varm flekk pent ut. Med r lik null komma seks begynner punktene å hoppe opp og ned – og etter førti steg er tallene oppe i millioner.
> Bruker vi i stedet verdiene i *neste* steg, er skjemaet *implisitt*. Da inneholder hver ligning tre *ukjente* naboer, så vi kan ikke regne ut punktene ett og ett. Vi må løse et ligningssystem – akkurat som randverdiproblemet – i hvert eneste tidssteg. Det koster mer, men til gjengjeld er det stabilt uansett hvor store tidssteg vi tar.
> Kort sagt: Eksplisitt er billig per steg, men krever små steg. Implisitt er dyrt per steg, men tåler store steg.

**[Du: ved «nå … eller neste steg»: pek på hånda nede (nå) og så oppe (neste). Ved «vektet gjennomsnitt»: en vektskål med hendene. Ved r = 0.6: hendene hopper opp og ned, større og større. Ved «millioner»: grip deg til hodet. Ved «implisitt»: hendene flettet i hverandre (alt henger sammen). Ved «kort sagt»: én hånd for hver.]**
*På skjermen:* En stav i elleve punkter med en varm «firkantbølge» i midten. Et rutenett med tid oppover: rad n (kjent, hvit) og rad n+1 (ukjent, tom).
- **Eksplisitt:** Tre fylte prikker i rad n, piler som samles i ett tomt punkt i rad n+1 – formet som en pil oppover (lyd: «pling» når punktet fylles). Punktene i rad n+1 fylles ett og ett fra venstre. Grønn boks: «U_i^{n+1} = U_i^n + r(U_{i+1}^n − 2U_i^n + U_{i−1}^n), r = αΔt/h²». Formelen stokkes om med popp: «U_i^{n+1} = r·U_{i−1}^n + (1 − 2r)·U_i^n + r·U_{i+1}^n» – vektene i gult. Tre søyler viser vektene; når r går over ½, krysser den midterste søylen null og blir rød. Gul lapp: «r ≤ ½ ⇔ alle vekter ≥ 0». To ruter side om side, tikk-lyd for hvert tidssteg: venstre «r = 0.4» – kurven glattes pent ut; høyre «r = 0.6» – kurven blir sagtakket, utslagene vokser, aksen må zoome ut (lyd: alarm), og et tall som ruller opp mot «1 800 000».
- **Implisitt:** Én fylt prikk i rad n, og tre tomme punkter i rad n+1 som er bundet sammen med strek – formen snus opp ned. Alle punktene i rad n+1 lenkes sammen i en kjede, og en tridiagonal matrise spretter opp (pop) for hvert tidssteg. Grønn boks: «U_i^{n+1} − r(U_{i+1}^{n+1} − 2U_i^{n+1} + U_{i−1}^{n+1}) = U_i^n». Lapp: «stabil for alle Δt ✓».
- Til slutt en liten tabell: «eksplisitt: billig per steg · krever små steg» og «implisitt: ligningssystem per steg · tåler store steg».

### 3. Avslutning (3:10–3:25)
*Kartet:* lyser på «endelige differanser (hele grenen)».

> Med endelige differanser blir randverdiproblemer til ligningssystemer, og i tid marsjerer vi – eksplisitt med små steg, eller implisitt med et ligningssystem i hvert steg. Prøv deg på noen oppgaver!

**[Du: åpne armer; pek ned mot oppgavene til slutt.]**
*På skjermen:* Tre ikoner: en tridiagonal matrise, og de to tidsstensilene (pil opp og pil ned) side om side. Fysikkhjelp-logoen.

---

**Tall (regnet i Python):** u″ = 2, u(0) = u(1) = 0, h = 0.25: U = −0.1875, −0.25, −0.1875 = x(x − 1) i nodene (sentraldifferansen er eksakt for andregradspolynomer). (En hengende ledning med lite nedheng har u″ = w/T tilnærmet konstant, så formen er en parabel.) Varmeligningen med α = 1, h = 0.1, U = 100 i nodene 3–7 og 0 ellers, 40 steg: Δt = 0.004 (r = 0.4) gir maks 18.3; Δt = 0.006 (r = 0.6) gir svingende verdier opp mot 1.8 · 10⁶.
