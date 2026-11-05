# Instruks for Claude: videoverkstedet til Realfagsambassaden

Du hjelper en fysikklærer å lage korte undervisningsvideoer til **fysikkhjelp.no** (og senere matematikkhjelp.no). Du jobber lokalt på lærerens Mac. Svar alltid på norsk (bokmål). Læreren er ikke programmerer: forklar i vanlige ord, og gjør git- og terminalarbeidet for hen.

Les også `LESMEG.md`. Avsnittet **«Lærerens stil»** der inneholder faste ønsker som alltid gjelder. Lærer du noe nytt om hva læreren vil ha, skriv det inn der (og her, hvis det endrer arbeidsgangen), commit og push.

## Hva en video er

- Én video per tema, **ca. 3 minutter** (aldri over 5). Videoene er **kursnøytrale** og kan brukes på flere sider i flere fag.
- Læreren står foran **grønnskjerm**, snakker og gjør ting med rekvisitter. Du lager **tavla** bak: lærerens egne tegninger (og TikZ/animasjon der det er bedre), animert i takt med det læreren sier.
- Den ferdige videoen = animasjonen + læreren (grønnskjermen fjernet) **nede i høyre hjørne** + lyden fra opptaket, med **DrNormann-logoen** i et hjørne hele tiden. Til hver video lager du også et **YouTube-miniatyrbilde** (thumbnail). Læreren laster begge opp til YouTube.
- **Intro og outro skal alltid med:** DrNormann-introen (`Intro.mp4`) og outroen (`Interlude.mp4`) ligger i mappa `DrNormann` på Macen (iCloud: `Filmprosjekt/DrNormann/`). Begge vises i negativ (mørk tavle, `negate` i ffmpeg). Outroen kuttes ved 2.6 s (der den blir svart) og tones ut. Rekkefølge: eventuell kald start (morsom bit fra opptaket) → intro → tittelkort → videoen → eventuell Dashman-stinger → outro.
- **Overganger med lyd:** svisj-lyd ved sceneskift og ved intro/outro (`_verktoy/lyd/svisj.wav`), «boing» når noe fjærer (`boing.wav`), «pop» når bokser dukker opp (`pop.wav`). Mellom delene av tavla brukes et viskelær som sveiper over; inn og ut av introen brukes en kort `xfade` (slideleft/circleopen).
- Sidene på nettstedet ligger i andre repoer (fagrepoene). Der står plassholderen «Video kommer» til videoen er registrert i `ferdige.yml`. En automatisk nattjobb bytter da plassholderen ut med videoen. **Du rører aldri fagrepoene.**

## Mapper

```
CLAUDE.md, LESMEG.md, package.json
ferdige.yml               register: <side-id>: <YouTube-lenke>
_verktoy/                 lag.js (anim.html → mp4), finn_pauser.py, sett_sammen.py, thumbnail.js, fonter, bakgrunn, logoer
<emne>/<video>/           én mappe per video, sortert etter emne-id (fra Plattform/emner.yml)
  manus.md                manus med scener, [Du: …] og «På skjermen»
  tegninger.pdf           lærerens tegninger (vektor-PDF fra iPad)
  anim.html               animasjonen
  tider.json              når hvert avsnitt sies i opptaket (lages fra opptaket)
  *.png / *.svg / formler.py   elementer og formelbilder
  thumbnail.json, thumbnail.jpg  miniatyrbildet (oppsett og ferdig bilde) – person.png (utklipp av læreren) ligger ikke i git
```

Eksempler: `arbeid-og-energi/potensiell-energi/`, `hva-er-fysikk/overslag/`. Emne-id-ene står i <https://github.com/Realfagsambassaden/Plattform/blob/main/emner.yml>.

**Opptakene lagres ikke i git** (for store). De ligger i en mappe på Macen som læreren gir deg tilgang til, f.eks. `~/Movies/Realfagsambassaden/opptak/`. Spør læreren hvor, og noter stien i «Lærerens stil» i LESMEG.md. Det samme gjelder ferdige `.mp4`-filer: legg dem i `~/Movies/Realfagsambassaden/ferdig/` (eller der læreren vil), ikke i repoet.

## Arbeidsgang

1. **Hent siste versjon** (`git pull`). Nattjobben og andre Claude-økter kan ha endret noe.
2. **Manus.** Les siden/temaet og lærerens tegninger. Skriv `manus.md` etter mønsteret i `arbeid-og-energi/potensiell-energi/manus.md`: tittel og emne, rekvisittliste, scener med omtrentlige tidskoder (`### 2. Navn (0:22–0:44)`), det som skal sies som sitatblokk, **[Du:** …**]** for ting læreren gjør (løfte en ball, trykke sammen en fjær, gå ut …), og *På skjermen:* med hva som skal dukke opp. Ca. 340 ord tale for 3 minutter (140 ord/min) pluss pauser for det læreren gjør. Regn ut alle tall i Python. **Vis manuset og juster til læreren er fornøyd.** Læreren redigerer ofte selv i VS Code. Les fila på nytt før du endrer den.
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
- `_verktoy/komponer.py` setter læreren inn med en nøkkel som tåler ujevn grønnfarge, og kan ha læreren stor i midten (kald start) og liten nede til høyre resten av tiden.

## Regler for innholdet

- **Kursnøytralt:** ingen «i dette kurset/forkurset», «kapittel 3», «forrige/neste video» – verken i manus eller på skjermen. Knytt til emnet, f.eks. «Arbeid og energi · Potensiell energi». «fysikkhjelp» og «oppgavene under videoen» er greit.
- **Notasjon** følger <https://github.com/Realfagsambassaden/Plattform/blob/main/NOTASJON.md> (les den). Kort: **punktum som desimaltegn** (9.81, 0.5), naturkonstanter i rett skrift (`\mathrm{g}`), **g = 9.81 m/s²** om ikke annet er oppgitt, SI-enheter med dekadiske prefikser (4.2 kJ, 35 mA), riktige gjeldende siffer. Gjelder manus, tekst på skjermen, aksetall og formelbilder. Muntlig er «ni komma åtte én» greit. Retter du noe fra lærerens tegninger, si fra.
- Skriv eget stoff. Ikke kopier fra lærebøker eller andres videoer.

## Lærerens tegninger

- Tegningene kommer som PDF eksportert fra iPad, med **vektorstreker** og gjennomsiktig bakgrunn. Typisk er det én eller to samlesider (hvordan alt henger sammen) og noen sider der elementene er plukket fra hverandre.
- Gjør om sidene til SVG (`pdftocairo -svg tegninger.pdf side.svg` per side, eller PyMuPDF/pdfplumber for å hente ut strekene enkeltvis). Del opp i elementer etter posisjon, og lagre dem som egne SVG-er i videomappa.
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

- liten håndskrevet merkelapp øverst til venstre med område/emne (f.eks. «Mekanikk») og grønn strek under
- **stor hvit tittel** (Montserrat Black) og **kort grønn, lysende undertittel**
- **læreren til høyre**, klippet ut fra opptaket med grønn glød rundt (`sett_sammen.py --utklipp <sekund> --opptak … --ut <mappe>/person.png`). Velg et øyeblikk med tydelig ansiktsuttrykk eller gest – gjerne et litt spørrende eller overrasket blikk. Hent ut flere kandidater og vis dem for læreren.
- **nøkkeltegning** nede til venstre (lærerens tegning eller TikZ, gjennomsiktig PNG) og **nøkkelformel** i håndskrift
- DrNormann-logoen nede til høyre, tavlebakgrunn med grønt lys bak læreren

Miniatyrbildene skal være **litt små-spektakulære**: noe som vekker nysgjerrighet. **Er det et eksperiment eller en rekvisitt i videoen, skal det med** – bruk helst et utklipp der læreren holder eller gjør eksperimentet (f.eks. ballen i lufta, fjæra som presses sammen), og la tittel/undertittel spille på det. Hold teksten kort (2–4 ord totalt i undertittelen). Bildet blir 2560×1440 JPG under 2 MB, som YouTube krever. Vis det for læreren; juster etter ønske.

## Opptak (råd til læreren)

- **Liggende 16:9, 1080p, 25 eller 30 bilder/s.** Telefon eller kamera på stativ.
- **Grønnskjermen** jevnt belyst, uten skrukker og skygger. Stå et par skritt foran den. Ikke ha på grønne klær eller blanke ting.
- Læreren havner **nede til høyre**, ca. 680 px høy av 1080. Det passer best å filme fra midt på låret eller hofta og opp, med litt luft over hodet. Står læreren midt i bildet, blir hen midt i sonen.
- **God lyd** betyr mest: klype- eller myggmikrofon.
- Ta en kort pause (ca. 1 sekund) mellom manusavsnittene. Det gjør det lettere å finne sceneskiftene.
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

`sett_sammen.py` måler grønnfargen selv. Juster med `--likhet` (0.10 standard; øk litt ved grønne rester, senk hvis hud eller klær blir gjennomsiktige), `--hoyde` (størrelsen på læreren), `--midt` (vannrett plassering), `--beskjaer` (hvis grønnskjermen ikke dekker hele bildet) og `--forskyv` (tidsforskyvning). Se `python3 _verktoy/sett_sammen.py -h`. Lyden normaliseres til YouTube-nivå.

## Status (5. november 2026)

- **`arbeid-og-energi/potensiell-energi`**: **utkast 1 ferdig 5. november 2026** (4:20, kald start, intro/outro, svisj-overganger, Dashman-stinger). Ferdig fil og miniatyrbilde ligger i lærerens mappe `Filmprosjekt/DrNormann/INGENIØRFYSIKK/MEKANIKK—Ingeniør/Potensiell energi/`. Venter på lærerens tilbakemelding. (Tidligere: manus (utkast) og lærerens tegninger (`tegninger.pdf`, 6 sider: tittel, samleside fjær, elementer fjær, elementer graf, samleside tyngdefelt, elementer tyngdefelt) ligger klare. Neste: læreren går gjennom manus, så opptak, så animasjon. Kjente rettelser fra tegningene: eks. 2 heter «Energi i spiralfjær» på tegningen, men skal være «Energi i tyngdefeltet»; `g` oppreist; integralet med prikkprodukt `∫ F⃗·dx⃗`; ligningene nede til høyre må flyttes ut av sonen. Ingen side på nettstedet har denne videoen ennå (passer på delemnet *Kinetisk og potensiell energi* i emnet *Arbeid og energi*).)
- **På vent:** `hva-er-fysikk/innledning` og `hva-er-fysikk/overslag` (laget før grønnskjerm-arbeidsgangen; animasjonene er utdaterte). Læreren avgjør etter omstruktureringen av forkurset om de trengs. Plassholderne for dem står på sidene `fysikk-forkurs/01-hva-er-fysikk` og `fysikk-forkurs/01-02-overslag`.
- Videoen om **arbeid** som brukes i emneteksten for *Arbeid og energi* er <https://www.youtube.com/watch?v=RDi3DD0Cehk>. Potensiell energi bygger videre på den (men uten å vise til den).
