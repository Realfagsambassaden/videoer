# Manus: Endelig volum-metoden 4 – tidsavhengige problemer

**Tema: Numeriske metoder for PDE-er · undertema: Endelig volum-metoden (4 av 4) · ca. 4.5 min**
**Brukes på:** (ingen side ennå – IMAA3012/IMAx3012, kompendiet §3.7)
**Grunnlag:** foilene F26_EVM_Tidsavhengig og forelesningsplanen F23–F26.

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** en stoppeklokke eller mobilen med stoppeklokke, og gjerne en grytelapp.

**Tavla:** svart tavle. En plate i fem celler som avkjøles over tid, med en klokke som tikker (lyd: tikk) for hvert tidssteg. Temperaturen vises både som farge i cellene og som en graf over plata.

---

### 0. Kald start (ca. 8 s)

> **[Du:** start stoppeklokka og hold den opp.**]**
> Hittil har ingenting endret seg i tid. Nå skal vi la tiden gå … og se hva som skjer hvis vi går litt for fort.

*På skjermen:* En klokke som tikker. Fem celler som skifter fra rødt mot blått – og så plutselig begynner én celle å blinke rødt–blått–rødt (lyd: alarm, kort). «?!» spretter inn.

### 1. Integrer over rom og tid (0:00–0:50)

> Varmeligningen har nå et tidsledd: rho c ganger den tidsderiverte. Vi integrerer derfor ikke bare over cellen, men også over et tidssteg, delta t.
> Tidsleddet blir enkelt: rho c ganger cellevolumet, ganger endringen i T P fra ett tidssteg til det neste.
> Men fluksene? Når i tidssteget skal vi regne dem ut? Det enkleste er å bruke de verdiene vi allerede kjenner – ved starten av tidssteget. Det kalles et *eksplisitt* skjema.

*På skjermen:* Tittel «Tidsavhengige problemer» (oransje). «ρc ∂T/∂t = ∂/∂x(κ ∂T/∂x) + S». En tidsakse t_n → t_{n+1} med «Δt» under en celle, så integralet «∫∫ … dV dt». Tidsleddet flyr ut: «ρcAδx (T_P^{n+1} − T_P^n)». Fluksene får et lite stempel «ved t_n (kjent)».

### 2. Det eksplisitte skjemaet (0:50–1:35)

> Samler vi leddene, står den nye temperaturen alene på venstre side, og alt på høyre side er kjent. Og a W, a E, S u og S P er nøyaktig de samme som i det stasjonære problemet.
> Så vi bare marsjerer fram i tid: steg for steg, regner vi ut de nye verdiene fra de gamle.
> På matriseform: den nye vektoren er den gamle, pluss delta t over rho c delta V, ganger F minus L T. Det er den samme matrisen L og høyresiden F som vi allerede har laget.

*På skjermen:* Grønn boks: «a_P⁰ T_P^{n+1} = a_W T_W^n + a_E T_E^n + (a_P⁰ − a_W − a_E + S_P) T_P^n + S^u», med «a_P⁰ = ρcAδx/Δt». Lapp «samme a-er som før ✓». Klokka tikker og verdiene «marsjerer» mot høyre (tikk, tikk, tikk). Matriseform flyr inn: «T^{n+1} = T^n + Δt/(ρcΔV) · (F − L T^n)».

### 3. Stabilitet: vektene må være positive (1:35–2:30)

> Del på a P null. Da er den nye temperaturen et *vektet gjennomsnitt* av den gamle temperaturen og naboene. Så lenge alle vektene er positive, kan det ikke oppstå nye topper eller bunner.
> Men vekten foran T P kan bli negativ hvis tidssteget er for stort. Da betyr det: jo varmere nå, jo kaldere i neste steg. Og så varmere igjen. Det svinger, og det vokser.
> Kravet er at a P null skal være minst like stor som summen av a W, a E og minus S P. For de indre cellene gir det det kjente kravet: r høyst en halv.
> Men se på randcellene! Med kjent randtemperatur er avstanden bare en halv celle. Da blir kravet strengere: delta t må være mindre enn rho c delta x i andre, delt på *tre* kappa. Randcellene bestemmer tidssteget.

*På skjermen:* Tre vekter som piler inn mot T_P^{n+1}: «a_W/a_P⁰», «a_E/a_P⁰», «(a_P⁰ − a_W − a_E + S_P)/a_P⁰». En vektskål («gjennomsnitt»). Den midterste vekten krymper og blir negativ (rød) – en graf som sager opp og ned med økende utslag (lyd: «boing-boing-BOING»). Grønn boks: «a_P⁰ ≥ a_W + a_E − S_P ⇔ Δt ≤ ρcΔV/L_PP». Tabell: «indre: ρcδx²/(2κ)», «kjent randtemperatur: ρcδx²/(3κ)» (gul, med et lite «!»), «isolert rand: ρcδx²/κ».

### 4. Eksempel: en plate som avkjøles (2:30–3:40)

> En plate er to hundre grader overalt. Plutselig settes østsiden til null grader, og vestsiden er isolert. Vi bruker fem celler på fire millimeter.
> Den isolerte cellen tåler seksten sekunder, de indre åtte, men randcellen mot den kalde siden bare fem komma tre tre sekunder.
> **[Du:** stopp stoppeklokka.**]**
> Med delta t lik to sekunder går alt fint: Kulda kryper innover fra østsiden, og etter hvert er hele platen null grader – den stasjonære løsningen.
> Men prøver vi seks sekunder – litt over grensen for randcellen – så begynner det å svinge. Og det starter akkurat der vi sa: ved randen.

*På skjermen:* Plata i fem celler (alle røde, «200 °C»), vestvegg med vott-tekstur «isolert», østvegg blå «0 °C» som smeller på (lyd: «klang»). «κ = 10 W/(m K), ρc = 10 · 10⁶ J/(m³ K), δx = 4 mm». Tabell «celle 1: 16 s, celle 2–4: 8 s, celle 5: 5.33 s» (den siste i gult). Animasjon: Δt = 2 s – fargene glir fra rødt til blått fra øst mot vest, og temperaturprofilen synker pent mot null (tikk-lyd). Så «Δt = 6 s»: celle 5 begynner å blinke og grafen får sagtenner som vokser (alarm). Gult kryss: «ustabilt!».

### 5. Til orientering: implisitt (3:40–4:05)

> Vil du slippe dette kravet, kan du regne fluksene ved slutten av tidssteget i stedet. Det er et *implisitt* skjema. Det er stabilt for alle tidssteg – men du må løse et ligningssystem i hvert eneste steg.

*På skjermen:* Lapp «til orientering». «fluks ved t_{n+1} → implisitt: stabilt for alle Δt ✓, men: ligningssystem i hvert steg» med en liten matrise som dukker opp ved hvert tikk.

### 6. Oppsummering av endelig volum-metoden (4:05–4:30)

> Endelig volum er bevaringsloven, skrevet opp for hver celle. I 1D, i 2D, med kilder, med ulike randbetingelser og med tid – alt ender i den samme ligningen. Bare husk tidssteget ved randen. Prøv deg på noen oppgaver!

*På skjermen:* Sluttboksen fra alle fire videoene, nå med alle bidrag på plass: naboer, kilder, rand og tid. Fire små ikoner fra seriene (koppen, votten, sjokoladeruten, stoppeklokka) dukker opp rundt den (pop × 4).

---

**Tall (regnet i Python):** κA/δx = 10 · 1/0.004 = 2500; ρcAδx = 10 · 10⁶ · 0.004 = 40 000; Δt-grenser: celle 1 (isolert) L_PP = 2500 → 16 s, celle 2–4 L_PP = 5000 → 8 s, celle 5 (T = 0) L_PP = 2500 + 5000 = 7500 → 5.33 s. Med Δt = 2 s er a_P⁰ = 20 000.
