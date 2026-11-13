# Manus: Endelige differanser

**Tema: Partielle differensialligninger · undertema: Endelige differanser · ca. 3 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.3)
**Format:** du på video foran grønnskjerm nede til høyre, tavla bak. Les sitatblokkene (nesten ordrett er greit); **[Du: …]** er ting du gjør, *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md` (kartet, faste farger, formler som bygges). Gangen er alltid fra det generelle til det konkrete.

Tre idéer: (1) numerikk: gi avkall på eksakthet, men ha kontroll på feilen, (2) diskretisering: et rutenett med avstand h, verdiene U_i, (3) den deriverte blir en differanse – og sentraldifferansen er best, fordi feilene på hver side veier hverandre opp. Bruken (randverdiproblem, marsjere i tid) er i neste film i rekka, `pde/4-pde-med-endelige-differanser`.

---

### 0. Kald start (ca. 0:00–0:50)
*Kartet:* lyser på «numerisk metode → endelige differanser».

> En datamaskin kan ikke derivere. Den kan bare legge sammen, trekke fra, gange og dele. Så hvordan i all verden løser den en differensialligning?

**[Du: kikker mistenksomt på en kalkulator (eller mobilen) i hånda.]**
*På skjermen:* En kalkulator med knappene + − × ÷ og et grått «d/dx» som blir strøket over (lyd: «dunk»).

> Vel, vi kan lære datamaskinen regler, sånn at den kan løse ting symbolsk, uten egentlig å forstå hva den holder på med (litt som studentene mine). Det er et viktig og mye brukt verktøy – biblioteket SymPy i Python er for eksempel god på sånt. Men noen ganger er det vanskelig, eller til og med umulig, å løse PDE-er eksakt, uansett hvor mange triks og regler du har i puggeboka di. Og da finnes det en annen metode, som vi skal se på her: NUMERIKK!

**[Du: ta-da-armer ved «NUMERIKK!».]**
*På skjermen:* Ved «regler»: en liten SymPy-linje som skrives fram, «integrate(x**2) → x**3/3» (grønn hake). Ved «umulig»: en stor, rotete PDE med et rødt «?». Ved «NUMERIKK!»: ordet spretter inn i oransje med stjerner rundt (pop + ta-da-lyd).

> Numerikk handler om å gi avkall på eksakte svar, og til gjengjeld faktisk finne løsninger. Derfor er det også viktig å ha kontroll på hvor stor feilen kan bli. Spesielt sårbart er det når vi deler på veldig små tall – slik som i definisjonen av den deriverte. Der deler vi jo på uendelig små størrelser. Hvordan håndterer vi sånt i en datamaskin, der alt må være endelig? Jo, la meg vise deg.

**[Du: holder tommel og pekefinger nesten sammen ved «veldig små tall».]**
*På skjermen:* En vekt: «eksakt» på den ene siden, «en løsning + kontroll på feilen» på den andre – vekta tipper over. Så definisjonen av den deriverte: «u′(x) = lim_{h→0} (u(x + h) − u(x))/h», der «h → 0» lyser rødt og en liten lapp sier «datamaskinen: ?».

### 1. Diskretisere (0:50–1:20)
*Kartet:* lyser på «endelige differanser».

> Punkt én: Vi må være litt diskré! Altså *diskretisere* problemet vårt. Det gjør vi ved å legge et rutenett med avstand h, og bare se på verdiene i punktene på rutenettet. Verdien av u i punktet x i kaller vi bare U i. U i minus én er da verdien i punktet til venstre for x i, og U i pluss én verdien ett steg til høyre.

**[Du: blunker til kamera ved «diskré». Viser avstanden h mellom to fingre.]**
*På skjermen:* Tittel «Endelige differanser» (oransje). En glatt kurve u(x). Et rutenett med lik avstand «h» legges under (stiplede loddlinjer, pop for hver). Kurven blir til prikker på loddlinjene, og selve kurven tones ned til grått. Tre prikker lyser turkis og får navn: «U_{i−1}», «U_i», «U_{i+1}» over «x_{i−1}», «x_i», «x_{i+1}». Lapp: «U_i = u(x_i)».

### 2. Derivert → differanse (1:20–2:50)
*Kartet:* lyser på «endelige differanser».

> Punkt to: I definisjonen av den deriverte dropper vi rett og slett grensen der h går mot null. I stedet lar vi bare h være liten. Da tilnærmer vi den deriverte med stigningstallet til sekanten gjennom to punkter. Det er ikke helt riktig, men blir h liten nok, blir feilen liten. Bruker vi punktet til høyre, kalles formelen *framoverdifferanse*. Tilsvarende kaller vi det *bakoverdifferanse* om vi bruker sekanten gjennom x i og punktet til venstre. Men en mye bedre tilnærming til den deriverte i x i får vi faktisk ved å bruke sekanten gjennom de to naboene, x i minus én og x i pluss én. Det kaller vi *sentraldifferanse*, og formelen ser sånn ut.

**[Du: viser helningen med flat hånd – litt for bratt, litt for slak, og så midt imellom.]**
*På skjermen:* Definisjonen fra kald start kommer tilbake; «lim_{h→0}» strykes over (rød strek) og blir til «≈». På kurven med prikkene: tangenten i x_i (stiplet, kritt). Så tre sekanter etter tur, hver med sin formel som bygges ved siden av:
- **framover** (oransje sekant gjennom U_i og U_{i+1}): «u′(x_i) ≈ (U_{i+1} − U_i)/h»
- **bakover** (lilla sekant gjennom U_{i−1} og U_i): «u′(x_i) ≈ (U_i − U_{i−1})/h»
- **sentral** (grønn sekant gjennom U_{i−1} og U_{i+1}): «u′(x_i) ≈ (U_{i+1} − U_{i−1})/(2h)» – den grønne sekanten flytter seg parallelt inn til x_i og legger seg nesten oppå tangenten. Grønn boks.

> La oss teste. Ta u lik x i andre. Den deriverte i x lik én er nøyaktig to. Med h lik null komma én gir framoverdifferansen to komma én – litt for bratt. Bakoverdifferansen gir én komma ni – litt for slak. Og sentraldifferansen gir nøyaktig to! Feilen til høyre og feilen til venstre veier hverandre opp.
> Og det blir bedre jo mindre h er. Tar vi sinus x og gjør h ti ganger mindre, blir feilen i framoverdifferansen ti ganger mindre. Men feilen i sentraldifferansen blir *hundre* ganger mindre!

**[Du: teller på fingrene ved de tre tallene; viser «ti» og så «hundre» med hendene langt fra hverandre.]**
*På skjermen:*
1. Parabelen u = x² med tangenten i x = 1 (stigning 2). En liten tabell bygges rad for rad (pop): «framover 2.1 · bakover 1.9 · sentral 2.0 ✓» – 2.1 i oransje med pil «for bratt», 1.9 i lilla med pil «for slak», 2.0 i grønt med hake. Lapp: «feilene veier hverandre opp».
2. En tabell for u = sin x i x = 1 (eksakt cos 1 ≈ 0.540302), feilen for h = 0.1 og h = 0.01:
   - framover: 4.3·10⁻² → 4.2·10⁻³ (pil: «÷ 10»)
   - sentral: 9.0·10⁻⁴ → 9.0·10⁻⁶ (pil: «÷ 100», grønn)
   Lapp: «framover: feil ∝ h · sentral: feil ∝ h²».

> Bruker vi sentraldifferansen to ganger, får vi også den andrederiverte: U i pluss én, minus to U i, pluss U i minus én, delt på h i andre. Den måler hvor mye et punkt avviker fra gjennomsnittet av naboene sine.
> Alright – vi har altså diskretisert, og tilnærmet de deriverte med endelige differanser. Det kan vi bruke til å løse differensialligninger.

**[Du: peker på den grønne boksen; avslutt med et lite nikk.]**
*På skjermen:* «u″(x_i) ≈ (U_{i+1} − 2U_i + U_{i−1})/h²» i grønn boks (stablede brøker). En liten tegning: midtpunktet U_i sammenlignet med en stiplet linje mellom naboene; avstanden i gult: «avvik fra gjennomsnittet av naboene». Til slutt de to grønne boksene (u′ og u″) side om side og Fysikkhjelp-logoen.

---

**Tall (regnet i Python):** u = x² i x = 1, h = 0.1: framover (1.21 − 1)/0.1 = 2.1, bakover (1 − 0.81)/0.1 = 1.9, sentral (1.21 − 0.81)/0.2 = 2.0 (sentraldifferansen er eksakt for andregradspolynomer). u = sin x i x = 1, eksakt cos 1 = 0.540302: h = 0.1 gir framover 0.497364 (feil 4.29·10⁻²), bakover 0.581441 (4.11·10⁻²), sentral 0.539402 (9.00·10⁻⁴); h = 0.01 gir framover 0.536086 (4.22·10⁻³), bakover 0.544501 (4.20·10⁻³), sentral 0.540293 (9.00·10⁻⁶). u″-formelen: (U_{i+1} − 2U_i + U_{i−1})/h² = (2/h²)·((U_{i+1} + U_{i−1})/2 − U_i).
