# Manus: Luftmotstand

**Tema: Newtons lover og krefter · undertema: Luftmotstand · ca. 3 min**
**Brukes på:** (ingen side ennå)

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** to like ark papir (A4) og fem kaffefiltre eller muffinsformer av papir. Ikke grønne.

**Tavla:** Dashman som hopper ut av et fly, kraftpiler G⃗ og F⃗_D, en v–t-graf som flater ut, og Dashman med fallskjerm. Alt tegnes i tavlestil.

---

### 0. Kald start (ca. 5 s)

> **[Du:** hold et flatt ark i hver hånd i hodehøyde. Krøll det ene til en ball, og slipp begge samtidig. Ballen treffer gulvet lenge før det flate arket.**]**
> Samme masse. Samme tyngde. Så hvorfor …?

*På skjermen:* Vekter over arkene: «samme m». Det flate arket får en stiplet bølgebane, og ballen en rett strek.

### 1. Hva er luftmotstand? (0:00–0:30)

> For å komme fram må alt som beveger seg, dytte lufta til side. Og lufta dytter tilbake. Det er luftmotstanden, og den peker alltid motsatt av fartsretningen.
> **[Du:** hold hånda ut som om du har den ut av bilvinduet, og vri den.**]**
> Du kjenner den hvis du har hånda ut av bilvinduet. Jo fortere det går, og jo større flate du viser fram, desto hardere dytter lufta.

*På skjermen:* Tittelen «Luftmotstand» i oransje. En hånd i vind med vindstreker: flat hånd liten pil, hånda på tvers stor pil. Stikkord: «fart», «areal», «form», «lufttetthet».

### 2. Formelen (0:30–1:00)

> Luftmotstanden er *en halv C rho A v i andre*. A er arealet tingen viser mot fartsretningen, rho er tettheten til lufta, og C er et tall for formen. Strømlinjet gir liten C.
> Legg merke til v i andre: Dobbelt så stor fart gir *fire* ganger så stor luftmotstand.

*På skjermen:* Grønn boks: «F_D = ½ · C · ρ · A · v²» (stablet brøk). Pilene peker på hver bokstav: «C: formen», «ρ: luft, ca. 1.2 kg/m³», «A: frontareal», «v: fart». Så «4 · F_D = ½ · C · ρ · A · (2 · v)²» med 2 og 4 i gult («pop»). En dråpeform med «liten C» og en fallskjerm med «stor C».

### 3. Dashman faller (1:00–1:40)

> Dashman hopper ut av et fly. I starten går det sakte, og nesten bare tyngden virker. Han akselererer med g.
> Men jo fortere han faller, desto større blir luftmotstanden. Akselerasjonen blir mindre og mindre.
> Til slutt er luftmotstanden like stor som tyngden. Da er kraftsummen null, og etter Newtons første lov faller han med konstant fart. Det er *terminalfarten*. For en fallskjermhopper tar det bare rundt ti sekunder å komme dit.

*På skjermen:* Dashman i fritt fall (armer og bein ut, kinnene blafrer). G⃗ ned er like lang hele tiden, F⃗_D opp vokser til den er like lang. «ΣF = G − F_D = m a». Ved siden av: en v–t-graf som starter bratt og flater ut mot en stiplet linje «v_t», med «ca. 10 s» på tidsaksen.

### 4. Terminalfarten (1:40–2:15)

> Vi setter luftmotstanden lik tyngden og løser for farten. Da blir terminalfarten kvadratroten av to m g delt på C rho A.
> **[Du:** slipp ett kaffefilter, og så fire stablet oppi hverandre.**]**
> Fire ganger så stor masse, men samme form. Da faller de dobbelt så fort, fordi kvadratroten av fire er to.
> Tunge ting med samme form faller altså fortere i lufta. I vakuum, uten luft, ville alt falt like fort.

*På skjermen:* «½ · C · ρ · A · v_t² = m g» ⇒ grønn boks: «v_t = √(2 m g / (C ρ A))» (stablet brøk under rottegnet, g oppreist). Ved filtrene: «4 · m → √4 · v_t = 2 · v_t» med 4 og 2 i gult.

### 5. Et eksempel (2:15–2:45)

> Dashman og utstyret veier 80 kilo. Han faller med magen ned, med et areal på 0.70 kvadratmeter og C lik én. Da blir terminalfarten rundt 43 meter per sekund. Det er 160 kilometer i timen!
> Så løser han ut fallskjermen. Arealet blir mye større, og farten faller til rundt seks meter per sekund. Puh.

*På skjermen:* «m = 80 kg, A = 0.70 m², C = 1.0, ρ = 1.2 kg/m³». «v_t = √(2 · 80 kg · 9.81 m/s² / (1.0 · 1.2 kg/m³ · 0.70 m²)) ≈ 43 m/s ≈ 160 km/h» (gul). Fallskjermen spretter ut («pop», «boing»): «A = 25 m², C = 1.5 → v_t ≈ 5.9 m/s». Dashman henger og dingler og vinker.

### 6. Avslutning (2:45–3:00)

> Og arkene? Det flate arket viser en stor flate, så det når en lav terminalfart nesten med en gang. Det krøllete arket har mindre areal, så det kommer opp i større fart før luftmotstanden tar igjen tyngden. Prøv deg på noen oppgaver!

*På skjermen:* Oppsummering: «F_D = ½ C ρ A v²», «terminalfart: F_D = G». Fysikkhjelp-logoen. Dashman lander mykt og fallskjermen dekker ham.

---

**Tall (regnet i Python):** Dashman: v_t = √(2 · 80 · 9.81 / (1.0 · 1.2 · 0.70)) m/s = 43.2 m/s ≈ 43 m/s = 155.6 km/h ≈ 160 km/h (2 gjeldende siffer). Fallskjerm: v_t = √(2 · 80 · 9.81 / (1.5 · 1.2 · 25)) m/s = 5.91 m/s ≈ 5.9 m/s. Kaffefiltrene: √4 = 2. Tid til nær terminalfart (uten fallskjerm): τ = v_t/g = 4.4 s; 95 % av v_t etter 8.1 s, 99 % etter 11.7 s → «rundt ti sekunder».
