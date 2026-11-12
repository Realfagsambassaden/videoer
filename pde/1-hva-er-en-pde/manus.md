# Manus: Hva er en PDE?

**Tema: Partielle differensialligninger · undertema: Introduksjon til PDE-er · ca. 3 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.1)
**Format:** du på video foran grønnskjerm nede til høyre, tavla bak. Les sitatblokkene (nesten ordrett er greit); **[Du: …]** er ting du gjør, *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md` (kartet, faste farger, formler som bygges). Gangen er alltid fra det generelle til det konkrete.

Tre idéer: (1) den ukjente er en funksjon av flere variabler – ODE mot PDE, (2) orden og lineær: i en lineær ligning legges virkninger sammen, (3) homogen eller med kilde – og bare lineær + homogen gir superposisjon (summen av to løsninger er en løsning). Kvasi-lineær er tatt ut (hører hjemme i «Tre typer»).

**Rekvisitter:** en kaffekopp (gjerne med damp) og en strikk eller et hoppetau (gitarstreng).

**Opptak:** hele filmen tas opp på video (lydopptaket PDE_1_take2 brukes ikke videre). Klassifiseringen og betingelsene er i film 2, `pde/2-tre-typer`.

---

### 0. Kald start (ca. 6 s)
*Kartet:* lyser på «PDE».

> Kaffen min blir kald. En gitarstreng svinger. En metallplate får etter hvert jevn temperatur. Tre helt forskjellige fenomener – men de har faktisk noefelles: De beskrives alle sammen av partielle differensialligninger, altså PDE-er.

**[Du: står med kaffekoppen og blåser på den; ved «gitarstreng» plukker du på en strikk du holder utspent; ved «PDE-er» ser du rett i kamera.]**
*På skjermen:* Tre små ruter som spretter inn (pop, pop, pop): en kaffekopp med damp som blir svakere, en streng som svinger, en plate med fargeskala fra rødt til blått.

### 1. En funksjon av flere variabler (0:00–0:40)
*Kartet:* lyser på «PDE».

> I en ordinær differensialligning er den ukjente en funksjon av én variabel, for eksempel tiden.
> I en *partiell* differensialligning avhenger den ukjente av flere variabler på en gang. Et eksempel er temperaturen, som avhenger både av hvor og når du måler.

> Da får vi *partielle* deriverte: Hvis u(x,t) er størrelsen vi studerer, for eksempel temperatur, så kan jeg se på endringen av u når bare t endrer seg. Det kaller vi u_t, og det er altså den partiellderiverte mhp tid. Tilsvarende kaller vi den partiellderiverte mhp posisjon for u x – og deriverer vi én gang til, skriver vi u x x, altså to ganger derivert med hensyn på x.

> En PDE er rett og slett en ligning som binder u og dens partielle deriverte sammen. Hva slags fysikk ligningen beskriver er bestemt av *hvilke* deriverte som er med.

**[Du: peker på ODE-grafen til venstre ved «én variabel», så på flaten ved «flere variabler». Ved «u t» og «u x» viser du med hånda: først stille hånd som «tikker» (tid), så hånda som glir sidelengs (posisjon).]**
*På skjermen:* (generelt → konkret)
1. Tittel «Hva er en PDE?» (oransje). Generelt først: «ODE: y(t)» – én akse, én kurve. Ved siden av: «PDE: u(x, t)» – to akser, og den turkise u-en (den ukjente) får to små piler ut til «x» og «t» (pop, pop). Merkelapp: «flere variabler».
2. Så det konkrete: en stav som er rød i midten og blå i endene. Over den grafen u(x) ved én tid; en klokke tikker og grafen flater ut. Grafene for flere tider stables bakover og blir en flate u(x, t) som vris litt i perspektiv (svisj).
3. De partielle deriverte bygges fra figuren: fra klokka flyr «∂u/∂t» ut og blir til «u_t» (lapp: «bare t endres»); fra helningen på grafen (en liten tangent) flyr «∂u/∂x» ut og blir til «u_x» (lapp: «bare x endres»); en liten bue over toppen gir «u_xx» (lapp: «deriverer én gang til»). De tre symbolene legger seg i en rad.
4. Generelt: grønn boks «F(x, t, u, u_t, u_x, u_xx, …) = 0» – symbolene fra raden flyr inn i parentesen (popp, popp, popp). Lapp under: «en PDE: en ligning mellom u og de partielle deriverte». Tre grå ligninger (uten navn) svever forbi med et «?» – de får navn i neste del.

### 2. Orden, lineær og homogen – og hvorfor det betyr noe (ca. 1:00–2:30)
*Kartet:* lyser på «PDE».

> Vi sorterer PDE-er etter tre viktige egenskaper. 

> Den første er *orden*: den høyeste deriverte som er med. En viktig PDE er den såkalte varmelikningen, som beskriver varmetransport. Den høyeste deriverte som er med her, er u x x, så likningen er av 2. orden.

> Egenskap nummer to: *linearitet*. Det betyr at u og de deriverte bare står alene, ganget med noe som avhenger av x og t – aldri u i andre, aldri u ganger u x. Hvorfor bryr vi oss om det? Fordi i en lineær ligning legges virkninger sammen: to varmeovner i et rom gir til sammen summen av det hver av dem varmer.

> Egenskap nummer tre: er ligningen *homogen*? Flytt alt som har med u å gjøre over til venstre. Står det null igjen til høyre, er den homogen. Står det en funksjon f der – en kilde, som en varmeovn – er den inhomogen.

> Og her er poenget: Er ligningen både lineær *og* homogen, kan vi legge sammen løsninger fritt. Er u_1 og u_2 løsninger, er u_1 + u_2 også en løsning. Tenk på en stav med to varme flekker: hver flekk flater ut for seg, og begge sammen gjør akkurat summen av de to. Med en kilde går ikke det, for summen ville fått kilden to ganger. Men lineariteten hjelper likevel: finner vi én løsning som tar seg av kilden, får vi alle de andre ved å legge til løsninger av den homogene ligningen.

**[Du: teller på fingrene – én (orden), to (lineær), tre (homogen). Ved «to varmeovner»: en hånd på hver side, som to varmekilder. Ved «to varme flekker»: hendene som to små pukler som synker og brer seg ut. Ved «kilden to ganger»: hold opp to fingre og rist på hodet.]**
*På skjermen:* (generelt → hvorfor → konkret)
1. **Tre merkelapper** øverst, som en sjekkliste: «orden», «lineær», «homogen» (popp, popp, popp). Den som snakkes om, lyser.
2. **Orden:** varmeligningen «u_t = α·u_xx» skrives. Under hvert ledd en liten teller: «1» under u_t, «2» under u_xx. Den største ringes inn i grønt: «orden 2».
3. **Lineær:** to kolonner. Til venstre (grønn hake): «u_t = α·u_xx», «u_xx + u_yy = 0», «u_t = (1 + x²)·u_xx» – koeffisientene er bare x og t. Til høyre (rødt kryss): «u_t + u·u_x = 0» (u ganger u_x lyser rødt), «u_t = u_xx + u²» (u² lyser rødt). Lapp: «u og de deriverte alene, ganget med noe av x og t».
4. **Hvorfor lineær – virkninger legges sammen:** et rom ovenfra med to varmeovner; to varmeflekker (turkis fra den ene, oransje fra den andre) brer seg ut, og den samlede temperaturen tegnes hvit som summen. Lapp: «to årsaker → summen av virkningene».
5. **Superposisjon (lineær + homogen):** en stav med to varme flekker (turkis u₁ og oransje u₂). Hver flater ut for seg (tynne grafer), summen (hvit, tykk) flater ut på samme måte. Formelen bygges: «u₁ løsning», «u₂ løsning» → «u₁ + u₂ løsning» i grønn boks.
6. **Homogen:** en vektskål-figur: venstre side «u_t − α·u_xx», høyre side først «0» (grønn lapp «homogen»), så byttes 0 ut med en gul «f(x, t)» og en liten varmeovn i en stav som gløder (gul lapp «inhomogen: kilde»). Par: «Laplace: ∇²u = 0» og «Poisson: ∇²u = f».
7. **Poenget:** «u₁ + u₂» settes inn i den homogene ligningen: «0 + 0 = 0» med grønn hake. I den inhomogene: høyre side blir «f + f = 2f» med rødt kryss. Grønn boks: «lineær + homogen ⇒ løsninger kan legges sammen». Under, litt mindre: «med kilde: u = (én løsning med kilden) + (løsninger av den homogene)».

### 3. Avslutning (ca. 2:30–2:45)
*Kartet:* lyser på «PDE», og lyset glir videre til «type».

> Så: en PDE er en ligning for en ukjent funksjon av flere variabler. Orden, lineær og homogen er de tre første spørsmålene vi stiller den. Prøv deg på en oppgave!

**[Du: tre fingre igjen ved «tre første spørsmålene», peker ned mot oppgavene ved slutten.]**
*På skjermen:* De tre merkelappene orden · lineær · homogen med haker, og flaten u(x, t). Fysikkhjelp-logoen.

---

**Tall og kilde:** kompendiet/foilene F19 «Lineær, kvasi-lineær og homogen PDE»: lineær = lineær i u og alle deriverte, koeffisienter bare av x, y, …; kvasi-lineær = lineær i de høyeste deriverte; homogen = (ledd i u) = f med f = 0. Lineær: L(u₁ + u₂) = Lu₁ + Lu₂ (virkninger legges sammen: Lu₁ = f₁, Lu₂ = f₂ ⇒ L(u₁ + u₂) = f₁ + f₂). Superposisjon: Lu₁ = Lu₂ = 0 ⇒ L(c₁u₁ + c₂u₂) = 0. Med kilde: L(u₁ + u₂) = 2f ≠ f, men alle løsninger er u = u_p + u_h med Lu_p = f og Lu_h = 0. Eksempler: u_t + u·u_x = 0 (Burgers, ikke-lineær), u_t = u_xx + u² (ikke-lineær kilde), u_xx + u·u_yy = u_x² (kvasi-lineær).
