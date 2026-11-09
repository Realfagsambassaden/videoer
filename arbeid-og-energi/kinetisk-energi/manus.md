# Manus: Kinetisk energi

**Tema: Arbeid og energi · undertema: Kinetisk og potensiell energi · ca. 3 min**
**Brukes på:** (ingen side ennå)

Les i rolig tempo, ca. 140 ord i minuttet. Du filmer deg selv foran grønnskjermen og havner nede til høyre i videoen. Tidskodene er omtrentlige. Animasjonen tilpasses det du faktisk sier og gjør i opptaket. Ta en kort pause mellom avsnittene, og **klapp før du tar noe på nytt**. **[Du:]** er forslag til ting du gjør i bildet.

**Rekvisitter:** ingen. Du «dytter» tegneseriebilen med Dashman på tavla: strekk ut hånda mot venstre og dytt i lufta, så starter bilen ved hånda di og kjører mot venstre. Siden du står nede til høyre, kjører bilen **fra høyre mot venstre**, og fart- og kraftpilene peker også mot venstre.

**Tegning fra deg:** ✓ levert (`tegninger.pdf`: Ben sin stasjon, Dashman som plystrer, bilen, bensinpumpa). Bilen speilvendes så fronten peker mot venstre. Den animeres på tavla (bilen kjører, hjulene går rundt, Dashman reagerer). Alt annet på tavla lager jeg med TikZ/SVG.

Utledningen følger samme idé som i «Potensiell energi»: **arbeid = arealet under en graf**, og arealet er en trekant. Den antar **ikke** konstant kraft eller konstant akselerasjon: W = ∫ F⃗ · dx⃗ = ∫ m v dv, og grafen av mv mot v er en rett linje uansett hvordan kraften varierer.

---

### 0. Kald start: Ben sin stasjon (ca. 5 s, ingen tale)

*På skjermen (lærerens tegning `tegninger.pdf`, se `_verktoy/dashman/`):* Skiltet «BEN SIN STASJON». Dashman står og plystrer (noter som svever opp) mens han fyller bensin på bilen fra pumpa. Plystrelyd og et lite «klunk» når tanken er full. Dashman hopper inn bak rattet – og så skjærer det over til tavla der du dytter bilen i gang (avsnitt 1). Bilen speilvendes så den kjører mot venstre. Teksten på bilsiden byttes ut med en nøytral tekst (f.eks. «FULL TANK!») – se merknad i `_verktoy/dashman/LESMEG.md`.

### 1. Intro (0:00–0:20)

> **[Du:** strekk ut hånda mot venstre og gi Dashman-bilen et kraftig dytt. Den suser av gårde mot venstre.**]**
> Når jeg dytter på bilen, gjør jeg et arbeid. Og arbeid er overføring av energi. Men hvor ble energien av nå?
> Den ligger i bevegelsen. Energi som et legeme har fordi det beveger seg, kaller vi *kinetisk energi*, eller bevegelsesenergi.

*På skjermen:* Dashman-bilen står ved hånda di. Når du dytter, suser den mot venstre med fartsstreker (svisj) og stopper midt på tavla. Tittelen «Kinetisk energi» i oransje og «Arbeid = overføring av energi» under.

### 2. Dashman gir gass (0:20–0:45)

> **[Du:** dytt bilen mot venstre igjen, først forsiktig, så hardere – som om du skyver den i gang.**]**
> Tenk deg at bilen står stille, og så dytter jeg på den. Kraften trenger ikke være konstant. Jeg kan dytte litt, så mye, så litt igjen.
> Arbeidet er kraft ganger strekning, lagt sammen bit for bit: *W er integralet av F d x*.

*På skjermen:* Bilen i ro med v₀ = 0 ved hånda di. Kraftpila F⃗ mot venstre fra hånda, som vokser og krymper i takt med dyttet ditt. Bilen øker farten mot venstre, med en liten oransje strekningsbit dx⃗ under. «W = ∫ F⃗ · dx⃗».

### 3. Newtons 2. lov (0:45–1:10)

> Kraften finner vi fra Newtons andre lov: *F er lik m ganger a*. Og akselerasjonen er hvor fort farten endrer seg: *d v delt på d t*.
> Så et lite triks: Den lille strekningen d x er farten ganger en liten tid, *v d t*.
> Setter vi inn, forsvinner d t, og igjen står *m v d v*.

*På skjermen:* «ΣF⃗ = ma⃗», «a = dv/dt» og «dx = v · dt» (stablede brøker). Så F · dx = m · (dv/dt) · v · dt, der de to dt-ene strykes over med en gul strek («pop»). Igjen står «F · dx = m v dv».

### 4. Arealet under en graf (1:10–1:45)

> Arbeidet er altså integralet av *m v* over v, fra null og opp til farten v. Dette tilsvarer arealet under grafen!
> **[Du:** tegn en skrå linje i lufta med hånda.**]**
> Tegner vi m v mot v – altså mot farten, ikke mot tiden – får vi alltid en rett linje, akkurat som kraften i en fjær. Uansett hvordan jeg dyttet. Arealet er en trekant!
> Areal av trekant er en halv ganger grunnlinje ganger høyde. Grunnlinja er v, høyden er m v. Arbeidet blir *en halv m v i andre*.

*På skjermen:* Aksene «mv» og «v» (med en liten gul lapp: «v, ikke t!»), linja fra 0 til (v, mv). Trekanten fylles grå fra venstre. «Areal av trekant: A = ½ · g · h» med en liten trekant, så g = v og h = mv (oransje). «W = ∫ m v dv = ½ · v · mv = ½mv²» (stablede brøker).

### 5. Kinetisk energi (1:45–2:05)

> Dette arbeidet forsvinner ikke. Det ligger i bevegelsen som kinetisk energi: *E k er lik en halv m v i andre*.
> Og hadde bilen allerede fart da jeg begynte å dytte, er arbeidet lik *endringen* i kinetisk energi.

*På skjermen:* Grønn boks: «Kinetisk energi: E_k = ½mv²». Under, mindre: «W = ½mv² − ½mv₀² = ΔE_k» (stablede brøker).

### 6. «Ok … det ble litt nerdete» – poenget (2:05–2:25)

> **[Du:** senk skuldrene, smil litt flau og se rett i kamera.**]**
> Ok … dette ble kanskje litt nerdete. Klarte du ikke å henge med på integralene? Helt greit! Poenget er dette:
> Dytter du på noe og det får fart, har du gitt det energi. Og den energien er *en halv m v i andre*. Dobbelt så tung – dobbelt så mye energi. Dobbelt så fort – *fire* ganger så mye!

*På skjermen:* Tavla tones ned og utledningen blir uskarp (eller viskelæret sveiper den halvveis bort). En liten Dashman kommer inn og klør seg i hodet med et «?». Så, stort og rent midt på tavla: «Poenget:» og «E_k = ½mv²» (stablet brøk), med to små pilbokser under: «2 × m → 2 × E_k» og «2 × v → 4 × E_k» (den siste i gult, «pop»).

### 7. Et eksempel (2:25–2:45)

> Et eksempel: Dashman kjører i 50 kilometer i timen, og bilen veier ett tonn. Da har den rundt 96 kilojoule. I 100 kilometer i timen: nesten 400. Det er derfor bremselengden øker så mye med farten.

*På skjermen:* m = 1000 kg, v = 50 km/h = 13.9 m/s, E_k = 96 kJ. Så v = 100 km/h = 27.8 m/s, E_k = 390 kJ og «×4!» i gult. Dashman-bilen kjører fortere (lengre fartsstreker).

### 8. Avslutning (2:45–3:05)

> **[Du:** hold hånda opp som en vegg (mot venstre) og «ta imot» bilen når den kommer tilbake.**]**
> For å stoppe bilen må noe gjøre det samme arbeidet, bare motsatt vei. Arbeid gir bevegelsesenergi, og bevegelsesenergi kan gjøre arbeid. Prøv deg på oppgavene under videoen!

*På skjermen:* Bilen kjører mot hånda di og bremser opp (bremsespor, Dashman lener seg framover). Oppsummering: «Arbeid ⇄ kinetisk energi», «E_k = ½mv²» (stablet brøk). Eventuell Dashman-stinger.

---

**Tall (regnet i Python):** 50 km/h = 13.89 m/s → E_k = ½ · 1000 kg · (13.89 m/s)² = 96 450 J ≈ 96 kJ. 100 km/h = 27.78 m/s → 385 800 J ≈ 390 kJ (= 4 × 96 kJ).
