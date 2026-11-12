# Manus: Hva er en PDE?

**Tema: Partielle differensialligninger · undertema: Introduksjon til PDE-er · ca. 3 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.1)
**Format:** animert Dashman nede til høyre, bare stemmen din. Les sitatblokkene; **[Dashman: …]** og *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md` (kartet, faste farger, formler som bygges). Gangen er alltid fra det generelle til det konkrete.

Tre idéer: (1) den ukjente er en funksjon av flere variabler, (2) tre typer – avgjort av a² − 4b (egenverdiene til koeffisientmatrisen) – som oppfører seg helt ulikt, (3) uten rand- og initialbetingelser er det uendelig mange løsninger.

---

### 0. Kald start (ca. 6 s)
*Kartet:* lyser på «PDE».

> En kopp kaffe blir kald. En gitarstreng svinger. En metallplate får fast temperatur. Tre helt forskjellige ting – og alle er partielle differensialligninger.

**[Dashman: noytral_kopp → blåser på koppen → overrasket]**
*På skjermen:* Tre små ruter som spretter inn (pop, pop, pop): en kaffekopp med damp som blir svakere, en streng som svinger, en plate med fargeskala fra rødt til blått.

### 1. En funksjon av flere variabler (0:00–0:40)
*Kartet:* lyser på «PDE».

> I en ordinær differensialligning er den ukjente en funksjon av én variabel, for eksempel tiden.
> I en *partiell* differensialligning avhenger den ukjente av flere variabler på en gang. Temperaturen u i en stav avhenger både av hvor og når du måler.

> Da får vi *partielle* deriverte: hvordan u endrer seg når bare tiden endres, u t, eller når bare posisjonen endres, u x – og deriverer vi én gang til, u x x.
> En PDE er rett og slett en ligning som binder u og de partielle deriverte sammen. *Hvilke* deriverte som er med, bestemmer hva slags fysikk ligningen beskriver.

**[Dashman: peker_tavla]**
*På skjermen:* (generelt → konkret)
1. Tittel «Hva er en PDE?» (oransje). Generelt først: «ODE: y(t)» – én akse, én kurve. Ved siden av: «PDE: u(x, t)» – to akser, og den turkise u-en (den ukjente) får to små piler ut til «x» og «t» (pop, pop). Merkelapp: «flere variabler».
2. Så det konkrete: en stav som er rød i midten og blå i endene. Over den grafen u(x) ved én tid; en klokke tikker og grafen flater ut. Grafene for flere tider stables bakover og blir en flate u(x, t) som vris litt i perspektiv (svisj).
3. De partielle deriverte bygges fra figuren: fra klokka flyr «∂u/∂t» ut og blir til «u_t» (lapp: «bare t endres»); fra helningen på grafen (en liten tangent) flyr «∂u/∂x» ut og blir til «u_x» (lapp: «bare x endres»); en liten bue over toppen gir «u_xx» (lapp: «deriverer én gang til»). De tre symbolene legger seg i en rad.
4. Generelt: grønn boks «F(x, t, u, u_t, u_x, u_xx, …) = 0» – symbolene fra raden flyr inn i parentesen (popp, popp, popp). Lapp under: «en PDE: en ligning mellom u og de partielle deriverte». Tre grå ligninger (uten navn) svever forbi med et «?» – de får navn i neste del.

### 2. Tre familier (0:40–1:55)
*Kartet:* lyser på «type».

> En andreordens PDE i to variabler kan skrives som u x x, pluss a ganger u x y, pluss b ganger u y y, er lik noe som er av lavere orden. Det er bare tallene a og b foran de andrederiverte som bestemmer *typen*.
> Regn ut a i andre minus fire b. Er det negativt, er ligningen *elliptisk*. Er det null, er den *parabolsk*. Er det positivt, er den *hyperbolsk*.
> Navnene kommer fra kjeglesnittene: x i andre pluss a x y pluss b y i andre lik én er en ellipse, en parabel eller en hyperbel – etter akkurat det samme fortegnet. Og det er det samme som å se på egenverdiene til koeffisientmatrisen foran de andrederiverte: like fortegn gir elliptisk, en null gir parabolsk, motsatte fortegn gir hyperbolsk.
> Typen bestemmer hvordan løsningen oppfører seg. Laplace-ligningen, u x x pluss u y y lik null, er elliptisk. Den beskriver *likevekt* – temperaturen i en plate etter lang, lang tid.
> Varmeligningen er parabolsk. Den *jevner ut*: topper synker, daler fylles.
> Og bølgeligningen er hyperbolsk. Den *frakter* ting av gårde: en puls deler seg i to og løper hver sin vei uten å bli mindre.

**[Dashman: skrive → gruble (ved «a i andre minus fire b») → lyspaere (ved kjeglesnittene) → mystisk (ved Laplace) → undrende (ved varme) → lattermild (ved «løper hver sin vei»)]**
*På skjermen:* (generelt → konkret)
1. **Den generelle formen:** «u_xx + a·u_xy + b·u_yy = (lavere orden)», der a og b er gule. Lapp: «bare a og b bestemmer typen».
2. **Kriteriet:** a og b flyr ned i «a² − 4b» i grønn boks. Under vokser et tre med tre greiner (svisj): «< 0 → elliptisk», «= 0 → parabolsk», «> 0 → hyperbolsk».
3. **Hvorfor navnene:** ved hver grein tegnes kjeglesnittet «x² + axy + by² = 1» – en ellipse, en parabel og en hyperbel (strekene tegnes fram). Liten lapp ved siden av: matrisen «[1, a/2; a/2, b]» med egenverdiene som to små piler: begge samme vei (elliptisk), én null (parabolsk), motsatt vei (hyperbolsk).
4. **Konkret:** hver grein får sitt eksempel, formelen flyr inn og a og b leses av (popp). Animasjon i løkke under, og et nøkkelord som stempel (i denne delen har familiene hver sin farge: Laplace kritt, varme rød, bølge lilla):
   - **Elliptisk – Laplace:** «u_xx + u_yy = 0» → «a = 0, b = 1, a² − 4b = −4». En firkantet plate med varm venstrekant der fargene legger seg i ro. Stempel: «LIKEVEKT».
   - **Parabolsk – varme:** «u_t = u_xx ⇔ u_xx − u_t = 0» → «ingen u_tt: a = b = 0, a² − 4b = 0». En tagget kurve som glattes ut. Stempel: «JEVNER UT».
   - **Hyperbolsk – bølge:** «u_tt = c²u_xx ⇔ u_xx − (1/c²)u_tt = 0» → «b = −1/c², a² − 4b = 4/c² > 0». En pukkel som deler seg i to og løper ut til hver side. Stempel: «FRAKTER».
5. Til slutt står bare de tre nøkkelordene igjen under treet, med ellipse, parabel og hyperbel som små ikoner.

### 3. Rand- og initialbetingelser (1:55–2:45)
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

### 4. Avslutning (2:45–3:00)
*Kartet:* lyser på «hele kartet (første halvdel lyser)».

> En PDE: en ukjent funksjon av flere variabler, tre familier med helt ulik oppførsel, og betingelser som plukker ut den ene løsningen. Prøv deg på noen oppgaver!

**[Dashman: tada]**
*På skjermen:* De tre kolonnene som små ikoner, og ramma med initial- og randbetingelser. Fysikkhjelp-logoen.

---

**Tall:** Laplace (x, y): a = 0, b = 1 → a² − 4b = −4 < 0. Varme u_xx − u_t = 0 i (x, t): a = b = 0 → 0. Bølge u_xx − (1/c²)u_tt = 0: a = 0, b = −1/c² → 4/c² > 0. Koeffisientmatrisen [1, a/2; a/2, b] har determinant b − a²/4 = −(a² − 4b)/4, så fortegnet til a² − 4b avgjør om egenverdiene har like fortegn (elliptisk), en er null (parabolsk) eller motsatte fortegn (hyperbolsk). Samme kriterium som i kompendiet (oppsummeringen «Klassifisering av 2.ordens PDE»).
