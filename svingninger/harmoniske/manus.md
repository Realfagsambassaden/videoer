# Manus: Harmoniske svingninger

**Tema: Svingninger · undertema: Harmoniske svingninger · ca. 3 min**
**Brukes på:** (ingen side ennå)

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** en fjær eller en kraftig strikk med et lodd i enden (f.eks. et nøkkelknippe eller en liten flaske), og hjulet ditt (gyroskop-hjulet) med en tapebit på kanten. Ikke grønne ting.

**Tavla:** loddet i fjæra tegnet ved hånda di, med en tusj som tegner en kurve på et papir som glir forbi. Dashman på en huske. Et hjul med en prikk som kaster skygge på en vegg. Alt tegnes i tavlestil.

---

### 0. Kald start (ca. 5 s)

> **[Du:** hold fjæra med loddet ut fra deg, dra loddet litt ned og slipp. La det hoppe opp og ned noen ganger, og følg det med blikket.**]**
> Opp, ned, opp, ned … i nøyaktig samme takt.

*På skjermen:* Loddet tegnes i takt med ditt lodd. En tusj på loddet tegner en bølgeformet kurve på et papir som ruller forbi mot venstre.

### 1. Likevekt og tilbakeførende kraft (0:00–0:30)

> Når loddet henger i ro, er det i *likevekt*. Drar jeg det ned, drar fjæra det tilbake. Det kaller vi en tilbakeførende kraft.
> Men loddet får fart, så det suser forbi likevekten. Da snur kraften og bremser det, og slik fortsetter det. Det er en *svingning*.

*På skjermen:* Tittelen «Harmoniske svingninger» i oransje. Loddet med en stiplet linje for likevekt. Når loddet er under likevekt, peker kraftpila F⃗ (oransje) opp; når det er over, peker den ned. Fartspila v⃗ (turkis) er størst ved likevekt.

### 2. Tre tall (0:30–1:05)

> En svingning beskriver vi med tre tall. *Amplituden*, A, er det største utslaget fra likevekten. *Perioden*, T, er tiden én hel svingning tar: ned, opp og tilbake. Og *frekvensen*, f, er antall svingninger per sekund. Den måles i hertz.
> Tar én svingning et kvart sekund, blir det fire svingninger hvert sekund. Frekvensen er én delt på perioden.

*På skjermen:* Kurven fra kald start blir en graf med aksene «x» og «t». A markeres som høyden fra midtlinja til toppen (gul), T som avstanden mellom to topper (turkis). «f = 1/T» i grønn boks (stablet brøk), og «1 Hz = 1 s⁻¹». Eksempel under: «T = 0.25 s → f = 4.0 Hz».

### 3. En cosinuskurve (1:05–1:40)

> Kurven tusjen tegnet, har akkurat samme form som en cosinus. Derfor kaller vi det en *harmonisk* svingning.
> Posisjonen er *x er lik A cosinus to pi t delt på T*. Hver gang det har gått én periode, har vinkelen inni cosinus gått én hel runde, to pi, og alt begynner på nytt. Tallet to pi delt på T kaller vi *vinkelfrekvensen*, omega.
> Det samme gjelder Dashman på huska!

*På skjermen:* «x(t) = A cos(2π t / T)» i grønn boks (stablet brøk), og «ω = 2π/T» under (turkis). Dashman på en huske ved siden av, som svinger i takt med kurven og roper «wiii!».

### 4. Hvor fort går det? (1:40–2:10)

> **[Du:** snurr hjulet sakte og pek på tapebiten.**]**
> Se på en prikk som går rundt i en sirkel. Fra siden går skyggen opp og ned, akkurat som loddet. Midt i går skyggen like fort som prikken. Prikken går omkretsen, to pi A, på én periode. Så den største farten er *to pi A delt på T*.

*På skjermen:* Et hjul med en prikk som går rundt, og skyggen av prikken på en vegg ved siden av som går opp og ned i takt med loddet. «v_maks = 2πA / T = ωA» i grønn boks (stablede brøker).

### 5. Et eksempel (2:10–2:45)

> Loddet i fjæra svinger fem centimeter opp og ned fra likevekt. Jeg teller tolv svingninger på seks sekunder.
> Da er perioden et halvt sekund, og frekvensen to hertz. Den største farten blir to pi ganger fem centimeter, delt på et halvt sekund: rundt sekstitre centimeter per sekund. Og det har loddet akkurat når det suser forbi likevekten.

*På skjermen:* «A = 5.0 cm, 12 svingninger på 6.0 s». «T = 6.0 s / 12 = 0.50 s», «f = 1/T = 2.0 Hz». «v_maks = 2π · 0.050 m / 0.50 s ≈ 0.63 m/s» (stablede brøker). En liten stoppeklokke som teller til 12.

### 6. Avslutning (2:45–3:00)

> Mens loddet svinger, går energien fram og tilbake mellom fjæra og farten. Uten friksjon ville det aldri stoppet. Prøv deg på noen oppgaver!

*På skjermen:* Oppsummering: «f = 1/T», «x = A cos(2πt/T)», «v_maks = 2πA/T» (stablede brøker). To små søyler som vipper fram og tilbake: «E_p fjær» og «E_k». Fysikkhjelp-logoen. Dashman hopper av huska på toppen.

---

**Tall (regnet i Python):** T = 0.25 s → f = 1/0.25 s = 4.0 Hz. Eksempel: T = 6.0 s / 12 = 0.50 s (12 er en telling, eksakt), f = 2.0 Hz, ω = 2π/0.50 s = 12.6 s⁻¹, v_maks = 2π · 0.050 m / 0.50 s = 0.628 m/s ≈ 0.63 m/s.
