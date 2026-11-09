# Manus: Endelig volum-metoden 2 – kildeledd og randbetingelser

**Tema: Numeriske metoder for PDE-er · undertema: Endelig volum-metoden (2 av 4) · ca. 4 min**
**Brukes på:** (ingen side ennå – IMAA3012/IMAx3012, kompendiet §3.5)
**Grunnlag:** foilene F24_EVM_1D_Kilder_Randbetingelser og forelesningsplanen F23–F26.

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** en ullvott eller et skjerf (isolasjon).

**Tavla:** svart tavle. En «sorteringsmaskin» går igjen: hvert bidrag (naboer, kilde, rand) flyr inn i riktig skuff – `a_W`, `a_E`, `S^u` eller `S_P` – med en pop.

---

### 0. Kald start (ca. 6 s)

> **[Du:** ta på deg votten og hold den opp.**]**
> En isolert rand. Matematisk sett er dette det enkleste av alt: ingenting går gjennom.

*På skjermen:* Votten får en stor grønn «q = 0»-lapp (pop).

### 1. Hvor havner bidragene? (0:00–0:25)

> I endelig volum-metoden ender alt i den samme ligningen: a P phi P er lik summen av naboene pluss en kilde S u. Kunsten er å vite hvor hvert bidrag skal. Her ser vi på to ting: kilder inne i cellen, og nye typer randbetingelser.

*På skjermen:* Tittel «Kildeledd og randbetingelser» (oransje). Grønn sluttboks «a_P φ_P = a_W φ_W + a_E φ_E + S^u, a_P = a_W + a_E − S_P». Under: fire skuffer «a_W», «a_E», «S^u», «S_P».

### 2. Kildeleddet (0:25–1:05)

> En kilde produserer noe inne i cellen – for eksempel varme fra en elektrisk strøm. Integrerer vi over cellen, får vi kilden ganger volumet.
> Den skriver vi alltid på lineær form: S u pluss S P ganger phi P. S u er den delen som ikke avhenger av temperaturen. S P er den delen som gjør det.
> Og én regel: S P skal være null eller negativ. En negativ S P er et sluk som blir sterkere jo varmere det er – det gjør systemet stabilt. En positiv S P kan få en iterativ løser til å eksplodere.

*På skjermen:* En celle med en gul stjerne som pulserer («kilde»). «∭ S dV ≈ S̄ ΔV = S^u + S_P φ_P» – S^u og S_P flyr i hver sin skuff (pop, pop). Lapp: «S_P ≤ 0!» med et grønt skilt. To små grafer: «S_P i sluket: konvergerer» (kurve som legger seg) og «S_P i S^u: divergerer» (kurve som eksploderer – lyd: «kaboom» og skjermristing).

### 3. Eksempel: plate med jevn varmeproduksjon (1:05–2:15)

> En plate, to centimeter tykk, produserer tusen kilowatt per kubikkmeter. Venstre side holdes på hundre grader, høyre side på to hundre.
> Vi bruker fem celler. Da er k A delt på delta x lik hundre og tjuefem, og kilden i hver celle er fire tusen.
> I de indre cellene er det rett fram: a W og a E er hundre og tjuefem, og S u er fire tusen.
> I randcellene kommer randen i tillegg. Den halve cellen gir dobbelt ledningsevne, to hundre og femti. Den går inn i S P, og to hundre og femti ganger randtemperaturen går inn i S u.
> Løser vi systemet, ligger alle fem punktene nøyaktig fire grader over den eksakte parabelen. Det er feilen fra randcellene. Halverer vi cellene, blir feilen fire ganger mindre – metoden er av andre orden.

*På skjermen:* En plate (rød glød inni, «q = 1000 kW/m³») mellom en blå vegg «100 °C» og en rød vegg «200 °C». Tallene «k = 0.5 W/(m K), δx = 0.004 m». «kA/δx = 125», «qAδx = 4000». Koeffisienttabellen fylles rad for rad med sorteringsmaskinen: indre celler (125, 125, 4000), randcellene med rødt «S_P = −250» og «S^u = 4000 + 250 · T_V» (pop). Graf: eksakt parabel (turkis) og fem punkter (oransje) 150, 218, 254, 258, 230, med små gule piler «+4 °C» ved hvert punkt. Til slutt: «feil = qδx²/(8k) → halver δx: feil / 4» (2² i gult).

### 4. Kjent fluks og isolert rand (2:15–3:15)

> Noen ganger kjenner vi ikke temperaturen på randen, men *fluksen* – hvor mye varme som strømmer inn. Det er enda enklere.
> Da kjenner vi jo fluksen på randflaten direkte. Vi klipper koblingen mot randen, og legger q B ganger A inn i S u. Ferdig. S P blir ikke rørt.
> **[Du:** hold opp votten.**]**
> Og en isolert rand er bare spesialtilfellet der fluksen er null. Da gir randen ingen bidrag i det hele tatt.

*På skjermen:* Randen til høyre: en pil «q_B» inn gjennom flaten. Saksen klipper koblingen (snipp). «a_E = 0, S^u += q_B A» flyr i S^u-skuffen (pop). Så: veggen får en tegnet strikkevott-tekstur, «q_B = 0 → ingen bidrag» (lyd: et lite «puff»).

### 5. Oppsummering: sorteringsmaskinen (3:15–3:50)

> Så: Naboene gir a W og a E. Kilden gir S u og S P. En kjent temperatur på randen gir et bidrag i både S u og S P. En kjent fluks gir bare et bidrag i S u. Og en isolert rand gir ingenting.
> Og uansett: a P er summen av naboene minus S P. Prøv deg på noen oppgaver!

*På skjermen:* Oversiktstabell som bygges med sorteringsmaskinen: «nabo → a_W, a_E», «kilde → S^u, S_P», «kjent T → S^u + S_P», «kjent fluks → S^u», «isolert → –». Grønn boks: «a_P = a_W + a_E − S_P».

---

**Tall (regnet i Python):** kA/δx = 0.5 · 1/0.004 = 125; qAδx = 1 000 000 · 1 · 0.004 = 4000; randceller S_P = −250, S^u = 4000 + 250 · 100 = 29 000 og 4000 + 250 · 200 = 54 000. Løsning: T = 150, 218, 254, 258, 230 °C; eksakt i nodene: 146, 214, 250, 254, 226 °C (avvik 4 °C = qδx²/(8k) = 10⁶ · 0.004²/4).
