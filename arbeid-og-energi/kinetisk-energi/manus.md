# Manus: Kinetisk energi

**Emne: Arbeid og energi · delemne: Kinetisk og potensiell energi · ca. 3 min**
**Brukes på:** (ingen side ennå)

Les i rolig tempo, ca. 140 ord i minuttet. Du filmer deg selv foran grønnskjermen og havner nede til høyre i videoen. Tidskodene er omtrentlige. Animasjonen tilpasses det du faktisk sier og gjør i opptaket. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet.

**Rekvisitter:** en lekebil (eller en ball) og gjerne en bok som «vegg». Ikke grønne.

**Tegning fra deg (valgfritt):** Dashman i en bil, sett fra siden. Den animeres på tavla (bilen kjører, hjulene går rundt). Alt annet på tavla lager jeg med TikZ/SVG.

Utledningen følger samme idé som i «Potensiell energi»: **arbeid = arealet under en graf**, og arealet er en trekant.

---

### 1. Intro (0:00–0:20)

> **[Du:** dytt lekebilen så den triller bortover bordet.**]**
> Når jeg dytter på bilen, gjør jeg et arbeid. Og arbeid er overføring av energi. Men hvor blir energien av denne gangen?
> Den ligger i bevegelsen. Energi som et legeme har fordi det beveger seg, kaller vi *kinetisk energi*, eller bevegelsesenergi.

*På skjermen:* Tittelen «Kinetisk energi» i oransje. «Arbeid = overføring av energi» skrives under. Dashman-bilen kjører inn fra venstre med fartsstreker (svisj).

### 2. Dashman gir gass (0:20–0:45)

> Tenk deg at Dashman står stille i bilen sin. Så gir han gass. En konstant kraft F virker framover, og bilen akselererer jevnt.
> Etter en tid t har bilen fått farten v. Hvor mye arbeid har kraften gjort? Det er kraft ganger strekning: *W er lik F ganger s*.
> Vi må altså finne både kraften og strekningen, uttrykt med farten.

*På skjermen:* Bilen i ro med v₀ = 0, så kraftpila F⃗ framover (pop). Bilen kjører strekningen s⃗ (oransje pil under) og får farten v⃗. Boksen «W = F · s».

### 3. Kraften: Newtons 2. lov (0:45–1:05)

> Kraften finner vi fra Newtons andre lov: *F er lik m ganger a*.
> Akselerasjonen er hvor fort farten endrer seg. Bilen går fra null til v på tiden t, så a er v delt på t.
> Kraften blir dermed *m ganger v delt på t*.

*På skjermen:* «ΣF⃗ = ma⃗», så «a = v/t» (stablet brøk), så «F = m · v/t». Stablede brøker.

### 4. Strekningen: arealet under fartsgrafen (1:05–1:40)

> Strekningen finner vi med et triks du kjenner igjen: arealet under en graf.
> **[Du:** tegn en skrå linje i lufta med hånda.**]**
> Tegner vi farten mot tiden, får vi en rett linje fra null og opp til v. Strekningen er arealet under grafen. Og arealet er en trekant!
> Areal av trekant er en halv ganger grunnlinje ganger høyde. Grunnlinja er t, høyden er v. Strekningen er altså *en halv v t*.

*På skjermen:* Aksene v og t, linja fra 0 til (t, v). Trekanten fylles grå fra venstre. «Areal av trekant: A = ½ · g · h» med en liten trekant, så g = t og h = v (oransje), så «s = ½ · v · t» (stablede brøker).

### 5. Sett sammen (1:40–2:10)

> Nå setter vi inn i arbeidet. W er F ganger s: *m v delt på t*, ganger *en halv v t*.
> **[Du:** klapp hendene sammen når t-ene forsvinner.**]**
> Tiden t forkorter seg bort! Igjen står *en halv m v i andre*.
> Dette arbeidet forsvinner ikke. Det ligger i bevegelsen som kinetisk energi: *E k er lik en halv m v i andre*.

*På skjermen:* W = F · s = m·(v/t) · ½·v·t. De to t-ene strykes over med en gul strek («pop»). W = ½mv². Grønn boks: «Kinetisk energi: E_k = ½mv²».

*(Valgfritt for ingeniørfysikk – kan droppes:* «Med integraler går det for enhver kraft: W = ∫ F⃗ · dx⃗ = ∫ m v dv = ½mv² − ½mv₀².» *Vises kort som en liten boks.)*

### 6. Hva betyr v i andre? (2:10–2:40)

> Legg merke til at farten står i andre. Kjører Dashman i 50 kilometer i timen, og bilen veier ett tonn, er den kinetiske energien rundt 96 kilojoule.
> Dobler han farten til 100, blir energien ikke dobbelt så stor, men *fire* ganger så stor – nesten 400 kilojoule.
> Det er derfor bremselengden øker så mye med farten.

*På skjermen:* m = 1000 kg, v = 50 km/h = 13.9 m/s, E_k = 96 kJ. Så v = 100 km/h = 27.8 m/s, E_k = 390 kJ og «×4!» i gult. Dashman-bilen kjører fortere (lengre fartsstreker).

### 7. Avslutning (2:40–3:00)

> **[Du:** dytt bilen inn i boka, så den stopper.**]**
> For å stoppe bilen må noe gjøre det samme arbeidet, bare motsatt vei. Arbeid gir bevegelsesenergi, og bevegelsesenergi kan gjøre arbeid. Prøv deg på oppgavene under videoen!

*På skjermen:* Oppsummering: «Arbeid ⇄ kinetisk energi», «E_k = ½mv²» (stablet brøk). Eventuell Dashman-stinger.

---

**Tall (regnet i Python):** 50 km/h = 13.89 m/s → E_k = ½ · 1000 kg · (13.89 m/s)² = 96 450 J ≈ 96 kJ. 100 km/h = 27.78 m/s → 385 800 J ≈ 390 kJ (= 4 × 96 kJ).
