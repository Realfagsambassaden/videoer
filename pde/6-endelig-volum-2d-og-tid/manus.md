# Manus: Endelig volum i 2D og i tid

**Tema: Partielle differensialligninger · undertema: Endelig volum-metoden i 2D og for tidsavhengige problemer · ca. 3.5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.6–3.8)
**Format:** du på video foran grønnskjerm nede til høyre, tavla bak. Les sitatblokkene (nesten ordrett er greit); **[Du: …]** er ting du gjør, *På skjermen* er for meg.
**Grunnlag:** foilene F25–F26.

**Grafisk språk:** se `pde/LESMEG.md` (kartet, faste farger, formler som bygges). Gangen er alltid fra det generelle til det konkrete.

Tre idéer: (1) i 2D får hver celle fire naboer – ellers er alt som før, (2) i tid blir den nye temperaturen et vektet gjennomsnitt av de gamle, (3) vektene må være positive, og randcellene bestemmer hvor stort tidssteget kan være.

---

### 0. Kald start (ca. 6 s)
*Kartet:* lyser på «endelig volum → 2D · tid».

> Hittil har ingenting endret seg i tid. Nå lar vi klokka gå – og ser hva som skjer hvis vi går litt for fort.

**[Dashman: noytral → overrasket]**
*På skjermen:* En klokke som tikker. En rad med celler som skifter fra rødt mot blått – så begynner én celle ytterst å blinke rødt–blått–rødt (lyd: alarm). «?!» spretter inn.

### 1. To dimensjoner: fire naboer (0:00–1:05)
*Kartet:* lyser på «2D».

> I to dimensjoner får hver celle fire naboer: vest, øst, sør og nord. Ligningen er den samme – bare med to ledd til.
> Langs veggene klipper vi koblingene akkurat som i én dimensjon. Og et hjørne ligger inntil *to* vegger, så det får et bidrag fra hver.
> Ta en plate i tre ganger fire celler. Fra vest strømmer det inn varme, sør og øst er isolert, og nord holdes på hundre grader. Løsningen er varmest der varmen kommer inn, to hundre og seksti grader, og kaldest ved den kalde nordveggen.
> Og sjekken: Fire celler tar inn fem hundre watt hver. Nøyaktig to tusen watt går ut gjennom nord. Bevart!

**[Dashman: peker_tavla → peker_opp (ved hjørnet) → noytral_kopp → armer_opp (ved «Bevart!»)]**
*På skjermen:* Tittel «Endelig volum i 2D og i tid» (oransje). Celle P med fire naboer W, E, S, N og fire røde flukspiler (pop × 4). Formelen fra 1D får to nye ledd som flyr inn: «a_P T_P = a_W T_W + a_E T_E + a_S T_S + a_N T_N + S^u». Et 3 × 4-gitter: gule piler inn fra vest «500 kW/m²», grått i sør og øst «isolert», blå nordvegg «100 °C», hjørnet oppe til venstre blinker «to bidrag». Varmekartet fylles celle for celle (blått → rødt) med 260 °C nederst til venstre og 124 °C oppe til høyre. En vekt: «inn 4 · 500 W = 2000 W» = «ut 2000 W» (pling).

### 2. Tid: et vektet gjennomsnitt (1:05–2:10)
*Kartet:* lyser på «tid».

> Med tid integrerer vi også over et lite tidssteg, delta t. Det enkleste er å regne ut fluksene med de temperaturene vi allerede har – et *eksplisitt* skjema. Da står den nye temperaturen alene på venstre side, og hver celle kan regnes ut for seg.
> Del på a P null – og se: Den nye temperaturen er et *vektet gjennomsnitt* av den gamle temperaturen i cellen og temperaturene i naboene.
> Så lenge alle vektene er positive, kan det ikke dukke opp nye topper eller daler. Varmen bare jevner seg ut, steg for steg.

**[Dashman: skrive → lyspaere (ved «vektet gjennomsnitt») → noytral]**
*På skjermen:* Tidsakse t_n → t_{n+1} med «Δt». Grønn boks: «a_P⁰ T_P^{n+1} = a_W T_W^n + a_E T_E^n + (a_P⁰ − a_W − a_E + S_P) T_P^n + S^u», «a_P⁰ = ρcΔV/Δt». Så tre piler inn mot T_P^{n+1} med vektene «a_W/a_P⁰», «a_E/a_P⁰» og «(a_P⁰ − a_W − a_E + S_P)/a_P⁰», og en vektskål. Verdiene marsjerer mot høyre (tikk, tikk, tikk).

### 3. Tidssteget ved randen (2:10–3:15)
*Kartet:* lyser på «tid (stabilitet)».

> Men vekten på cellen selv kan bli *negativ* hvis tidssteget er for stort. Da betyr det: jo varmere nå, jo kaldere neste gang – og så varmere igjen. Det svinger, og det vokser.
> Og se på randcellen! Der er ledningsevnen mot randen dobbel, så summen av koblingene blir én pluss to – tre i stedet for to. Den som er koblet sterkest til omgivelsene, endrer seg raskest – og tåler derfor minst tidssteg. Ta en plate som er to hundre grader, og sett den ene siden plutselig til null. De indre cellene tåler åtte sekunder, men randcellen bare fem komma tre tre.
> Med to sekunder kryper kulda pent innover. Med seks sekunder begynner randcellen å blinke – akkurat der vi sa.
> Vil du slippe denne grensen, kan du bruke et *implisitt* skjema i stedet: Da regnes fluksene med de nye, ukjente temperaturene, og du må løse et ligningssystem i hvert steg – men tidssteget kan være så stort du vil.

**[Dashman: gruble → svette (ved «seks sekunder») → hoho_x → lyspaere (ved «implisitt»)]**
*På skjermen:* Den midterste vekten krymper og blir rød og negativ; en graf som sager opp og ned med økende utslag (lyd: «boing-boing-BOING»). Grønn boks: «a_P⁰ ≥ a_W + a_E − S_P». Fem celler (alle røde, «200 °C»), vestvegg isolert, østveggen blir blå «0 °C» (lyd: «klang»). Tabell: «isolert celle: 16 s · indre celler: 8 s · randcelle: 5.33 s» (den siste i gult). To animasjoner side om side med tikk-lyd: «Δt = 2 s» – fargene glir pent fra rødt til blått fra øst; «Δt = 6 s» – randcellen blinker og grafen får sagtenner (alarm).

### 4. Oppsummering av PDE-delen (3:15–3:35)
*Kartet:* lyser på «hele kartet lyser».

> Så: Varme jevner ut, bølger frakter, Laplace finner likevekt. Endelige differanser bytter deriverte med differanser. Endelig volum skriver bevaringsloven opp for hver celle. Og når tiden går – pass på tidssteget, særlig ved randen. Prøv deg på noen oppgaver!

**[Dashman: tada]**
*På skjermen:* Fire små ikoner fra de fire filmene: tre familier, tre prikker med sekant, en celle med piler, en klokke. Fysikkhjelp-logoen.

---

**Tall (regnet i Python):** 2D-plata: κA/δx = 1000 · (0.1 · 0.01)/0.1 = 10; vest q_V A = 500 000 · 0.1 · 0.01 = 500 W per celle; nordvegg 2κA/δy = 20, S^u = 2000. Løsning (nord øverst): 146.3, 129.7, 124.0 / 205.6, 178.2, 166.2 / 242.3, 211.2, 196.5 / 260.0, 227.8, 212.2 °C. Energibalanse 4 · 500 W = 2000 W. Tidsdelen: κA/δx = 10 · 1/0.004 = 2500, ρcAδx = 10 · 10⁶ · 0.004 = 40 000; grenser: isolert celle 40 000/2500 = 16 s, indre 40 000/5000 = 8 s, randcelle med T = 0: 40 000/7500 = 5.33 s.
