# Manus: Rand- og initialbetingelser

**Tema: Partielle differensialligninger · undertema: Introduksjon til PDE-er (betingelser) · ca. 5 min**
**Brukes på:** (ingen side ennå – kompendiet IMAx3012 §3.1)
**Format:** du på video foran grønnskjerm nede til høyre, tavla bak. Les sitatblokkene (nesten ordrett er greit); **[Du: …]** er ting du gjør, *På skjermen* er for meg.

**Grafisk språk:** se `pde/LESMEG.md`.

Tre idéer: (1) en PDE har uendelig mange løsninger – betingelser plukker ut den ene, (2) typen og ordenen bestemmer hvilke og hvor mange betingelser (orden i tid = antall initialbetingelser, én randbetingelse i hver ende), (3) tre slags randbetingelser: Dirichlet, Neumann og Robin. Skilt ut fra «Tre typer PDE-er» 20. november 2026.

**Rekvisitter:** slinkyen eller et tau (gitarstreng), gjerne en kopp og et skjerf/en vott (isolasjon).

---

### 0. Kald start: uendelig mange løsninger (0:00–0:35)
*Kartet:* lyser på «betingelser».

> Andreordens PDE-er kommer i tre typer: hyperbolske, parabolske og elliptiske. Men ett problem gjenstår. En PDE har uendelig mange løsninger. For bølgeligningen er f av x minus c t, pluss g av x pluss c t, en løsning *uansett* hvilke funksjoner f og g du velger, så lenge de er to ganger deriverbare.
> Så... hvilken av de uendelig mange løsningene er riktig beskrivelse av akkurat det ingeniørproblemet du forsøker å løse?

**[Du: plukk på slinkyen og la den svinge; trekk på skuldrene ved «uendelig mange»; spør rett i kamera ved «akkurat det ingeniørproblemet».]**
*På skjermen:* Tittel «Rand- og initialbetingelser» (oransje). Tre små ruter med de tre typene (lilla bølge, rød varme, kritt Laplace) glir inn øverst og krymper. Så «u = f(x − ct) + g(x + ct)», der f og g er gule bokser. Formene i boksene byttes raskt (lyd: «brrrt»), og bølgeformene under flimrer forbi. Et stort gult «∞ løsninger». Ved «to ganger deriverbare»: en liten grå lapp «f, g: to ganger deriverbare». Ved «ingeniørproblemet»: et stort gult «?» over en bro eller et rør.

### 1. To klasser betingelser (0:35–0:55)

> Svaret ligger i ekstra betingelser. Vi deler disse i to viktige klasser: *Initialbetingelser* sier hvordan alt er ved start, t lik null. *Randbetingelser* sier hva som skjer på randen, altså kanten. For eksempel at utslaget i endene av gitarstrengen alltid er null.

**[Du: vis «start» med en hånd som slipper noe; vis endene på gitarstrengen med de to hendene (fast i begge ender).]**
*På skjermen:* Et område (grått) med randen tegnet rundt. To merkelapper: «initialbetingelse: hvordan det er ved start, t = 0» (turkis) og «randbetingelse: hva som skjer på kanten» (oransje). Så en gitarstreng mellom to fester, endene oransje: «u = 0 i endene».

### 2. Hvilke og hvor mange? (0:55–3:45)

> Og typen til PDEen bestemmer hva du trenger: Varme og bølger marsjerer fram i tid fra en starttilstand, så de trenger initialbetingelser – i tillegg til randbetingelser. Varmeligningen er av første orden i tid, så den trenger bare starttemperaturen. Bølgeligningen er av andre orden i tid, så den trenger to: både formen og farten på strengen ved start. Hvorfor er antallet initialbetingelser avhengig av ordenen til den tidsderiverte? Jo, fordi hvis du må integrere én gang i tid, så får du én integrasjonskonstant som må bestemmes av initialverdiene. Og hvis du må integrere to ganger for å finne løsningen – ja, så får du to integrasjonskonstanter som må bestemmes. (Her er «konstantene» egentlig hele funksjoner av x: én verdi for hvert punkt på staven eller strengen.) Akkurat som for ordinære differensiallikninger, med andre ord.

> Men varmelikningen og bølgelikningen inneholder også romlige deriverte. For å bestemme en entydig løsning trenger vi derfor ikke bare initialbetingelser, men også betingelser på den romlige randen – såkalte randbetingelser.

> Eksempel med varmelikningen: Se for deg en stav det går varme i, for eksempel et varmeelement i et tørkeskap. Der vil temperaturen utvikle seg med tiden. Da må jeg vite temperaturen i staven i starten for å bestemme hvordan den utvikler seg i tid. I tillegg, på grunn av romlige deriverte, trenger jeg randbetingelser: Jeg må vite hva som skjer på randa, for eksempel hva temperaturen er i endene.

> Eksempel med bølgelikningen: En gitarstreng som vibrerer. Jeg må vite både utslaget og farten i starten for å si noe om hvordan det utvikler seg over tid. Jeg skal ikke bare finne ut hvordan ett punkt utvikler seg over tid, men hvordan en hel streng med punkter interagerer og utvikler seg over tid. Jeg har med andre ord også romlige deriverte. Derfor trenger jeg også randbetingelser: informasjon om oppførselen ved randen.

> Til slutt: Elliptiske ligninger, som Laplace og Poisson, har ingen tidsutvikling. Kun romlige deriverte. Her trenger vi derfor kun randbetingelser. 

> For staven, eller gitarstrengen, så vi at vi trengte to randbetingelser: en på hver ende. Dette fordi det var en andrederivert i x. Vi kan også merke oss at disse to punktene utgjør hele randen. Og dette gjelder også i høyere dimensjoner: Skal vi få nøyaktig én løsning – en såkalt velstilt løsning – så trenger vi randbetingelser på hele randen. 

**[Du: ett finger for varme, to fingre for bølge; ved «integrere to ganger»: to fingre igjen; ved «en på hver ende»: én hånd i hver ende; ved «velstilt»: tommel opp.]**
*På skjermen:*
1. Konkret for varme og bølge: en x–t-ramme. Nederste kant lyser turkis «u(x, 0) = f(x)», sidekantene lyser oransje «u(0, t), u(L, t)». En pil glir oppover gjennom ramma: «marsjerer i tid».
2. En liten tabell bygges: «varme: u_t → 1. orden i tid → 1 initialbetingelse: u(x, 0)» · «bølge: u_tt → 2. orden i tid → 2: u(x, 0) og u_t(x, 0)». Ved «integrere»: «∫ dt → 1 konstant», «∫∫ dt dt → 2 konstanter». Lapp: «orden i tid = antall initialbetingelser».
3. Ved tørkeskapet: en stav (varmeelement) med temperaturprofil – bunnen turkis «starttemperatur», endene oransje. Ved gitarstrengen: strengen med startform og små fartspiler (turkis), festene oransje. Ved «andrederivert i x»: «u_xx → én betingelse i hver ende».
4. Konkret for Laplace: en firkant der *hele* randen lyser oransje – «rand rundt hele området».
5. Telleren: «∞» krymper til «1» i grønn boks: «riktige betingelser → én løsning». Til sidene: «for få → mange løsninger» (gult) og «for mange → ingen løsning» (rødt). Stempel: «VELSTILT».

### 3. Tre slags randbetingelser (3:45–4:40)

> Og heeeelt til slutt, bare så dere har hørt om det: Vi snakker gjerne om tre typer randbetingelser. 

> Hvis du vet verdien av den ukjente på randen, så snakker vi om et *Dirichlet*-randverdiproblem. For eksempel en ende som holdes på hundre grader. Hvis det derimot er den romlige deriverte av den ukjente som er informasjonen du har på randen, ja, så kaller vi det et *Neumann*-randverdiproblem. For eksempel en isolert ende, der ingen varme slipper ut: Da er den deriverte null. Hvis det du vet er en blanding av de to, så kaller vi det et *Robin*-randverdiproblem. Et eksempel kan være en ende som taper varme til lufta rundt: jo varmere enden er, jo mer varme strømmer ut. Det er Newtons avkjølingslov.

**[Du: vis staven med hendene; ved «isolert»: pakk inn hånda i et skjerf eller en vott; ved Robin: blås på hånda (varme ut i lufta).]**
*På skjermen:* En stav i likevekt, varmet fra venstre (rød → blå), med et lite varmeelement (tørkeskap) til venstre og termometre i begge ender: «Dirichlet: u = verdi på randen» (oransje). Så den høyre enden pakket inn i isolasjon, med en pil for varmestrøm og «0»: «Neumann: u_x = verdi (strømmen ut)». Til slutt en ende med små bølgete piler ut i lufta, og pilene blir større når enden blir varmere: «Robin: −k·u_x = h·(u − u_luft)». De tre merkelappene blir stående side om side.

### 4. Avslutning (4:40–5:00)
*Kartet:* lyser på «betingelser».

> Alright! Deriverte i tid betyr at vi trenger initialverdier – like mange som ordenen. Er det romlige deriverte der i tillegg, trenger vi også randverdier. Lett som en plett. And now it's time to shut up and calculate!

**[Du: ett finger ved «initialverdier», to ved «randverdier»; blunk ved «Lett som en plett».]**
*På skjermen:* Staven med de tre betingelsene markert (turkis bunn «u(x, 0) = f(x)», oransje venstre ende «u = 100 °C», isolert høyre ende «u_x = 0»), og temperaturprofilen som utvikler seg i tid mot likevekt. Grønn boks: «1 + 2 betingelser → én løsning». Fysikkhjelp-logoen.

---

**Tall:** Bølgeligningen u_tt = c²·u_xx har d'Alemberts løsning u = f(x − ct) + g(x + ct) for alle to ganger deriverbare f, g. Antall initialbetingelser = orden i tid (varme: u(x, 0); bølge: u(x, 0) og u_t(x, 0)); andre orden i x gir én randbetingelse i hver ende. Randbetingelser: Dirichlet u = g, Neumann ∂u/∂n = g, Robin αu + β∂u/∂n = g (Newtons avkjølingslov: −k·∂u/∂n = h·(u − u_omg)). Velstilt (Hadamard): løsningen finnes, er entydig og avhenger kontinuerlig av dataene. Eksempelet: u_t = α·u_xx på 0 < x < L, u(x, 0) = f(x), u(0, t) = 100 °C, u_x(L, t) = 0 – går mot u = 100 °C overalt.
