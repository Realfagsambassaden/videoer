# Manus: Rand- og initialbetingelser

**Tema: Partielle differensialligninger · undertema: Introduksjon til PDE-er (betingelser) · ca. 3 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.1)
**Format:** du på video foran grønnskjerm nede til høyre, tavla bak. Les sitatblokkene (nesten ordrett er greit); **[Du: …]** er ting du gjør, *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md`.

Tre idéer: (1) en PDE har uendelig mange løsninger – betingelser plukker ut den ene, (2) typen og ordenen bestemmer hvilke og hvor mange betingelser (orden i tid = antall initialbetingelser, én randbetingelse i hver ende), (3) tre slags randbetingelser: Dirichlet, Neumann og Robin. Skilt ut fra «Tre typer PDE-er» 20. november 2026.

**Rekvisitter:** slinkyen eller et tau (gitarstreng), gjerne en kopp og et skjerf/en vott (isolasjon).

---

### 0. Kald start: uendelig mange løsninger (0:00–0:35)
*Kartet:* lyser på «betingelser».

> Andreordens PDE-er kommer i tre typer: hyperbolske, parabolske og elliptiske. Men ett problem gjenstår. En PDE har uendelig mange løsninger. For bølgeligningen er f av x minus c t, pluss g av x pluss c t, en løsning *uansett* hvilke funksjoner f og g du velger, så lenge de er to ganger deriverbare.
> Så... hvilken av de uendelig mange løsningene er riktig beskrivelse av akkurat det ingeniørproblemet du forsøker å løse?

**[Du: plukk på slinkyen og la den svinge; trekk på skuldrene ved «uendelig mange»; spør rett i kamera ved «akkurat det ingeniørproblemet».]**
*På skjermen:* Tittel «Rand- og initialbetingelser» (oransje). Tre små ruter med de tre typene (lilla bølge, rød varme, kritt Laplace) glir inn øverst og krymper. Så «u = f(x − ct) + g(x + ct)», der f og g er gule bokser. Formene i boksene byttes raskt (lyd: «brrrt»), og bølgeformene under flimrer forbi. Et stort gult «∞ løsninger». Ved «to ganger deriverbare»: en liten grå lapp «f, g: to ganger deriverbare». Ved «ingeniørproblemet»: et stort gult «?» over en bro eller et rør.

### 1. To klasser betingelser (0:35–1:05)

> Svaret ligger i ekstra betingelser. Vi deler disse i to viktige klasser: *Initialbetingelser* sier hvordan alt er ved start, t lik null. *Randbetingelser* sier hva som skjer på randen, altså kanten. For eksempel at utslaget i endene av gitarstrengen alltid er null.

**[Du: vis «start» med en hånd som slipper noe; vis endene på gitarstrengen med de to hendene (fast i begge ender).]**
*På skjermen:* Et område (grått) med randen tegnet rundt. To merkelapper: «initialbetingelse: hvordan det er ved start, t = 0» (turkis) og «randbetingelse: hva som skjer på kanten» (oransje). Så en gitarstreng mellom to fester, endene oransje: «u = 0 i endene».

### 2. Hvilke og hvor mange? (1:05–2:05)

> Og typen til PDEen bestemmer hva du trenger: Varme og bølger marsjerer fram i tid fra en starttilstand, så de trenger initialbetingelser – i tillegg til randbetingelser. Varmeligningen er av første orden i tid, så den trenger bare starttemperaturen. Bølgeligningen er av andre orden i tid, så den trenger to: både formen og farten på strengen ved start – akkurat som en ball trenger både startposisjon og startfart. Regelen er den samme som for ordinære differensialligninger: Ordenen i tid sier hvor mange initialbetingelser du trenger. Elliptiske ligninger, som Laplace og Poisson, har ingen tid og trenger randbetingelser rundt hele området.
> Det samme gjelder i rommet: Varme- og bølgeligningen er av andre orden i x, så vi trenger én randbetingelse i hver ende av staven – to til sammen.
> Teller vi riktig, får vi nøyaktig én løsning. For få betingelser – og det finnes mange løsninger. For mange – og det finnes kanskje ingen. Et problem med nøyaktig én løsning, som bare endrer seg litt når dataene endres litt, kaller vi *velstilt*.

**[Du: ett finger for varme, to fingre for bølge; ved «ball»: kast en tenkt ball opp; ved «én i hver ende»: én hånd i hver ende; ved «velstilt»: tommel opp.]**
*På skjermen:*
1. Konkret for varme og bølge: en x–t-ramme. Nederste kant lyser turkis «u(x, 0) = f(x)», sidekantene lyser oransje «u(0, t), u(L, t)». En pil glir oppover gjennom ramma: «marsjerer i tid».
2. En liten tabell bygges: «varme: u_t → 1. orden i tid → 1 initialbetingelse: u(x, 0)» · «bølge: u_tt → 2. orden i tid → 2: u(x, 0) og u_t(x, 0)». Ved ballen: en ball i en bue med «startposisjon» og en pil «startfart». Lapp: «orden i tid = antall initialbetingelser».
3. Ved «andre orden i x»: en stav med én oransje prikk i hver ende, «u_xx → én betingelse i hver ende».
4. Konkret for Laplace: en firkant der *hele* randen lyser oransje – «rand rundt hele området».
5. Telleren: «∞» krymper til «1» i grønn boks: «riktige betingelser → én løsning». Til sidene: «for få → mange løsninger» (gult) og «for mange → ingen løsning» (rødt). Stempel: «VELSTILT».

### 3. Tre slags randbetingelser (2:05–2:45)

> Randbetingelser finnes i tre varianter: *Dirichlet* gir verdien på randen. Se for deg en stav som varmes fra én side, og har oppnådd likevekt, så ingenting endrer seg i tid. Det kan f. eks. være et varmeelement i et tørkeskap. Da trenger jeg å vite temperaturen på randa for å kunne løse PDE-en for temperaturfordelingen inne i staven. *Neumann* gir den deriverte på randen, altså strømmen ut – en isolert ende har null varmestrøm. Og *Robin* er en blanding av de to – for eksempel en ende som taper varme til lufta rundt: jo varmere enden er, jo mer varme strømmer ut. Det er Newtons avkjølingslov.

**[Du: vis staven med hendene; ved «isolert»: pakk inn hånda i et skjerf eller en vott; ved Robin: blås på hånda (varme ut i lufta).]**
*På skjermen:* En stav i likevekt, varmet fra venstre (rød → blå), med et lite varmeelement (tørkeskap) til venstre og termometre i begge ender: «Dirichlet: u = verdi på randen» (oransje). Så den høyre enden pakket inn i isolasjon, med en pil for varmestrøm og «0»: «Neumann: u_x = verdi (strømmen ut)». Til slutt en ende med små bølgete piler ut i lufta, og pilene blir større når enden blir varmere: «Robin: −k·u_x = h·(u − u_luft)». De tre merkelappene blir stående side om side.

### 4. Avslutning (2:45–3:10)
*Kartet:* lyser på «betingelser».

> Et eksempel som samler alt: en stav med starttemperatur f av x, hundre grader i venstre ende og isolert høyre ende. Én initialbetingelse, to randbetingelser – og nøyaktig én løsning. Prøv deg på noen oppgaver! Kos dæ – ubetinga!

**[Du: tell én – to – tre på fingrene; pek ned mot oppgavene; blunk ved «ubetinga».]**
*På skjermen:* Staven med de tre betingelsene markert (turkis bunn «u(x, 0) = f(x)», oransje venstre ende «u = 100 °C», isolert høyre ende «u_x = 0»), og temperaturprofilen som utvikler seg i tid mot likevekt. Grønn boks: «1 + 2 betingelser → én løsning». Fysikkhjelp-logoen.

---

**Tall:** Bølgeligningen u_tt = c²·u_xx har d'Alemberts løsning u = f(x − ct) + g(x + ct) for alle to ganger deriverbare f, g. Antall initialbetingelser = orden i tid (varme: u(x, 0); bølge: u(x, 0) og u_t(x, 0)); andre orden i x gir én randbetingelse i hver ende. Randbetingelser: Dirichlet u = g, Neumann ∂u/∂n = g, Robin αu + β∂u/∂n = g (Newtons avkjølingslov: −k·∂u/∂n = h·(u − u_omg)). Velstilt (Hadamard): løsningen finnes, er entydig og avhenger kontinuerlig av dataene. Eksempelet: u_t = α·u_xx på 0 < x < L, u(x, 0) = f(x), u(0, t) = 100 °C, u_x(L, t) = 0 – går mot u = 100 °C overalt.
