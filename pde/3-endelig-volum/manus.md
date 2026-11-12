# Manus: Endelig volum – bevaring i hver celle

**Tema: Partielle differensialligninger · undertema: Bevaringslover og endelig volum-metoden i 1D · ca. 3.5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.2, §3.4–3.5)
**Format:** animert Dashman nede til høyre, bare stemmen din. Les sitatblokkene; **[Dashman: …]** og *På skjermen* er for meg.
**Grunnlag:** foilene F23–F24.

**Grafisk språk:** se `pde/LESMEG.md` (kartet, faste farger, formler som bygges). Gangen er alltid fra det generelle til det konkrete.

Tre idéer: (1) bevaringsloven – endring = inn − ut + produksjon, (2) endelig volum skriver den opp for hver celle, og bevaring blir eksakt, (3) randen og kilder går inn i den samme ligningen.

---

### 0. Kald start (ca. 6 s)
*Kartet:* lyser på «endelig volum».

> Det som går ut av én celle, må gå inn i den neste. Det høres opplagt ut – men det er hele hemmeligheten bak metoden som brukes i nesten all strømningsprogramvare.

**[Dashman: noytral_kopp → mystisk]**
*På skjermen:* En rad med fem celler. Røde varmepiler hopper fra celle til celle (pop-pop-pop). «ut av én = inn i neste» spretter inn.

### 1. Bevaringsloven (0:00–0:55)
*Kartet:* lyser på «numerisk metode → endelig volum (fra bevaringsloven)».

> Se på en liten bit av en stav. Varmen i biten kan bare endre seg på tre måter: Den strømmer inn på den ene siden, den strømmer ut på den andre, eller den lages inni biten, av en kilde.
> Endring er lik inn minus ut, pluss produksjon. Det er en bevaringslov.
> Lar vi biten bli uendelig liten, blir det en PDE – for eksempel varmeligningen. Men endelig volum-metoden gjør det motsatte: Den lar bitene være *endelige*, og bruker loven direkte.

**[Dashman: peker_tavla → skrive → lyspaere]**
*På skjermen:* Tittel «Endelig volum» (oransje). En grå celle med en rød pil inn fra venstre «fluks inn», en rød pil ut til høyre «fluks ut», en gul stjerne inni «kilde S». Grønn boks: «endring = inn − ut + produksjon». En pil ned med «δx → 0» til «ρc u_t = (κu_x)_x + S» (grå), og en pil til siden med «δx endelig» til «endelig volum» (grønn).

### 2. Bevaring i hver celle (0:55–2:05)
*Kartet:* lyser på «bevaring i cellen».

> Vi deler staven i celler. Midt i hver celle er en node – der vil vi finne temperaturen. Mellom cellene er flatene.
> Ser vi på én celle, P, med naboene W og E: Fluksen gjennom en flate tilnærmer vi med en rett linje mellom nodene. Varmen går fra varmt til kaldt, så fluksen er ledningsevnen ganger temperaturforskjellen.
> Samler vi alt, får vi én ligning per celle: a P T P er lik a W T W pluss a E T E pluss S u. a-ene er rett og slett ledningsevner – hvor lett varmen slipper over til naboen.
> Og det fine: Fluksen gjennom en flate regnes ut med samme formel fra begge sider. Det som går ut av én celle, går nøyaktig inn i neste. Bevaringen er eksakt – uansett hvor grovt gitteret er.

**[Dashman: peker_tavla → noytral → armer_opp (ved «eksakt»)]**
*På skjermen:* Staven deles i fem celler (svisj for hvert snitt), prikker midt i cellene, stiplede flater. Én celle lyser: W, P, E og flatene w, e. En graf med en rett linje mellom T_P og T_E og stigningen «(T_E − T_P)/δx». Formelen bygges med «popp»: «κA(T_E − T_P)/δx − κA(T_P − T_W)/δx + S = 0» → grønn boks «a_P T_P = a_W T_W + a_E T_E + S^u» med «a = κA/δx» og lappen «a = ledningsevne». Så de fem cellene igjen med like store røde piler over hver flate, som hopper videre: «bevaring: eksakt ✓».

### 3. Randen og kilder (2:05–3:15)
*Kartet:* lyser på «1D (rand og kilder)».

> Ved randen er avstanden fra noden til kanten bare en *halv* celle. Da blir ledningsevnen dobbel. Vi klipper koblingen til randen, og legger den kjente temperaturen inn i S u – og den doble ledningsevnen inn i S P.
> Er det i stedet *fluksen* som er kjent, legger vi den bare inn i S u. En isolert vegg gir ingenting i det hele tatt.
> Og en kilde – for eksempel varme fra strøm – skrives som S u pluss S P ganger T P. S P skal være null eller negativ, ellers kan løsningen stikke av.
> Prøv med en stav som er hundre grader i den ene enden og fem hundre i den andre. Fem celler gir hundre og førti, to hundre og tjue, tre hundre, tre hundre og åtti og fire hundre og seksti grader. Akkurat en rett linje – den eksakte løsningen.

**[Dashman: skrive → skuldre (ved «isolert vegg gir ingenting») → overrasket → tada]**
*På skjermen:* Første celle med randen og «δx/2». En saks klipper koblingen (lyd: «snipp»). Fire skuffer «a_W», «a_E», «S^u», «S_P» – bidragene flyr ned i riktig skuff med pop: «kjent T → S^u og S_P», «kjent fluks → S^u», «isolert → –», «kilde → S^u + S_P T_P, S_P ≤ 0». Så eksempelet: stav med «100 °C» (blå) og «500 °C» (rød), «κA/δx = 100». Matrisen fylles rad for rad (300, 200, 200, 200, 300 på diagonalen, −100 ved siden av; høyreside 20 000, 0, 0, 0, 100 000). Cellene farges fra blått til rødt med 140, 220, 300, 380, 460, og en rett linje går gjennom: «= eksakt ✓» (pling).

### 4. Avslutning (3:15–3:30)
*Kartet:* lyser på «endelig volum (1D)».

> Endelig volum: bevaringsloven, skrevet opp for hver celle. Fluksene på flatene, én ligning per celle, og randen og kildene i de samme skuffene. Prøv deg på noen oppgaver!

**[Dashman: noytral_kopp]**
*På skjermen:* Grønn boks «a_P T_P = Σ a_nb T_nb + S^u, a_P = Σ a_nb − S_P». Fysikkhjelp-logoen.

---

**Tall (regnet i Python):** κA/δx = 1000 · 0.01/0.1 = 100; randceller a_P = 100 + 200 = 300, S^u = 200 · 100 = 20 000 og 200 · 500 = 100 000. Løsning: 140, 220, 300, 380, 460 °C.
