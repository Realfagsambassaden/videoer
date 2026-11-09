# Manus: Endelig volum-metoden 1 – idéen og 1D diffusjon

**Tema: Numeriske metoder for PDE-er · undertema: Endelig volum-metoden (1 av 4) · ca. 4 min**
**Brukes på:** (ingen side ennå – IMAA3012/IMAx3012, kompendiet §3.4–3.5)
**Grunnlag:** foilene F23_EVM_1D_Diffusjon og forelesningsplanen F23–F26.

Les i rolig tempo, ca. 140 ord i minuttet. Du står foran grønnskjermen og havner nede til høyre. Tidskodene er omtrentlige. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet. Improviser gjerne: jeg følger det du faktisk sier.

**Rekvisitter:** en pakke kjeks eller en eske med sukkerbiter (noe du kan «dele opp i celler»), og en kopp med varm drikke.

**Tavla:** svart tavle i vanlig stil. Røde tråd i alle fire videoene: *bevaringsloven skrevet opp for hver celle*. Hver video ender i den samme «sluttboksen» `a_P φ_P = Σ a_nb φ_nb + S^u`, som fylles litt mer for hver video.

---

### 0. Kald start (ca. 8 s)

> **[Du:** hold koppen med begge hender og se fornøyd ut.**]**
> Varmen fra koppen går inn i hendene mine. Og det som går ut av koppen … må gå inn et annet sted. Det er hele hemmeligheten bak endelig volum-metoden.

*På skjermen:* Røde varmepiler fra koppen ut i hendene. Teksten «ut av én = inn i neste» spretter inn (pop).

### 1. Hvorfor en ny metode? (0:00–0:40)

> Med endelige differanser tilnærmer vi de *deriverte* i punkter. Endelig volum-metoden starter et annet sted: med *bevaringsloven*.
> Vi deler området i små celler – kontrollvolum – og krever at det som strømmer inn i en celle, minus det som strømmer ut, er lik det som produseres inni.
> Det gir tre fordeler: bevaring er bygget inn, cellene kan ha hvilken som helst form, og det går fint selv om materialet hopper fra kobber til plast. Derfor er dette standardmetoden i strømningsprogrammer, CFD.

*På skjermen:* Tittel «Endelig volum-metoden» (oransje). To kolonner: «Endelige differanser: tilnærm u′, u″ i punkter» (punkter på et gitter) og «Endelig volum: bevaring i celler» (rektangler med piler inn og ut). Tre grønne haker spretter inn: «bevaring innebygd ✓», «vilkårlig geometri ✓» (et skjevt gitter rundt en vingeprofil), «hopp i materialet ✓» (to farger på en stav).

### 2. Bevaringsloven for en celle (0:40–1:20)

> **[Du:** hold opp kjeksen eller sukkerbiten: «Dette er en celle.»**]**
> Se på én celle. Størrelsen vi følger med på kaller vi phi – det kan være temperatur, et stoff eller bevegelsesmengde.
> Phi kan endre seg på tre måter: den kan føres med strømmen, den kan spre seg fra høyt til lavt – diffusjon – og den kan produseres inni cellen, av en kilde.
> Her ser vi på det enkleste tilfellet: ren diffusjon, og ingen endring i tid. Da sier loven bare: fluks inn gjennom overflaten pluss produksjon inni er null.

*På skjermen:* En grå firkant (cellen). Piler: blå bølgende pil («føres med strømmen»), rød pil fra varmt til kaldt («diffusjon, −Γ∇φ»), en gul stjerne inni («kilde S»). Blå pil strekes ut med et lite «pff». Grønn boks: «∮ n̂·(Γ∇φ) dS + ∭ S dV = 0», under: «fluks inn + produksjon = 0».

### 3. Celler i 1D: noder og flater (1:20–1:55)

> I én dimensjon blir cellene små biter av en stav. Midt i hver celle har vi en *node* – der vi skal finne verdien. Grensene mellom cellene kaller vi *flater*, og de ligger midt mellom nodene.
> Vi ser på én node, P. Naboen i vest heter W, og naboen i øst heter E. Flatene imellom heter liten w og liten e.

*På skjermen:* En stav tegnes, deles opp i fem celler med stiplede flater (svisj for hvert snitt). Prikker midt i cellene. Én celle lyser grått: P, med W og E på hver side, og w og e på flatene. Et lite kompass «V–Ø» øverst.

### 4. Tilnærm fluksen (1:55–2:40)

> Integrerer vi over cellen, står det bare: fluksen ut gjennom e minus fluksen inn gjennom w, pluss kilden, er null.
> Men fluksen trenger vi på *flatene*, og vi kjenner bare verdiene i *nodene*. Løsningen er så enkel som den kan bli: trekk en rett linje mellom to noder. Stigningstallet er phi E minus phi P, delt på avstanden.
> Setter vi det inn og samler phi P på venstre side, får vi EVM-ligningen: a P phi P er lik a W phi W pluss a E phi E pluss en kilde. a-ene er rett og slett *ledningsevner*: hvor lett varmen slipper fra P til naboen.

*På skjermen:* Røde fluks-piler over w og e. Rett linje mellom φ_P og φ_E (graf), med stigningstrekant «(φ_E − φ_P)/δx». Brøken flyr inn i formelen med «popp»: «Γ_e A (φ_E − φ_P)/δx − Γ_w A (φ_P − φ_W)/δx + S = 0». Så: grønn sluttboks «a_P φ_P = a_W φ_W + a_E φ_E + S^u», med «a_W = Γ_w A/δx», «a_E = Γ_e A/δx». Liten lapp: «a = ledningsevne».

### 5. Bevaring er innebygd (2:40–3:00)

> Og her er det fine: Fluksen gjennom en flate regnes ut med den samme formelen fra begge sider. Det som går ut av én celle, går nøyaktig inn i neste. Bevaringsloven holder eksakt – uansett hvor grovt gitteret er.

*På skjermen:* Fem celler med like røde piler Q₀–Q₄ over flatene; pilene «hopper» fra celle til celle (pop-pop-pop). Teksten «ut av én = inn i neste» kommer tilbake fra kald start (svisj).

### 6. Randen: den halve cellen (3:00–3:30)

> Ved randen kjenner vi temperaturen. Men avstanden fra den første noden til randen er bare en *halv* celle. Da blir ledningsevnen dobbelt så stor: to Gamma A delt på delta x.
> Vi «klipper koblingen» mot randen og legger den kjente verdien inn som en kilde. Formen på ligningen er den samme.

*På skjermen:* Første celle, randen V med en rød firkant «T_V». Avstandspil «δx/2». En saks klipper koblingen mot randen (lyd: «snipp»). «a_W = 0, S^u = (2ΓA/δx)·φ_V, S_P = −2ΓA/δx» flyr inn i sluttboksen.

### 7. Eksempel: varmeledning i en stav (3:30–4:15)

> En stav er hundre grader i den ene enden og fem hundre i den andre. Vi deler den i fem celler, og kappa A delt på delta x blir hundre.
> Fem ligninger, fem ukjente – og matrisen er tridiagonal, fordi hver celle bare snakker med de to naboene sine.
> Løser vi den, får vi hundre og førti, to hundre og tjue, tre hundre, tre hundre og åtti og fire hundre og seksti grader. Akkurat den eksakte løsningen – en rett linje.

*På skjermen:* Stav med «100 °C» (blå) og «500 °C» (rød), fem celler. «κA/δx = (1000 · 0.01)/0.1 = 100». Matrisen bygges rad for rad (pop per rad): diagonal 300, 200, 200, 200, 300 og −100 ved siden av; høyreside 20 000, 0, 0, 0, 100 000. Cellene fargelegges fra blått til rødt, og tallene 140, 220, 300, 380, 460 dukker opp i cellene. En rett linje tegnes gjennom punktene: «= eksakt ✓» (pling).

### 8. Avslutning (4:15–4:30)

> Endelig volum i fire steg: Del i celler. Integrer over hver celle. Tilnærm fluksene på flatene. Løs ligningssystemet. Prøv deg på noen oppgaver!

*På skjermen:* Fire nummererte steg med små ikoner (saks, integraltegn, rett linje, matrise). Sluttboksen står igjen.

---

**Tall (regnet i Python):** κA/δx = 1000 · 0.01/0.1 = 100; randceller a_P = 100 + 200 = 300, S^u = 200 · T_V = 20 000 og 200 · T_H = 100 000. Løsningen: T = 140, 220, 300, 380, 460 °C.
