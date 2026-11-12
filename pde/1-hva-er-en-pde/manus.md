# Manus: Hva er en PDE?

**Tema: Partielle differensialligninger · undertema: Introduksjon til PDE-er · ca. 2.5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.1)
**Format:** animert Dashman nede til høyre, bare stemmen din. Les sitatblokkene; **[Dashman: …]** og *På skjermen* er for meg.

Tre idéer: (1) den ukjente er en funksjon av flere variabler, (2) tre familier av ligninger oppfører seg helt ulikt, (3) uten rand- og initialbetingelser er det uendelig mange løsninger.

---

### 0. Kald start (ca. 6 s)

> En kopp kaffe blir kald. En gitarstreng svinger. En metallplate får fast temperatur. Tre helt forskjellige ting – og alle er partielle differensialligninger.

**[Dashman: noytral_kopp → blåser på koppen → overrasket]**
*På skjermen:* Tre små ruter som spretter inn (pop, pop, pop): en kaffekopp med damp som blir svakere, en streng som svinger, en plate med fargeskala fra rødt til blått.

### 1. En funksjon av flere variabler (0:00–0:40)

> I en vanlig differensialligning er den ukjente en funksjon av én variabel, for eksempel tiden.
> I en *partiell* differensialligning avhenger den ukjente av flere variabler på en gang. Temperaturen u i en stav avhenger både av hvor du er, x, og når du ser, t.
> Da får vi to slags deriverte: hvor fort temperaturen endrer seg i tid, u t, og hvordan den krummer seg langs staven, u x x. En PDE er en ligning som binder dem sammen.

**[Dashman: peker_tavla]**
*På skjermen:* Tittel «Hva er en PDE?» (oransje). Venstre: «ODE: y(t)» med en enkel kurve. Høyre: en stav som farges rødt i midten og blått i endene; over den en graf u(x) som flater ut mens en klokke tikker – så blir grafen en flate u(x, t) som vris litt i perspektiv (svisj). To piler: «u_t: endring i tid» (turkis) og «u_xx: krumning langs staven» (oransje). Grønn boks: «u_t = u_xx».

### 2. Tre familier (0:40–1:35)

> De viktigste andreordens ligningene finnes i tre familier, og de oppfører seg helt forskjellig.
> Varmeligningen, u t lik u x x, *jevner ut*. Topper synker, daler fylles. Det kalles en parabolsk ligning.
> Bølgeligningen, u t t lik c i andre u x x, *frakter* ting av gårde. En puls deler seg i to og løper hver sin vei uten å bli mindre. Den er hyperbolsk.
> Og Laplace-ligningen, u x x pluss u y y lik null, har ingen tid i det hele tatt. Den beskriver likevekt – temperaturen i en plate etter lang, lang tid. Den er elliptisk.

**[Dashman: undrende → lattermild (ved «løper hver sin vei») → mystisk (ved «ingen tid»)]**
*På skjermen:* Tre kolonner som kommer etter tur, hver med animasjon i løkke:
- **Varme** (rød): en tagget kurve som glattes ut. «u_t = u_xx · parabolsk · jevner ut».
- **Bølge** (turkis): en pukkel som deler seg i to like pukler som løper ut til hver side. «u_tt = c²u_xx · hyperbolsk · frakter».
- **Laplace** (gul): en firkantet plate med varm venstrekant; fargene legger seg i ro. «u_xx + u_yy = 0 · elliptisk · likevekt».
Svisj mellom kolonnene.

### 3. Rand- og initialbetingelser (1:35–2:25)

> Men det er et problem. En PDE har uendelig mange løsninger. For bølgeligningen er f av x minus c t, pluss g av x pluss c t, en løsning *uansett* hvilke funksjoner f og g du velger.
> Det som velger ut den ene riktige løsningen, er betingelsene. *Initialbetingelser* sier hvordan alt er ved start, t lik null. *Randbetingelser* sier hva som skjer på kanten – for eksempel at endene av staven holdes på fast temperatur.
> Og typen bestemmer hva du trenger: Varme og bølger marsjerer fram i tid fra en starttilstand. Laplace trenger randverdier rundt hele området.

**[Dashman: skuldre (ved «uendelig mange») → lyspaere → peker_opp]**
*På skjermen:* Mange forskjellige bølgeformer som flimrer forbi (f og g byttes, lyd: «brrrt»), med «u = f(x − ct) + g(x + ct)» og et stort gult «∞». Så en x–t-ramme: nederste kant lyser turkis «initialbetingelse, t = 0», sidekantene lyser oransje «randbetingelser». Pil oppover: «marsjer i tid». Ved siden av: en firkant der *hele* randen lyser gul – «Laplace: rand rundt hele».

### 4. Avslutning (2:25–2:40)

> En PDE: en ukjent funksjon av flere variabler, tre familier med helt ulik oppførsel, og betingelser som plukker ut den ene løsningen. Prøv deg på noen oppgaver!

**[Dashman: tada]**
*På skjermen:* De tre kolonnene som små ikoner, og ramma med initial- og randbetingelser. Fysikkhjelp-logoen.

---

**Tall:** ingen utregninger.
