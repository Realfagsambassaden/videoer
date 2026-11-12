# Manus: Tre typer PDE-er – og hvorfor

**Tema: Partielle differensialligninger · undertema: Introduksjon til PDE-er (klassifisering) · ca. 4.5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.1)
**Format:** animert Dashman nede til høyre, bare stemmen din.

**Grafisk språk:** se `pde/LESMEG.md`.

Tre idéer: (1) tre typer – fordi en rotasjon gjør koeffisientmatrisen A diagonal, og informasjonen kan gå i 2, 1 eller 0 retninger, (2) kriteriet a² − 4b kommer fra determinanten, (3) typen bestemmer hvilke rand- og initialbetingelser vi trenger.

**Opptak:** innspilt i PDE_1_take2 (12. november 2026), del 2–4. Klippet: «Vi sa at hvilke deriverte …», «på denne måten kan alle … klassifiseres» og «viktige ligninger i fysikken» er kuttet som gjentakelser, og talen er gjort 8 % raskere (læreren ønsket det). Filmen begynner rett på «De viktigste ligningene i fysikken er av andre orden».

---

### 1. Tre typer – og hvorfor (0:00–2:50)
*Kartet:* lyser på «type».

> Vi sa at *hvilke* deriverte som er med, bestemmer fysikken. Det kan vi gjøre helt presist. De viktigste ligningene i fysikken er av andre orden – den høyeste deriverte er en andrederivert. Og det er nettopp de høyeste deriverte som bestemmer hvordan løsningen oppfører seg.
> En andreordens PDE i to variabler kan skrives som u x x, pluss a ganger u x y, pluss b ganger u y y, er lik noe som er av lavere orden. Leddene med de andrederiverte bestemmer *typen*. Resten spiller ingen rolle.
> Koeffisientene foran de andrederiverte – a og b kan godt være funksjoner av x og y – kan vi samle i en symmetrisk matrise, A. Den sier hvordan ligningen setter de andrederiverte sammen.
> Og en symmetrisk matrise kan alltid gjøres diagonal: Vi dreier koordinatsystemet langs egenvektorene til A. Da forsvinner blandingsleddet, og igjen står bare lambda én ganger u ksi ksi, pluss lambda to ganger u eta eta.
> Nå er det bare tre muligheter. Har egenverdiene like fortegn, får vi Laplace-ligningen. Er én av dem null, får vi varmeligningen. Har de motsatte fortegn, får vi bølgeligningen. Hver andreordens PDE er altså, i de riktige koordinatene, en av disse tre.
> Og forskjellen handler om hvordan *informasjon* beveger seg.
> I bølgeligningen går den langs *to* retninger – en puls deler seg i to og løper hver sin vei. Den er *hyperbolsk*.
> I varmeligningen, u t lik alfa u x x, finnes det bare *én* slik retning: tiden. Og langs staven sprer varmen seg øyeblikkelig – litt overalt med en gang. Den *jevner ut*. Den er *parabolsk*.
> I Laplace-ligningen, u x x pluss u y y pluss u z z lik null, finnes det *ingen* spesiell retning. Hvert punkt kjenner hele området rundt seg – det gir en *likevektstilstand*, for eksempel temperaturen i et materiale etter lang, lang tid. Den er *elliptisk*.
> Men hvordan sjekker vi typen i praksis, uten å dreie noe? Vi trenger bare fortegnene til egenverdiene. Og produktet av egenverdiene er determinanten til A: b minus a i andre over fire.
> Er determinanten positiv, har egenverdiene like fortegn. Er den null, er én av dem null. Er den negativ, har de motsatte fortegn. Ganger vi med minus fire, får vi det kjente kriteriet: a i andre minus fire b. Negativ betyr elliptisk, null betyr parabolsk, positiv betyr hyperbolsk.
> Og de to, én eller null retningene? De er røttene i en andregradsligning – med akkurat den samme diskriminanten.

**[Dashman: skrive → peker_tavla (ved matrisen A) → lyspaere (ved «gjøres diagonal») → gruble (ved «bare tre muligheter») → lattermild (ved «løper hver sin vei») → undrende (ved varme) → mystisk (ved Laplace) → tada (ved «a i andre minus fire b»)]**
*På skjermen:* (generelt → hvorfor → konkret)
0. **Overgangen:** den grønne F-boksen «F(x, t, u, u_t, u_x, u_xx, …) = 0» står øverst. Lappen «hvilke deriverte?» lyser opp. Inni F-parentesen lyser u_xx (og de andre andrederiverte) gult, mens u, u_t og u_x blir grå: «de høyeste deriverte bestemmer». Tre grå ligninger med «?» glir inn til høyre og blir stående og vente – de skal sorteres i treet nedenfor.
1. **Den generelle formen** (F-boksen folder seg ut til): «u_xx + a·u_xy + b·u_yy = (lavere orden)». Andreordensleddene lyser, resten blir grått. Lapp: «bare andreordensleddene bestemmer typen». Liten grå lapp ved a og b: «a(x, y), b(x, y) → typen kan variere fra punkt til punkt».
2. **Matrisen A:** tallene 1, a, b flyr ut av ligningen og inn i «A = [1, a/2; a/2, b]» (popp; a/2 havner på begge sidene av diagonalen). Ved siden av, mindre og grå: Hessematrisen til u, «[u_xx, u_xy; u_xy, u_yy]», og en lapp: «A virker på de andrederiverte – typen avgjøres av A, ikke av u».
3. **Rotasjonen (vektorer):** et x–y-koordinatsystem med et rutenett. To egenvektorer til A tegnes som piler fra origo, vinkelrett på hverandre, med lengde |λ₁| og |λ₂|, og farge etter fortegn (grønn = +, rød = −). Hele koordinatsystemet dreier seg langs pilene (svisj), og aksene får nye navn: ξ og η. Samtidig krymper «a·u_xy» og strykes over, og ligningen blir «λ₁·u_ξξ + λ₂·u_ηη + … = 0». A blir «[λ₁, 0; 0, λ₂]».
4. **Tre muligheter:** tre ruter side om side, hver med de to egenvektor-pilene og sin standardform (skalert så λ-ene blir ±1 eller 0):
   - **like fortegn** (to grønne piler): «u_ξξ + u_ηη = 0» → «Laplace»
   - **én null** (én grønn pil og en prikk): «u_ξξ – (førsteordens ledd) = 0» → «varme»
   - **motsatte fortegn** (én grønn og én rød pil): «u_ξξ − u_ηη = 0» → «bølge»
5. **Informasjon – 2, 1 eller 0 retninger:** i hver rute settes et lysende punkt («en forstyrrelse»), og vi ser hvordan den sprer seg (løkke):
   - **Hyperbolsk – bølge:** to lysende linjer går ut fra punktet i hver sin retning (en V-form i x–t-planet), med endelig fart. En pukkel under deler seg i to og løper ut til sidene. Stempel: «FRAKTER · 2 retninger».
   - **Parabolsk – varme:** én retning, oppover i tid, merket med pil «t». Langs x sprer en svak klokke-kurve seg ut over hele staven på en gang, og blir lavere og bredere. Stempel: «JEVNER UT · 1 retning».
   - **Elliptisk – Laplace:** punktet påvirker hele området; en myk sky av farge brer seg ut i alle retninger samtidig, og en plate med varm venstrekant legger seg i ro. Stempel: «LIKEVEKT · 0 retninger».
6. **Fra egenverdier til kriteriet (bygges trinn for trinn):** matrisen A fra punkt 2 kommer tilbake. «λ₁ · λ₂ = det A» skrives under; determinanten regnes ut i A med kryss-strek (1·b − a/2·a/2) og blir «b − a²/4» (popp). Tre linjer med fortegn: «det A > 0 → like fortegn», «= 0 → én er null», «< 0 → motsatte fortegn», med de små pilparene fra punkt 4 ved siden av. Så ganges det med «· (−4)», som flyr inn fra siden, og «b − a²/4» blir til «a² − 4b» i grønn boks (popp) – fortegnene snus: «< 0 elliptisk · = 0 parabolsk · > 0 hyperbolsk». Til slutt, lite: «m² − a·m + b = 0» med «retningene = røttene, samme diskriminant», og de 2, 1 eller 0 lysende linjene fra punkt 5 blinker én gang. Eksemplene leses av i en liten tabell: Laplace −4, varme 0 (u_t er bare av første orden), bølge 4/c².
(I denne delen har familiene hver sin farge i animasjonene: bølge lilla, varme rød, Laplace kritt.)


### 2. Rand- og initialbetingelser (2:50–4:00)
*Kartet:* lyser på «betingelser».

> Men det er et problem. En PDE har uendelig mange løsninger. For bølgeligningen er f av x minus c t, pluss g av x pluss c t, en løsning *uansett* hvilke funksjoner f og g du velger.
> Det som velger ut den ene riktige løsningen, er betingelsene. *Initialbetingelser* sier hvordan alt er ved start, t lik null. *Randbetingelser* sier hva som skjer på kanten – for eksempel at endene av staven holdes på fast temperatur.
> Og typen bestemmer hva du trenger: Varme og bølger marsjerer fram i tid fra en starttilstand. Laplace trenger randverdier rundt hele området.

**[Dashman: skuldre (ved «uendelig mange») → lyspaere → peker_opp]**
*På skjermen:*
1. Problemet: «u = f(x − ct) + g(x + ct)», der f og g er gule bokser. Formene i boksene byttes raskt (lyd: «brrrt»), og bølgeformene under flimrer forbi. Et stort gult «∞ løsninger».
2. Generelt: et område (grått) med randen tegnet rundt. To merkelapper: «initialbetingelse: hvordan det er ved start» (turkis) og «randbetingelse: hva som skjer på kanten» (oransje).
3. Konkret for varme og bølge: en x–t-ramme. Nederste kant lyser turkis «u(x, 0) = f(x)», sidekantene lyser oransje «u(0, t), u(1, t)». En pil glir oppover gjennom ramma: «marsjer i tid».
4. Konkret for Laplace: en firkant der *hele* randen lyser oransje – «rand rundt hele området». Til slutt krympes «∞» til «1» i grønn boks: «betingelser → én løsning».


### 3. Avslutning (4:00–4:30)
*Kartet:* lyser på «hele kartet (første halvdel lyser)».

> Andreordens PDE-er: tre familier med helt ulik oppførsel, og betingelser som plukker ut den ene løsningen. Prøv deg på noen oppgaver!

**[Dashman: tada]**
*På skjermen:* De tre kolonnene som små ikoner, og ramma med initial- og randbetingelser. Fysikkhjelp-logoen.


**Tall:** Laplace (x, y): a = 0, b = 1 → a² − 4b = −4 < 0. Varme u_t = αu_xx ⇔ u_xx − (1/α)u_t = 0 i (x, t): a = b = 0 → 0 (α = κ/(ρc) > 0). Bølge u_xx − (1/c²)u_tt = 0: a = 0, b = −1/c² → 4/c² > 0. Koeffisientmatrisen [1, a/2; a/2, b] har determinant b − a²/4 = −(a² − 4b)/4, så fortegnet til a² − 4b avgjør om egenverdiene har like fortegn (elliptisk), en er null (parabolsk) eller motsatte fortegn (hyperbolsk). a og b kan være funksjoner av x, y (og for kvasi-lineære ligninger av u, u_x, u_y); da avgjøres typen punktvis – f.eks. Tricomi-ligningen y·u_xx + u_yy = 0 er elliptisk for y > 0 og hyperbolsk for y < 0. Samme kriterium som i kompendiet (oppsummeringen «Klassifisering av 2.ordens PDE»). Karakteristikkene: for u_xx + a·u_xy + b·u_yy har retningene med stigning m = dy/dx (m² − a·m + b = 0) diskriminant a² − 4b. NB: typen avgjøres av egenverdiene til A, ikke Hessematrisen til u (for Laplace har Hessematrisen til enhver løsning spor 0, f.eks. u = xy med egenverdier ±1, men ligningen er elliptisk).

