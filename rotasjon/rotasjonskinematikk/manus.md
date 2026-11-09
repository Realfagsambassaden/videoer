# Manus: Rotasjonskinematikk

**Tema: Rotasjon og spinn · undertema: Rotasjonskinematikk · ca. 3 min**
**Brukes på:** (ingen side ennå)

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** hjulet ditt (gyroskop-hjulet) med to små tapebiter (ikke grønne): én like ved navet og én helt ute på kanten.

**Tavla:** hjulet tegnet stort med de to tapebitene som prikker (gul inne, oransje ute), en vinkel-bue, Dashman på en karusell og Dashman som snurrer rundt i en vaskemaskin. Alt tegnes i tavlestil.

---

### 0. Kald start (ca. 5 s)

> **[Du:** hold hjulet opp mot kamera og gi det en god snurr. Pek først på tapen ved navet, så på tapen ute på kanten.**]**
> Hvem av disse to går fortest?

*På skjermen:* Det tegnede hjulet snurrer i takt med ditt. Den gule prikken (inne) og den oransje prikken (ute) trekker hver sin sirkel etter seg, den oransje mye lengre. Et stort «?».

### 1. Vinkel i radianer (0:00–0:35)

> Begge tapebitene går én runde på samme tid. Men den ytterste går mye lengre. Derfor beskriver vi rotasjon med vinkelen hjulet har dreid, ikke med strekningen.
> Fysikere måler vinkler i *radianer*: buen delt på radien. Én hel runde er to pi radianer, altså tre hundre og seksti grader. Det ser kanskje rart ut, men med radianer blir formlene mye enklere, som du snart skal se.

*På skjermen:* Tittelen «Rotasjonskinematikk» i oransje. Hjulet med en radius r og en bue s (turkis) langs kanten. «θ = s/r» (stablet brøk). Så «1 runde = 2π rad = 360°» i grønn boks, og «1 rad ≈ 57°» mindre under.

### 2. Vinkelfart og vinkelakselerasjon (0:35–1:10)

> Hvor fort vinkelen endrer seg, kaller vi *vinkelfarten*, omega: d theta delt på d t. Den måles i radianer per sekund.
> Og hvor fort vinkelfarten endrer seg, er *vinkelakselerasjonen*, alfa: d omega delt på d t.
> Når vaskemaskinen starter sentrifugeringen, øker vinkelfarten, og alfa er positiv. Når den bremser, er alfa negativ.
> Det fine er at hele hjulet har samme vinkelfart. Begge tapebitene dreier like mange radianer hvert sekund.

*På skjermen:* «ω = dθ/dt» og «α = dω/dt» (stablede brøker, dθ og dω oppreist d). Begge prikkene på hjulet får en like stor vinkel-bue (gul). «Samme ω for hele hjulet!» i turkis.

### 3. Fra vinkelfart til fart (1:10–1:45)

> Men farten er ikke den samme. Buen er radien ganger vinkelen, så farten blir *v er lik r omega*.
> **[Du:** snurr hjulet igjen og pek ut på kanten.**]**
> Dobbelt så langt ut, dobbelt så stor fart. Det merker Dashman på karusellen: Inne ved midten er det rolig. Ute på kanten må han holde seg fast!

*På skjermen:* «s = rθ» → «v = rω» i grønn boks, der θ byttes ut med ω med et «popp». Proporsjonaliteten: «(2r) · ω = 2v» med 2-tallene i gult. Dashman på en karusell sett ovenfra: én Dashman ved midten som drikker kaffe, én ute på kanten med fartsstreker, flagrende skjerf og hendene klamret fast.

### 4. Samme formler som før (1:45–2:10)

> Og har du lært bevegelse med konstant akselerasjon, kan du alt allerede. Formlene er de samme. Bare bytt strekning med vinkel, fart med vinkelfart og akselerasjon med vinkelakselerasjon. Vinkelfarten ved tiden t blir for eksempel *omega null pluss alfa t*.

*På skjermen:* To kolonner. Venstre: «v = v₀ + at», «s = v₀t + ½at²». Høyre: «ω = ω₀ + αt», «θ = ω₀t + ½αt²» (stablede brøker). Pilene «s → θ», «v → ω», «a → α» flyr over fra venstre til høyre, og bokstavene bytter seg ut med et «popp» (turkis).

### 5. Et eksempel: vaskemaskinen (2:10–2:45)

> En vaskemaskin sentrifugerer med fjorten hundre runder i minuttet. Trommelen har radius tjue centimeter. Hvor fort går sokken langs veggen?
> Fjorten hundre ganger to pi, delt på seksti sekunder: rundt hundre og førtisju radianer per sekund. Ganger vi med radien, får vi nesten tretti meter per sekund. Det er over hundre kilometer i timen! Ikke rart klærne blir nesten tørre.

*På skjermen:* En vaskemaskin med Dashman (som en sokk) klistret til trommelveggen, svimmel med spiraløyne. «1400 omdr/min, r = 20 cm». «ω = 1400 · 2π / 60 s ≈ 147 rad/s» (stablet brøk). «v = rω = 0.20 m · 147 rad/s ≈ 29 m/s» og «29 m/s · 3.6 ≈ 110 km/h» med «> 100 km/h!» i gult.

### 6. Avslutning (2:45–3:00)

> Rotasjon beskriver vi med vinkel, vinkelfart og vinkelakselerasjon. Hele hjulet har samme vinkelfart, men jo lenger ut, jo større fart. Prøv deg på noen oppgaver!

*På skjermen:* Oppsummering: «θ = s/r», «ω = dθ/dt», «α = dω/dt», «v = rω» (stablede brøker). Fysikkhjelp-logoen. Dashman kravler ut av vaskemaskinen, tørr og svimmel.

---

**Tall (regnet i Python):** 1 omdr/min = 2π/60 rad/s = 0.1047 rad/s. ω = 1400 · 2π / 60 s = 146.6 rad/s ≈ 147 rad/s. v = 0.20 m · 146.6 rad/s = 29.3 m/s ≈ 29 m/s = 105.6 km/h ≈ 110 km/h med to gjeldende siffer (over 100 km/h). (Ikke brukt i tale: sentripetalakselerasjonen rω² = 4.3 km/s², ca. 440 g.)
