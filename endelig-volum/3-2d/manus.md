# Manus: Endelig volum-metoden 3 – to dimensjoner

**Tema: Numeriske metoder for PDE-er · undertema: Endelig volum-metoden (3 av 4) · ca. 4 min**
**Brukes på:** (ingen side ennå – IMAA3012/IMAx3012, kompendiet §3.6)
**Grunnlag:** foilene F25_EVM_2D og forelesningsplanen F23–F26.

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** en sjokoladeplate med ruter (3 × 4 er perfekt).

**Tavla:** svart tavle. Et 3 × 4-gitter som går igjen gjennom hele videoen, med et kompass (N, S, Ø, V) i hjørnet. Cellene farges som et varmekart til slutt.

---

### 0. Kald start (ca. 6 s)

> **[Du:** hold opp sjokoladeplata og bræk av én rute.**]**
> Tolv kontrollvolum. Og hver rute har fire naboer … nesten.

*På skjermen:* Plata blir et 3 × 4-gitter på tavla (svisj). Én rute lyser opp med fire piler ut til naboene (pop × 4).

### 1. Fra 1D til 2D (0:00–0:40)

> I én dimensjon hadde hver celle to naboer, vest og øst. I to dimensjoner får vi to til: sør og nord. Og fire flater: w, e, s og n.
> Det er egentlig ikke noe nytt i metoden. Vi integrerer over cellen, og divergenssetningen gjør det om til fluks gjennom de fire flatene.

*På skjermen:* Tittel «Endelig volum i 2D» (oransje). 1D-staven med W–P–E roterer, og N og S kommer til (svisj). Celle P med flatene w, e, s, n, og flatearealene «A_w = A_e = δy · t» og «A_s = A_n = δx · t». Fire røde flukspiler over flatene.

### 2. Den diskrete ligningen (0:40–1:20)

> Fluksene tilnærmer vi akkurat som før: en rett linje mellom nodene. Da får vi den samme ligningen – bare med fire naboer.
> a P phi P er lik a W phi W pluss a E phi E pluss a S phi S pluss a N phi N pluss S u. Og a P er summen av de fire, minus S P.
> Med konstant Gamma og kvadratiske celler er dette den samme fempunktsformelen som vi kjenner fra endelige differanser. Forskjellen ligger igjen i randen.

*På skjermen:* Sluttboksen fra før får to nye ledd som flyr inn (popp, popp): «+ a_S φ_S + a_N φ_N». «a_P = a_W + a_E + a_S + a_N − S_P». Ved siden av: et fempunkts-stensil (pluss-form) med −1, −1, 4, −1, −1, og teksten «= fempunktsformelen».

### 3. Randceller og hjørneceller (1:20–2:00)

> Langs veggene gjør vi det samme som i 1D: klipp koblingen mot veggen, og legg bidraget i S u og S P.
> En kjent temperatur gir et bidrag i begge. En kjent fluks gir bare et bidrag i S u. En isolert vegg gir ingenting.
> **[Du:** pek på et hjørne av sjokoladeplata.**]**
> Og et hjørne? Det ligger inntil *to* vegger – og får ett bidrag fra hver.

*På skjermen:* Gitteret med veggene farget: kjent T (rød), kjent fluks (gul pil), isolert (grå vott-tekstur fra forrige stil). En saks går rundt kanten og klipper koblinger (snipp-snipp-snipp). Et hjørne blinker med to små piler: «to bidrag!».

### 4. Eksempel: plate med varmefluks fra vest (2:00–3:20)

> En plate, tretti ganger førti centimeter, én centimeter tykk. Fra vest strømmer det inn fem hundre kilowatt per kvadratmeter. Sør og øst er isolert, og nord holdes på hundre grader.
> Vi deler i tre ganger fire celler på ti centimeter. Alle de indre koblingene blir like: kappa A delt på delta x er ti.
> Vestveggen gir fem hundre i S u. Nordveggen gir minus tjue i S P, og to tusen i S u. Og hjørnet oppe i nordvest får begge deler.
> Løser vi de tolv ligningene, blir det varmest der varmen kommer inn, nede i sørvest: to hundre og seksti grader. Og kaldest oppe ved den kalde nordveggen.
> Og sjekken: Fire celler tar inn fem hundre watt hver – to tusen watt. Nøyaktig like mye går ut gjennom nordveggen. Bevaring – helt eksakt.

*På skjermen:* Plata med mål «0.3 m × 0.4 m, t = 1 cm, κ = 1000 W/(m K)». Gule piler inn fra vest «q_V = 500 kW/m²», grå isolasjon i sør og øst, blå nordvegg «100 °C». Cellene nummereres 1–12, rad for rad (pop pop pop). «κA/δx = (1000 · 0.1 · 0.01)/0.1 = 10». Sorteringsmaskinen fra 1D: «vest: S^u += 500», «nord: S_P −= 20, S^u += 2000». Hjørne 10 blinker. Så fylles varmekartet celle for celle (fra blått til rødt) med tallene 260.0 … 124.0. Energibalanse: «inn: 4 · 500 W = 2000 W» og «ut gjennom nord: 2000 W» med en vekt som balanserer (lyd: «pling»).

### 5. Finere gitter (3:20–3:45)

> Vil vi ha mer nøyaktighet, deler vi bare finere. Ligningene ser helt like ut – det blir bare flere av dem. Og bevaringen holder fortsatt eksakt, på hvert eneste gitter.

*På skjermen:* Gitteret deles 2 og 4 ganger finere (svisj), varmekartet blir glattere. Teksten «bevaring: eksakt på alle gitre ✓».

### 6. Avslutning (3:45–4:00)

> I to dimensjoner: fire naboer, fire flater, og hjørnene får bidrag fra to vegger. Ellers er alt som før. Prøv deg på noen oppgaver!

*På skjermen:* Sluttboksen med fire naboer, og 2D-gitteret med kompasset. Sjokoladeruten fra kald start dukker opp en siste gang (pop).

---

**Tall (regnet i Python):** κA/δx = 1000 · (0.1 · 0.01)/0.1 = 10; vestvegg q_V A_w = 500 000 · 0.1 · 0.01 = 500 W; nordvegg 2κA/δy = 20, S^u = 20 · 100 = 2000. Løsning (nord øverst): 146.3, 129.7, 124.0 / 205.6, 178.2, 166.2 / 242.3, 211.2, 196.5 / 260.0, 227.8, 212.2 °C. Energibalanse: 4 · 500 W = 2000 W inn, 2000 W ut gjennom nord.
