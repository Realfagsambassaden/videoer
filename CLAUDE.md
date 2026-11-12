# Instruks for Claude: videoverkstedet til Realfagsambassaden

Du hjelper en fysikklærer å lage korte undervisningsvideoer til **fysikkhjelp.no** (og senere matematikkhjelp.no). Du jobber lokalt på lærerens Mac. Svar alltid på norsk (bokmål). Læreren er ikke programmerer: forklar i vanlige ord, og gjør git- og terminalarbeidet for hen.

Les også `LESMEG.md`. Avsnittet **«Lærerens stil»** der inneholder faste ønsker som alltid gjelder. Lærer du noe nytt om hva læreren vil ha, skriv det inn der (og her, hvis det endrer arbeidsgangen), commit og push.

## Hva en video er

- Én video per tema, **ca. 3 minutter** (aldri over 5). Videoene er **kursnøytrale** og kan brukes på flere sider i flere fag.
- Læreren står foran **grønnskjerm**, snakker og gjør ting med rekvisitter. Du lager **tavla** bak: lærerens egne tegninger (og TikZ/animasjon der det er bedre), animert i takt med det læreren sier.
- Den ferdige videoen = animasjonen + læreren (grønnskjermen fjernet) **nede i høyre hjørne** + lyden fra opptaket, med **DrNormann-logoen** i et hjørne hele tiden. Til hver video lager du også et **YouTube-miniatyrbilde** (thumbnail). Læreren laster begge opp til YouTube.
- **Intro og outro skal alltid med, som i Arbeid-videoen men med grønn DrNormann** (lærerens kjennemerke): `python3 _verktoy/intro_gronn.py <Intro.mp4> intro.mp4` (de første 2.2 s av `Intro.mp4` i negativ, «Dr. Normann» farget neongrønn med glød) og `python3 _verktoy/outro_gronn.py <Intro.mp4> outro.mp4` (grønn DrNormann-logo spretter fram på dempet tavle, 2.8 s, tones til svart). `Intro.mp4` ligger i `Filmprosjekt/DrNormann/` på Macen. Rekkefølge: eventuell kald start (morsom bit fra opptaket) → intro → **miniatyrbildet som tittelkort** (ca. 1.6 s) → videoen → eventuell Dashman-stinger → outro. Overganger: `xfade` slideleft inn i introen, kort fade (0.3 s) fra intro til tittelkort, fadeblack til outro. **Intromusikken er alltid `_verktoy/lyd/intro_musikk.wav`** (fra Arbeid-videoen v2, 3.25 s), lagt inn fra introens start og over tittelkortet – ikke lyden fra `Intro.mp4`. **Outroen får `_verktoy/lyd/outro_musikk.wav`** (samme musikk, svakere, tones ut), lagt inn fra starten av outroen.
- **Overganger med lyd:** svisj-lyd ved sceneskift og ved intro/outro (`_verktoy/lyd/svisj.wav`), «boing» når noe fjærer (`boing.wav`), «pop» når bokser dukker opp (`pop.wav`). Mellom delene av tavla brukes et viskelær som sveiper over; inn og ut av introen brukes en kort `xfade` (slideleft/circleopen).
- Sidene på nettstedet ligger i andre repoer (fagrepoene). Der står plassholderen «Video kommer» til videoen er registrert i `ferdige.yml`. En automatisk nattjobb bytter da plassholderen ut med videoen. **Du rører aldri fagrepoene.**

## Mapper

```
CLAUDE.md, LESMEG.md, package.json
ferdige.yml               register: <side-id>: <YouTube-lenke>
_verktoy/                 lag.js (anim.html → mp4), finn_pauser.py, sett_sammen.py, thumbnail.js, fonter, bakgrunn, logoer
<tema>/<video>/           én mappe per video, sortert etter tema-id (fra Plattform/tema.yml)
  manus.md                manus med scener, [Du: …] og «På skjermen»
  tegninger.pdf           lærerens tegninger (vektor-PDF fra iPad)
  anim.html               animasjonen
  tider.json              når hvert avsnitt sies i opptaket (lages fra opptaket)
  *.png / *.svg / formler.py   elementer og formelbilder
  thumbnail.json, thumbnail.jpg  miniatyrbildet (oppsett og ferdig bilde) – person.png (utklipp av læreren) ligger ikke i git
```

Eksempler: `arbeid-og-energi/potensiell-energi/`, `hva-er-fysikk/overslag/`. Tema-id-ene står i <https://github.com/Realfagsambassaden/Plattform/blob/main/tema.yml>. (Vi sier «tema», ikke «emne», fordi «emne» også betyr et kurs.)

**Opptakene lagres ikke i git** (for store). De ligger i en mappe på Macen som læreren gir deg tilgang til, f.eks. `~/Movies/Realfagsambassaden/opptak/`. Spør læreren hvor, og noter stien i «Lærerens stil» i LESMEG.md. Det samme gjelder ferdige `.mp4`-filer: legg dem i `~/Movies/Realfagsambassaden/ferdig/` (eller der læreren vil), ikke i repoet.

## Arbeidsgang

1. **Hent siste versjon** (`git pull`). Nattjobben og andre Claude-økter kan ha endret noe.
2. **Manus.** Les siden/temaet og lærerens tegninger. Skriv `manus.md` etter mønsteret i `arbeid-og-energi/potensiell-energi/manus.md`: tittel og tema, rekvisittliste, scener med omtrentlige tidskoder (`### 2. Navn (0:22–0:44)`), det som skal sies som sitatblokk, **[Du:** …**]** for ting læreren gjør (løfte en ball, trykke sammen en fjær, gå ut …), og *På skjermen:* med hva som skal dukke opp. Ca. 340 ord tale for 3 minutter (140 ord/min) pluss pauser for det læreren gjør. Regn ut alle tall i Python. **Vis manuset og juster til læreren er fornøyd.** Læreren redigerer ofte selv i VS Code. Les fila på nytt før du endrer den.
3. **Læreren tar opp** (se «Opptak» under) og sier fra hvor filen ligger.
4. **Finn tidene:** `python3 _verktoy/finn_pauser.py <opptak>` lister taleavsnitt og pauser. Kople pausene til manusavsnittene (de lengste pausene er sceneskiftene). Har læreren improvisert, hør på opptaket (eller bruk tale-til-tekst hvis det er installert, f.eks. `whisper` – spør før du installerer) og følg det som faktisk sies, ikke manuset. Lagre tidene i `tider.json` i videomappa.
5. **Animasjonen:** lag `anim.html` med scenelengder fra `tider.json`, slik at total lengde = opptakets lengde, og at hver tegning dukker opp når læreren snakker om den (gjerne 0.3–0.5 s før). Se reglene under. Lag stillbilder av de travleste øyeblikkene, se på dem, rett feil, og lag så animasjonen.
6. **Sett sammen:** sjekk først ett bilde med læreren i (`--stillbilde`), juster nøkkel og plassering, og lag så den ferdige videoen. Se «Sette sammen» under. Åpne den for læreren (`open <fil>`).
7. **Miniatyrbilde:** lag `thumbnail.jpg` (se «Miniatyrbilde» under) og vis det for læreren sammen med videoen.
8. **Juster** etter lærerens tilbakemeldinger. Endrer læreren noe i opptaket, kjør steg 4–6 på nytt.
9. **Lagre:** commit og push (`manus.md`, `anim.html`, `tider.json`, elementer, `thumbnail.json`, `thumbnail.jpg`) til `main`. Det er greit her, ingenting i repoet vises på nettsiden.
10. **Når videoen er på YouTube:** sjekk at lenken virker, og registrer den i `ferdige.yml` for **hver side** den skal vises på (se under). Commit og push. Nattjobben legger den ut neste natt.

## Registrere en ferdig video (`ferdige.yml`)

Nøkkelen er **side-id-en fra plassholderen** på siden i fagrepoet, ikke videomappa. Plassholderen ser slik ut: `<!-- video: kommer (videoer/fysikk-forkurs/11-02-potensiell-energi) -->` → nøkkelen er `fysikk-forkurs/11-02-potensiell-energi`. Én video kan registreres på flere sider:

```yaml
videoer:
  fysikk-forkurs/11-02-potensiell-energi: https://www.youtube.com/watch?v=XXXXXXXXXXX
  ingeniorfysikk/04-02-potensiell-energi-og-energibevaring: https://www.youtube.com/watch?v=XXXXXXXXXXX
```

Finn sidene med `grep -rl "video: kommer" kapitler/` i de offentlige fagrepoene på github.com/Realfagsambassaden (eller spør læreren). Skriv også i `manus.md` (øverst, «Brukes på:») hvilke sider videoen er registrert på. Finnes det ingen side ennå, vent med å registrere, men noter videoen i «Status» nederst.

## Klipping (når opptaket har omtak)

Læreren tar ofte ting på nytt og improviserer. Da må opptaket høres gjennom og klippes:

- **Tale til tekst:** I skyøkter virker `sherpa-onnx` (pip) med modellen `sherpa-onnx-whisper-turbo` og `silero_vad.onnx` fra GitHub-releasen `k2-fsa/sherpa-onnx` (`asr-models`). Huggingface er stengt. Se `arbeid-og-energi/potensiell-energi/klipp/` for et eksempel.
- Lag en klippeliste (`klipp/edl.py` → `tider.json`): velg siste, beste tagning av hver setning, stram inn pauser over ca. 0.85 s, men ikke der læreren gjør noe med rekvisitter. Enkeltord kan byttes ut fra et annet sted i opptaket (læreren sier slike ord ekstra til slutt).
- Klipp først fra en mindre proxy for å sette tidene, og hent så bitene i full kvalitet fra originalopptaket på Macen (`ffmpeg -ss … -t …` per bit) til den ferdige videoen.
- **Leppesynk, rest:** Selv med like lange biter hang bildet bittelitt etter i Potensiell energi (opptaket fra Macen har lyden 0.075 s forskjøvet). Vis derfor opptaket **0.08 s tidligere** i `plan.json` (`"opptak": T + 0.08`). Spør læreren om det stemmer.
- **Leppesynk (viktig – feilet i utkast 1 av Potensiell energi og i Arbeid-videoen: bildet hang etter):** Hver bit må ha *nøyaktig* like lang lyd og bilde. Legg start og lengde for hver bit på opptakets bilderutenett (25 bilder/s → hele 0.04 s), kutt med `-frames:v N -t N·0.04` og behold opptakets bildefrekvens (ikke `fps=30` per bit – da rundes hver bit opp med en brøkdel av et bilde, og feilen hoper seg opp til flere tideler mot slutten). Ta lyden fra de samme bitene, kutt til nøyaktig N·1920 samples (48 kHz), og sjekk at total bildelengde = total lydlengde før du setter sammen. Eksempel: `arbeid-og-energi/potensiell-energi/klipp/edl2.json`.
- Kutter du bort biter etter at animasjonen er laget, behold tidene i animasjonen og oversett dem med en tabell (gammel T → ny T), slik `R()` i `anim.mal.html` og `lyd.py` gjør.
- `_verktoy/komponer.py` setter læreren inn med en nøkkel som tåler ujevn grønnfarge, og kan ha læreren stor i midten (kald start) og liten nede til høyre resten av tiden.

## Regler for innholdet

- **Kursnøytralt:** ingen «i dette kurset/forkurset», «kapittel 3», «forrige/neste video» – verken i manus eller på skjermen. Knytt til temaet, f.eks. «Arbeid og energi · Potensiell energi». «fysikkhjelp» og «oppgavene under videoen» er greit.
- **Notasjon** følger <https://github.com/Realfagsambassaden/Plattform/blob/main/NOTASJON.md> (les den). Kort: **punktum som desimaltegn** (9.81, 0.5), naturkonstanter i rett skrift (`\mathrm{g}`), **g = 9.81 m/s²** om ikke annet er oppgitt, SI-enheter med dekadiske prefikser (4.2 kJ, 35 mA), riktige gjeldende siffer. Gjelder manus, tekst på skjermen, aksetall og formelbilder. Muntlig er «ni komma åtte én» greit. Retter du noe fra lærerens tegninger, si fra.
- Skriv eget stoff. Ikke kopier fra lærebøker eller andres videoer.

## Lærerens tegninger

- Tegningene kommer som PDF eksportert fra iPad, med **vektorstreker** og gjennomsiktig bakgrunn. Typisk er det én eller to samlesider (hvordan alt henger sammen) og noen sider der elementene er plukket fra hverandre.
- Gjør om sidene til SVG (`pdftocairo -svg tegninger.pdf side.svg` per side, eller PyMuPDF/pdfplumber for å hente ut strekene enkeltvis). Del opp i elementer etter posisjon, og lagre dem som egne SVG-er i videomappa.
- **Tavla tegnes alltid på nytt** (TikZ, egen SVG eller annet verktøy: rene streker, håndskriftfont, uformelle bokstaver). Lærerens tegninger er **bare inspirasjon** for hva som skal stå der og omtrent hvor – strekene hans brukes ikke direkte. Unntak: Dashman-tegneserier og andre rene figurtegninger som læreren vil ha med som de er. (Uttrekk av iPad-strekene ga prikker og rot i utkast 1 av Potensiell energi.) Ting som læreren gjør med rekvisitter (fjær som presses/strekkes) animeres i takt med opptaket – se på bildene fra opptaket for å finne tidene.
- **Dashman-repertoar:** hovedkilden er repoet `Realfagsambassaden/dashman` (tegninger + animerbar rigg); en kopi ligger i `_verktoy/dashman/` (PDF + PNG, oversikt i `oversikt.jpg` og `LESMEG.md`). Legg nye Dashman-tegninger dit og før dem opp.
- **Tegn fram strekene** i animasjonen (stroke-dashoffset på hver sti, i den rekkefølgen læreren skrev dem), så det ser ut som det skrives på tavla. Fylte flater (som det grå arealet under en graf) kan tones inn eller «fylles» fra venstre.
- Det er greit å gjøre strekene **tykkere**, rydde, flytte elementer, eller bytte ut deler med TikZ/egne SVG-animasjoner der det blir tydeligere eller beveger seg bedre (f.eks. en fjær som faktisk presses sammen, en ball som løftes). Behold lærerens særpreg der det går, og si kort fra om hva du har endret.
- **Tekst** fra tegningene skrives om med håndskriftfonten (se under). Tittelen er oransje.

## Regler for animasjonen

- 1920×1080, 30 bilder/s. Myk inn- og uttoning mellom scener (0.4 s).
- **Presentatørsonen x ≥ 1300 og y ≥ 420 skal alltid være tom** – der står læreren. Det gjelder også ting som beveger seg. Lærerens tegninger har ofte ting nede til høyre; flytt dem.
- Tavlestil: bakgrunn `#0d1110` med `_verktoy/tavle-bakgrunn.webp` svakt (opacity ca. 0.09), kritt `#ecefe6`, grønn `#6ef04a`, oransje `#f19c2c`, gul `#eee462`, turkis `#56d7b8`.
- **Logoer:** DrNormann-logoen (`_verktoy/drnormann-logo.svg`, vektor med glød; `drnormann-logo.png` er samme logo i høy oppløsning, `drnormann-logo-flat.svg` uten glød til lys bakgrunn) står **øverst til høyre gjennom hele videoen**, ca. 90 px høy, med ca. 30 px marg. Fysikkhjelp-logoen (`fh-logo-linje.png`) vises bare i tittelscenen og sluttscenen. Ikke legg annet innhold oppå logoene.
- **Skrift:** håndskriftfonten **Architects Daughter** (samme som nettstedet bruker) for tekst fra tegningene og titler. Ligger den ikke i `_verktoy/`, last ned `ArchitectsDaughter-Regular.ttf` og lisensen `OFL.txt` fra <https://github.com/google/fonts/tree/main/ofl/architectsdaughter> til `_verktoy/`, og commit dem (lisensen tillater det). Comic Neue og Montserrat finnes også i `_verktoy/`.
- `anim.html` definerer `window.S = [[scene-id, sekunder], …]` og en **deterministisk** `window.render(sceneIndeks, t)` (samme t gir samme bilde), og har et skjult element `#sone`. Felles filer hentes med `../../_verktoy/…`. Bruk `hva-er-fysikk/innledning/anim.html` som teknisk mal (men ikke som innholdsmal – den er utdatert).
- Formler: skriv dem helst med håndskriftfonten som tekst (passer til lærerens stil), eller som PNG med matplotlib mathtext (`formler.py` i `hva-er-fysikk/overslag/`).

## Miniatyrbilde (YouTube-thumbnail)

Hver video får et miniatyrbilde i fast mal, laget med `npm run thumbnail -- <videomappe>` fra `thumbnail.json` i videomappa (se kommentaren øverst i `_verktoy/thumbnail.js`). Malen følger lærerens eksempel («ARBEID i fysikken», se `_verktoy/thumbnail-eksempel.png` – se på det før du lager et nytt):

- liten håndskrevet merkelapp øverst til venstre med område/tema (f.eks. «Mekanikk») og grønn strek under
- **stor hvit tittel** (Montserrat Black) og **kort grønn, lysende undertittel**
- **læreren til høyre**, klippet ut fra opptaket med grønn glød rundt (`sett_sammen.py --utklipp <sekund> --opptak … --ut <mappe>/person.png`). Velg et øyeblikk med tydelig ansiktsuttrykk eller gest – gjerne et litt spørrende eller overrasket blikk. Hent ut flere kandidater og vis dem for læreren.
- **nøkkeltegning** nede til venstre (lærerens tegning eller TikZ, gjennomsiktig PNG) og **nøkkelformel** i håndskrift
- DrNormann-logoen nede til høyre, tavlebakgrunn med grønt lys bak læreren

Miniatyrbildene skal være **litt små-spektakulære**: noe som vekker nysgjerrighet. **Er det et eksperiment eller en rekvisitt i videoen, skal det med** – bruk helst et utklipp der læreren holder eller gjør eksperimentet (f.eks. ballen i lufta, fjæra som presses sammen), og la tittel/undertittel spille på det. Hold teksten kort (2–4 ord totalt i undertittelen). Bildet blir 2560×1440 JPG under 2 MB, som YouTube krever. Vis det for læreren; juster etter ønske.

**Eldre videoer (før grønnskjerm):** Læreren har egne forsidebilder (grønne tekstbokser og «Dr. Normann»-sirkel) i Mac-mappene. Nye miniatyrbilder i malen lages ved å klippe læreren (og rekvisitter/andre personer) ut av hans gamle forside med `rembg` (pip; modellene `u2net_human_seg` + `isnet-general-use` lastes fra GitHub). Fjern hvit sirkel, grønne bokser og løse bokstaver. Lagres som `<tema>/<video>/thumbnail.json` + `thumbnail.jpg`, og som `<video>_thumbnail.jpg` ved siden av videoen på Macen. `person_hoyde` gjør brede utklipp (flere personer) mindre; lange titler krympes automatisk til én linje. Andre valg i `thumbnail.json`: `person_hoyre` (skyv personen mot/ut av høyre kant), `tittel_bredde` (bredere tittel som kan dekke en avskåret kant), `undertittel_vinkel` (skrå undertittel), `<br>` i undertittelen, og vektorpil i formelen med U+20D7 (`F\u20d7`). Bilder læreren sender: klipp ut med `rembg` (kun `u2net_human_seg` for personer; legg til `isnet-general-use` for rekvisitter som henger fast i personen), og ton ut kanter der bildet er skåret av.

## Korte videoer (TikTok, Instagram Reels, YouTube Shorts)

Egen serie med egne korte manus, ikke klipp fra de lange videoene: **«Visste du at …?»** og **«Kåffer det?!»** – enkle eksperimenter læreren lett kan gjøre. Idéliste og mal: `korte/ideer.md`. Én mappe per snutt: `korte/<slug>/` (manus.md, klipp/, tekst). Opptak og ferdige filer ligger på Macen, ikke i git.

- **Stående 9:16, 1080×1920, maks 60 s** (helst 30–50 s). Læreren filmer stående med mobilen, i vanlige omgivelser (ingen grønnskjerm).
- **Krok i første 1–2 s** (spørsmålet eller det rare resultatet først). Så eksperimentet (gjerne en gang til i sakte film), så en forklaring på én–to setninger.
- **Teksting som kommer samtidig med talen** (TikTok-stil): ord for ord eller korte biter på 2–4 ord, tidsatt fra tale-til-tekst med ordtider og rettet, med ordet som sies uthevet (f.eks. grønt). Store, tydelige bokstaver i håndskriftfonten med mørk kant, midt i bildet litt under midten, så den ikke dekker eksperimentet. Formler og piler kan sprette inn i tavlestil.
- **DrNormann-logoen** (grønn) synlig hele tiden, og en **peker til fysikkhjelp.no** på slutten («Mer fysikk på fysikkhjelp.no», ca. 3 s), gjerne også liten nederst underveis.
- Ingen lang intro: høyst et kort grønt DrNormann-glimt. Lydeffekter (svisj, pop, boing) som i de lange videoene.
- Kutt hardt: bare det beste forsøket, ingen pauser. Leppesynk-reglene under «Klipping» gjelder også her.

**Verktøy for korte videoer:** `python3 korte/_tiktok/lag.py korte/<slug>` leser `korte/<slug>/klipp.json` (kilder, biter med fra/til/fart/zoom/lyd/utsnitt, teksting og stempler – se kommentaren øverst i `lag.py`) og lager hele snutten (biter → tekstlag med Playwright → lyd med svisj/pop/boing/trombone og ut-musikk → `tmp/<ut>.mp4`). Stillbilder for sjekk: `python3 korte/_tiktok/lag.py korte/<slug> 1,5,10` (→ `tmp/ov_<t>.png`). Kø: legg mappenavn i `korte/_tiktok/ko.txt` og kjør `bash korte/_tiktok/ko.sh`. Liggende kilder: `"utsnitt": "boks"` (bildet på uskarp bakgrunn, `forhold` 1.0 = kvadratisk utsnitt, `skala`/`x`/`y` for innzoom) eller `"utsnitt": <x 0–1>` (stående utsnitt). Videoer fra iPhone med rotasjon håndteres automatisk.
- **Håndskriftfonten mangler synlig ring i «å»** (ringen ligger inni a-en). Bruk `_verktoy/ArchitectsDaughter-Norsk.ttf` (ringen flyttet opp) i alt som skal vise norsk tekst.
- Serien **ArtiFyssik** (Ken og Ben) og eksperimentopptakene klippes til korte videoer uten «Ken & Ben»-tekst. Bruk råopptakene uten innbrent tekst. Oversikt over de ferdige snuttene med forslag til tekst og emneknagger: `korte/oversikt.md`.

## Opptak (råd til læreren)

- **Liggende 16:9, 1080p, 25 eller 30 bilder/s.** Telefon eller kamera på stativ.
- **Grønnskjermen** jevnt belyst, uten skrukker og skygger. Stå et par skritt foran den. Ikke ha på grønne klær eller blanke ting.
- Læreren havner **nede til høyre**, ca. 680 px høy av 1080. Det passer best å filme fra midt på låret eller hofta og opp, med litt luft over hodet. Står læreren midt i bildet, blir hen midt i sonen.
- **God lyd** betyr mest: klype- eller myggmikrofon.
- Ta en kort pause (ca. 1 sekund) mellom manusavsnittene. Det gjør det lettere å finne sceneskiftene.
- **Klapp før du tar noe på nytt.** Da er omtakene lette å finne, og det er den siste tagningen som gjelder. Én opptaksfil per video er best (ikke del opp).
- Tilbakemeldinger på et utkast gis helst med tidskoder fra den ferdige videoen («2:40: …»). Regn om: tid i animasjonen = tid i videoen − (intro + overlapp), se `klipp/sett_sammen2.sh`.
- Rekvisitter skal være godt synlige og ikke grønne.

## Oppsett på Mac (første gang)

Krever Node.js, ffmpeg og Python med matplotlib og Pillow. Sjekk med `node -v`, `ffmpeg -version`, `python3 -c "import matplotlib, PIL"`. Mangler noe, installer med Homebrew (`brew install node ffmpeg`, `pip3 install matplotlib pillow`). **Spør læreren før du installerer.**

```
npm install                          # henter Playwright (står i package.json)
npx playwright install chromium      # nettleseren som tar bildene
```

## Kommandoer

Fra roten av repoet:

```
# 1. Tidene i opptaket
python3 _verktoy/finn_pauser.py ~/Movies/Realfagsambassaden/opptak/potensiell-energi.mov

# 2. Animasjonen (stum)
npm run preview -- arbeid-og-energi/potensiell-energi "0:5,2:20"   # stillbilder med sonen markert → <mappe>/sjekk/
npm run video   -- arbeid-og-energi/potensiell-energi              # → <mappe>/<mappe>.mp4

# 3. Sett sammen med læreren
python3 _verktoy/sett_sammen.py --anim arbeid-og-energi/potensiell-energi/potensiell-energi.mp4 \
    --opptak ~/Movies/Realfagsambassaden/opptak/potensiell-energi.mov \
    --ut ~/Movies/Realfagsambassaden/ferdig/potensiell-energi.png --stillbilde 60     # sjekk ett bilde først
python3 _verktoy/sett_sammen.py --anim … --opptak … --ut ~/Movies/Realfagsambassaden/ferdig/potensiell-energi.mp4

# 4. Miniatyrbilde
python3 _verktoy/sett_sammen.py --opptak ~/Movies/Realfagsambassaden/opptak/potensiell-energi.mov \
    --utklipp 75 --ut arbeid-og-energi/potensiell-energi/person.png
npm run thumbnail -- arbeid-og-energi/potensiell-energi           # → <mappe>/thumbnail.jpg
```

`komponer.py` (brukes ved klipping) demper grønt skjær i håret (despill mot snittet av rød og blå) og krymper alfakanten litt. `sett_sammen.py` måler grønnfargen selv. Juster med `--likhet` (0.10 standard; øk litt ved grønne rester, senk hvis hud eller klær blir gjennomsiktige), `--hoyde` (størrelsen på læreren), `--midt` (vannrett plassering), `--beskjaer` (hvis grønnskjermen ikke dekker hele bildet) og `--forskyv` (tidsforskyvning). Se `python3 _verktoy/sett_sammen.py -h`. Lyden normaliseres til YouTube-nivå.

## Status (6. november 2026)

- **`arbeid-og-energi/potensiell-energi`**: **utkast 5 laget 6. november 2026 – læreren er fornøyd** (kald start uten «wireless GoPro», stablede brøker, outromusikk; utkast 4: «løfter den oppover» kuttet og «løfter den» dubbet inn). Klar for opplasting til YouTube og registrering i `ferdige.yml` når en side har plassholder. Utkast 3 laget 5. november 2026 (intromusikk fra Arbeid v2, leppesynk +0.08 s, vektorpiler, bok i stedet for ball, kutt «e lik» → «lik», «akkurat» hel). Utkast 2 laget 5. november 2026 etter lærerens tilbakemeldinger (grønn intro/outro, leppesynk rettet, tavla for eks. 1 tegnet på nytt med fjær som følger læreren, bølge ved SPJONG, kutt av pauser/snubling). Utkast 1 ferdig 5. november 2026 (4:20, kald start, intro/outro, svisj-overganger, Dashman-stinger). Ferdig fil og miniatyrbilde ligger i lærerens mappe `Filmprosjekt/DrNormann/INGENIØRFYSIKK/MEKANIKK—Ingeniør/Potensiell energi/`. Venter på lærerens tilbakemelding. (Tidligere: manus (utkast) og lærerens tegninger (`tegninger.pdf`, 6 sider: tittel, samleside fjær, elementer fjær, elementer graf, samleside tyngdefelt, elementer tyngdefelt) ligger klare. Neste: læreren går gjennom manus, så opptak, så animasjon. Kjente rettelser fra tegningene: eks. 2 heter «Energi i spiralfjær» på tegningen, men skal være «Energi i tyngdefeltet»; `g` oppreist; integralet med prikkprodukt `∫ F⃗·dx⃗`; ligningene nede til høyre må flyttes ut av sonen. Ingen side på nettstedet har denne videoen ennå (passer på undertemaet *Kinetisk og potensiell energi* i temaet *Arbeid og energi*).)
- **`arbeid-og-energi/kinetisk-energi`**: **ferdig 10. november 2026** (utkast 4 godkjent, lagret som `Energi/Kinetisk energi/kinetisk-energi_ferdig.mp4`). Manus (utkast) skrevet 6. november 2026 – utleder E_k = ½mv² fra arbeid uten å anta konstant akselerasjon (W = ∫F dx = ∫m v dv = arealet under mv–v-grafen = trekant), som i Potensiell energi. Læreren dytter tegneseriebilen på tavla. Dashman i bil (lærerens tegning) kjører på tavla. Venter på lærerens gjennomlesning og opptak.
- **TikTok-rekke (15 snutter) laget 9. november 2026** fra ArtiFyssik, Newtons lover-eksperimentene, ballongen og «Sola på banen» – se `korte/oversikt.md`. Ferdige filer i `Filmprosjekt/ArtiFyssik/TikTok/` på Macen. Neste: rekke med eksamenstips.
- **`arbeid-og-energi/energibevaring`**: **ferdig 10. november 2026 – læreren er fornøyd med utkast 4**, lagret som `Energi/EnergiBevaring/energibevaring.mp4` på Macen (de gamle utkastene er slettet). Utkast 4 laget 10. november 2026 (fartspila starter i ballens midtpunkt, «Da vil» satt sammen av hel «Da» + «vil» med romtone – `klipp/dubb.py`, «Tilsvarende … bevegelsen» kuttet – `klipp/lag_opptak3.sh`, energitap-ballen slippes to ganger, fjærkanon med kula som går opp og ned i oppsummeringen). Utkast 3 laget 9. november 2026 (første 1.5 s kuttet, fjær-sammenpressingen kuttet – `klipp/lag_opptak2.sh`, «vil» dubbet fra «Det vil si» – `klipp/dubb.py`, E_tot-linje, fartspil midt på ballen, turkis/oransje i mgh = ½mv², rottegn over hele uttrykket, tegnet fjær som presses sammen i fjærkanonen, E_mek i slutten). Utkast 2 laget 9. november 2026 etter lærerens tilbakemeldinger (ballen faller med økende fart i løkke, læreren speilvendt og bak tegningene, «Da vil» dubbet inn, fjæra som spretter tatt med, fjærkanonen står stille mellom tegningene, søylene følger kula, startenergi/sum-søyle ved energitap, ∇ synlig, mekanisk energi definert på tavla; klipp oversatt med `KLIPP`/`R()` i `innhold.js`, bygg `anim.html` med `bygg.py`). Utkast 1 laget 9. november 2026 (6:52, fra 19 min opptak `Energi/EnergiBevaring/Meg_Energibevaring.mov` på Macen; kald start med ballen, Dashman i skaterampa (lærerens tegning `_verktoy/dashman/skaterampe`), fjærkanon (`fjaerkanon`), energitap kort, konservative krefter med utledning; «i forkursfysikken og ingeniørfysikken» kuttet). Venter på lærerens tilbakemelding. Mekanikkmappene på Macen ligger nå under `MEKANIKK—Ingeniør/Energi/` (Arbeid, Kinetisk energi, Potensiell energi, EnergiBevaring). **Råopptakene (`Meg*.mov`) til de fire ferdige energivideoene er slettet 10. november 2026** etter lærerens ønske; bare `_arbeidsfiler` (klippede biter) er igjen, så større endringer i opptaket kan ikke gjøres lenger.
- **Animert Dashman i stedet for læreren** (bestemt 12. november 2026): videoer kan lages med Dashman nede i høyre hjørne og bare lærerens stemme (leppesynk fra tale til tekst, poser fra manuset). Starter med EVM-videoene; læreren er med selv der han rekker det. Læreren tegner riggen etter `rigg/SPESIFIKASJON.md` i Dashman-repoet. **Dashman-repo:** alt Dashman-materiale skal ligge i et eget repo ([Realfagsambassaden/dashman](https://github.com/Realfagsambassaden/dashman), opprettet 12. november 2026 – hovedkilden; `_verktoy/dashman/` er en kopi). Lærerens rigg er tegnet og klippet ut (`rigg/deler/`, `rigg/rigg.json`), og en test på 11 s er laget (`rigg/eksempel_test.py`), så andre KI-agenter kan bruke det; det skal være mye Dashman rundt på nettsidene.
- **`endelig-volum/` (matematikk, IMAA3012/IMAx3012):** fire manus skrevet 9. november 2026 til forelesningsvideoer om endelig volum-metoden (1: idéen og 1D, 2: kilder og randbetingelser, 3: 2D, 4: tidsavhengig), bygd på lærerens foiler F23–F26 og `Forelesningsplan_F23-F26_EVM.md` i `Undervisning/IMAA3012/IMAA3012_TeachingMaterial/Forelesningsfoiler/` på Macen. Samme oppsett som ellers (svart tavle, læreren nede til høyre, lydeffekter); det visuelle bærer forklaringen. Venter på lærerens gjennomlesning og opptak.
- **Manus for hele mekanikken** (9. november 2026): `arbeid-og-energi/energibevaring` og `arbeid-og-energi/effekt`, og 22 manus til, ett per undertema i tema-mappene (`kinematikk/`, `sirkelbevegelse/`, `newtons-lover/`, `bevegelsesmengde/`, `statikk/`, `rotasjon/`, `gravitasjon/`, `svingninger/` → `<tema>/<undertema-id>/manus.md`). Læreren leser gjennom og spiller inn. Plassholdere finnes alt for bl.a. `ingeniorfysikk/02-03-skratt-kast`, `fysikk-forkurs/03-06-bevegelse-i-to-dimensjoner`, `ingeniorfysikk/03-02-friksjon-fjaer-trinser`, `ingeniorfysikk/03-05-luftmotstand`, `ingeniorfysikk/05-01…05-03` og `ingeniorfysikk/06-04-statisk-likevekt`.
- **Korte videoer (TikTok/Instagram):** serien «Visste du at …?» / «Kåffer det?!» startet 6. november 2026. Idéliste med 10 eksperimenter i `korte/ideer.md`. Manus: `korte/mynten`, `korte/tennisballen`, `korte/vannbotta`, `korte/sugekoppen`, `korte/glasset-opp-ned`, `korte/gyroskopet` (lærerens rekvisitter: sugekopp, gyroskop-hjul). Venter på opptak.
- **Miniatyrbilder for de eldre mekanikkvideoene** (17 stk., i malen) laget 5. november 2026. «Hva er fysikk», «Hva er mekanikk» og «Akselerasjon» er laget på nytt fra bilder læreren sendte. Alle ligger som `<video>_thumbnail.jpg` i mappene på Macen. Merkelappen er «Mekanikk» på alle (bestemt 6. november 2026). Flere bruker samme bilde av læreren (brun skjorte); bedre øyeblikk kan hentes fra opptakene (`Meg_*.mov`).
- **På vent:** `hva-er-fysikk/innledning` og `hva-er-fysikk/overslag` (laget før grønnskjerm-arbeidsgangen; animasjonene er utdaterte). Læreren avgjør etter omstruktureringen av forkurset om de trengs. Plassholderne for dem står på sidene `fysikk-forkurs/01-hva-er-fysikk` og `fysikk-forkurs/01-02-overslag`.
- Videoen om **arbeid** som brukes i temateksten for *Arbeid og energi* er <https://www.youtube.com/watch?v=RDi3DD0Cehk>. Potensiell energi bygger videre på den (men uten å vise til den).
