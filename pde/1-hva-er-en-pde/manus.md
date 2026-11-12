# Manus: Hva er en PDE?

**Tema: Partielle differensialligninger · undertema: Introduksjon til PDE-er · ca. 2.5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.1)
**Format:** animert Dashman nede til høyre, bare stemmen din. Les sitatblokkene; **[Dashman: …]** og *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md` (kartet, faste farger, formler som bygges). Gangen er alltid fra det generelle til det konkrete.

Tre idéer: (1) den ukjente er en funksjon av flere variabler, (2) tre familier av ligninger oppfører seg helt ulikt, (3) uten rand- og initialbetingelser er det uendelig mange løsninger.

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

> Da får vi to slags deriverte: hvor fort temperaturen endrer seg i tid, u t, og hvordan den endrer seg langs staven, u x x. En PDE er en ligning som binder dem sammen.

**[Dashman: peker_tavla]**
*På skjermen:* (generelt → konkret)
1. Tittel «Hva er en PDE?» (oransje). Generelt først: «ODE: y(t)» – én akse, én kurve. Ved siden av: «PDE: u(x, t)» – to akser, og den turkise u-en (den ukjente) får to små piler ut til «x» og «t» (pop, pop). Merkelapp: «flere variabler».
2. Så det konkrete: en stav som er rød i midten og blå i endene. Over den grafen u(x) ved én tid; en klokke tikker og grafen flater ut. Grafene for flere tider stables bakover og blir en flate u(x, t) som vris litt i perspektiv (svisj).
3. Formelen bygges fra figuren: fra klokka flyr «∂u/∂t» ut og blir til «u_t» (lapp: «endring i tid»); fra krumningen på grafen (en liten bue tegnes over toppen) flyr «∂²u/∂x²» ut og blir til «u_xx» (lapp: «krumning langs staven»). De to møtes med et «=» imellom (popp) i grønn boks: «u_t = u_xx». Under boksen, liten: «en PDE binder de partielle deriverte sammen».

### 2. Tre familier (0:40–1:35)
*Kartet:* lyser på «type».

> De viktigste andreordens ligningene finnes i tre familier, og de oppfører seg helt forskjellig.
> Varmeligningen, u t lik u x x, *jevner ut*. Topper synker, daler fylles. Det kalles en parabolsk ligning.
> Bølgeligningen, u t t lik c i andre u x x, *frakter* ting av gårde. En puls deler seg i to og løper hver sin vei uten å bli mindre. Den er hyperbolsk.
> Og Laplace-ligningen, u x x pluss u y y lik null, har ingen tid i det hele tatt. Den beskriver likevekt – temperaturen i en plate etter lang, lang tid. Den er elliptisk.

**[Dashman: undrende → lattermild (ved «løper hver sin vei») → mystisk (ved «ingen tid»)]**
*På skjermen:* Generelt først: et tre som vokser ut fra «andreordens PDE» med tre greiner (svisj): «parabolsk», «hyperbolsk», «elliptisk». Så fylles hver grein med sitt konkrete eksempel, én etter én, med animasjon i løkke (i denne delen har familiene hver sin farge: varme rød, bølge lilla, Laplace kritt):
- **Varme:** formelen flyr inn i greina, «u_t = u_xx». Under: en tagget kurve som glattes ut. Nøkkelord som stempel: «JEVNER UT».
- **Bølge:** «u_tt = c²u_xx» flyr inn. Under: en pukkel som deler seg i to like pukler som løper ut til hver side. Stempel: «FRAKTER».
- **Laplace:** «u_xx + u_yy = 0» flyr inn; «t» står gjennomstreket ved siden av (ingen tid). Under: en firkantet plate med varm venstrekant der fargene legger seg i ro. Stempel: «LIKEVEKT».
Til slutt blir de tre nøkkelordene stående alene under treet.

### 3. Rand- og initialbetingelser (1:35–2:25)
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

### 4. Avslutning (2:25–2:40)
*Kartet:* lyser på «hele kartet (første halvdel lyser)».

> En PDE: en ukjent funksjon av flere variabler, tre familier med helt ulik oppførsel, og betingelser som plukker ut den ene løsningen. Prøv deg på noen oppgaver!

**[Dashman: tada]**
*På skjermen:* De tre kolonnene som små ikoner, og ramma med initial- og randbetingelser. Fysikkhjelp-logoen.

---

**Tall:** ingen utregninger.
