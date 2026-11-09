# Manus: Satellitter og planetbaner

**Tema: Gravitasjon · undertema: Satellitter og planetbaner · ca. 3 min**
**Brukes på:** (ingen side ennå)

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** en myk ball eller et par sammenrullede sokker (ikke grønt), som du kaster vannrett ut av bildet mot venstre.

**Tavla:** Jorda med et høyt fjell på toppen og Newtons kanon, romstasjonen med Dashman som svever inni, og sola med planetbaner. Alt tegnes i tavlestil.

---

### 0. Kald start (ca. 5 s)

> **[Du:** kast ballen vannrett ut mot venstre, først forsiktig, så hardere.**]**
> Hvor hardt må jeg kaste for at den aldri skal lande?

*På skjermen:* To kastebaner som buer ned mot bakken, den andre lengre. Så en tredje, stiplet bane i gult som går helt rundt jordkloden og kommer tilbake bak deg. «?!» og svisj.

### 1. Å falle rundt jorda (0:00–0:35)

> Kaster jeg hardere, lander ballen lenger unna. Men jorda er rund. Kaster jeg *hardt nok*, krummer bakken seg bort like fort som ballen faller.
> Da faller den hele tiden, men treffer aldri. Den går i bane. En satellitt er rett og slett noe som faller rundt jorda.

*På skjermen:* Tittelen «Satellitter og planetbaner» i oransje. Jorda med et høyt fjell og en kanon på toppen. Dashman fyrer av kanonen med større og større fart: banene blir lengre og lengre, til den siste går helt rundt og treffer Dashman i bakhodet («boing»).

### 2. Banefarten (0:35–1:20)

> Hvor fort må den gå? I en sirkelbane er det gravitasjonen som gir sentripetalkraften.
> G ganger M m delt på r i andre er lik m v i andre delt på r.
> Satellittens masse m stryker seg, og én r forsvinner. Farten blir *kvadratroten av G M delt på r*.
> Legg merke til: Farten avhenger ikke av hvor tung satellitten er. En skrue og en romstasjon i samme høyde går like fort.

*På skjermen:* Jorda (M) og satellitten (m) i sirkelbane med radius r fra jordsenteret. «G · Mm / r² = m · v² / r» (stablede brøker, G oppreist). De to m-ene strykes over med gul strek, og r i nevneren forkortes («pop»). Grønn boks: «v = √(G M / r)». En liten skrue og romstasjonen ved siden av hverandre: «samme fart».

### 3. Et eksempel: romstasjonen (1:20–2:00)

> Romstasjonen går rundt 420 kilometer over bakken. Da er r jordradien pluss høyden: rundt 6800 kilometer.
> Setter vi inn, blir farten 7.7 kilometer per sekund. Det er over 27 000 kilometer i timen!
> En runde tar to pi r delt på v: omtrent 93 minutter.
> Og astronautene svever – ikke fordi tyngdekraften er borte, men fordi de faller sammen med stasjonen.

*På skjermen:* «h = 420 km», «r = R + h = 6371 km + 420 km = 6791 km». «v = √(6.674 · 10⁻¹¹ · 5.972 · 10²⁴ / 6.791 · 10⁶) m/s ≈ 7.66 km/s ≈ 27 600 km/h». «T = 2πr / v ≈ 5570 s ≈ 93 min» (stablede brøker). Dashman svever inne i stasjonen med kaffen svevende ut av koppen: «Jeg faller!» – «Ja, hele tiden.»

### 4. Høyere opp går det saktere (2:00–2:30)

> Jo lenger ut, jo saktere går satellitten, og jo lenger blir runden. Setter vi v inn i omløpstiden, får vi at *T i andre er proporsjonal med r i tredje*.
> Det er Keplers tredje lov. Fire ganger så langt ut gir åtte ganger så lang omløpstid.
> Langt nok ute bruker satellitten et døgn – og står stille over samme sted. Det er TV-satellittene.

*På skjermen:* «T = 2πr / v», der v = √(G M / r) flyr inn med et «popp». Grønn boks: «T² = 4π² / (G M) · r³» (stablet brøk). «4r → 4^(3/2) = 8 · T» i gult. En satellitt langt ute (r ≈ 42 000 km) over et fast punkt med en parabolantenne på et hustak: «T = 1 døgn».

### 5. Planetene (2:30–2:45)

> Det samme gjelder planetene rundt sola, og månen rundt jorda, bare med solmassen i stedet for jordmassen. Banene er egentlig litt avlange ellipser, men forholdet T i andre delt på r i tredje er det samme for alle.

*På skjermen:* Sola med fire planetbaner (litt avlange ellipser). Tabell som fylles ut: Jorda og Mars med «T² / r³ = samme» (stablet brøk). Dashman vinker fra jordkloden.

### 6. Avslutning (2:45–3:00)

> En satellitt faller hele tiden, men bommer på jorda. Gravitasjonen gir sentripetalkraften, og det gir både farten og omløpstiden. Prøv deg på noen oppgaver!

*På skjermen:* Oppsummering: «v = √(G M / r)», «T² ∝ r³». Fysikkhjelp-logoen. Ballen fra kald start kommer susende inn bakfra og lander i hånda di («pop»).

---

**Tall (regnet i Python):** G = 6.674 · 10⁻¹¹ N m²/kg², M = 5.972 · 10²⁴ kg, R = 6.371 · 10⁶ m. Romstasjonen: r = 6.791 · 10⁶ m, v = √(GM/r) = 7661 m/s ≈ 7.66 km/s = 27 580 km/h ≈ 27 600 km/h, T = 2πr/v = 5570 s = 92.8 min ≈ 93 min. Keplers 3. lov: 4^(3/2) = 8. Geostasjonær bane (T = 1 stjernedøgn = 86 164 s): r = 4.22 · 10⁷ m ≈ 42 000 km fra jordsenteret (ca. 36 000 km over bakken). Kontroll: T²/r³ = 4π²/(GM) = 9.90 · 10⁻¹⁴ s²/m³.
