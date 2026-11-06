# Videoer – Realfagsambassaden

Manus, tegninger og animasjoner til videoene på fysikkhjelp.no og matematikkhjelp.no. Videoene lages lokalt på Mac med Claude Code. **Instruksen Claude følger står i [`CLAUDE.md`](CLAUDE.md).** Denne fila er oversikten for mennesker.

Ingenting i dette repoet vises direkte på nettsidene. Videoene lastes opp til YouTube og legges inn på sidene i fagrepoene av en automatisk nattjobb.

## Slik blir en video til

1. **Manus:** Claude skriver manus ut fra siden/temaet og lærerens tegninger. Læreren redigerer i VS Code til det sitter.
2. **Opptak:** Læreren filmer seg selv foran grønnskjerm, snakker etter manus og bruker rekvisittene. Opptaket ligger på Macen, ikke i git.
3. **Animasjon:** Claude finner pausene i opptaket og lager tavla bak (lærerens tegninger tegnes fram, pluss TikZ/animasjon der det er bedre), i takt med det som sies.
4. **Sammensetting:** Claude fjerner grønnskjermen og legger læreren nede til høyre, oppå tavla, med lyden fra opptaket.
5. **YouTube:** Læreren ser gjennom, ber om justeringer, og laster opp.
6. **Registrering:** Lenken legges inn i `ferdige.yml` for hver side videoen skal vises på. Neste natt bytter nattjobben ut «Video kommer» på sidene med videoen.

## Mapper

```
CLAUDE.md              instruksen til Claude (arbeidsgang, regler, kommandoer, status)
ferdige.yml            register: <side-id> → YouTube-lenke
_verktoy/              verktøyene (lag.js, finn_pauser.py, sett_sammen.py) og fonter, bakgrunn, logo
<emne>/<video>/        én mappe per video, sortert etter emne, f.eks. arbeid-og-energi/potensiell-energi/
```

Videoene sorteres etter **emne** (som på nettstedet), ikke etter fag, fordi samme video kan brukes i flere fag.

## Redigere manus i VS Code

1. Klon repoet én gang: Cmd+Shift+P → **Git: Clone** → `https://github.com/Realfagsambassaden/videoer`.
2. Hent siste versjon før du begynner (synk-pilene nederst til venstre).
3. Rediger `<emne>/<video>/manus.md`. Cmd+K V gir forhåndsvisning.
4. Lagre, skriv en melding i Source Control, **Commit** og **Sync Changes**.

## Lærerens stil

Faste ønsker som gjelder alle videoer. Claude fyller på her når læreren sier noe nytt.

- **Kursnøytrale videoer.** En video skal kunne brukes i flere fag og løyper. Ikke referer til et bestemt kurs, kapittel eller rekkefølge: ikke «i dette kurset/forkurset», «i kapittel 3», «forrige video» eller «neste gang ser vi på …». Det gjelder både manus og tekst på skjermen. Knytt i stedet videoen til emnet (f.eks. «Arbeid og energi · Potensiell energi»). Henvisninger til nettstedet («fysikkhjelp») og til «oppgavene under videoen» er greit.
- **Tavla tegnes alltid på nytt** med TikZ/SVG eller lignende, med uformelle bokstaver i håndskriftfonten. Lærerens tegninger er **bare inspirasjon** for hva som skal stå der. Unntak: Dashman-tegneserien og lignende figurer brukes som de er. Finn gjerne et bedre pedagogisk oppsett ut fra det læreren sier.
- **Ting som beveger seg følger læreren:** når læreren presser sammen eller strekker en fjær, presses/strekkes fjæra på tavla i takt, og kraftvektoren vokser. Vis likevektsposisjonen og hva x er.
- **Merkelappen** øverst til venstre på miniatyrbildet er «Mekanikk» for alt som er kinematikk, dynamikk eller statikk (ikke underområdet).
- **Miniatyrbilder:** bruk gjerne bilder læreren sender (med kolleger, rekvisitter, et tydelig blikk) i stedet for de gamle forsidene. Undertittelen skal være kort og vittig, ikke klisjé («spenning garantert» er for dumt); den kan stå på skrå for et «raskere» bilde, og deles på to linjer hvis den ellers havner oppå den grønne gløden rundt læreren. Titler deles aldri med bindestrek (ett ord = én linje, krympes heller). Er et utklipp skåret av mot kanten av bildet (f.eks. toppen av et hode), legg tittelen over kanten eller ton den ut, så det ikke blir åpenbart.
- **Brøker skrives stablet** (teller over vannrett brøkstrek, f.eks. klassen `.brok` i `anim.mal.html`), ikke ½ eller skråstrek.
- **Vektorer har pil** overalt: F⃗, x⃗, h⃗, dx⃗ i integraler (W = ∫ F⃗ · dx⃗). Rekvisitter tegnes som det de er (boka som bok, ikke sirkel).
- **Forklar formler eksplisitt** – studentene trenger mer enn du tror. Skriv f.eks. «Areal av trekant: A = (1 over 2) · g · h» med en liten trekant før man setter inn x og kx.
- **Lydeffekter i takt med det som skjer i bildet** (sjekk opptaket: «SPJONG» når fjæra faktisk slippes). Gjerne en bølge utover hele tavla ved «SPJONG».
- **Tekst** fra tegningene skrives om med håndskriftfonten Architects Daughter (penere enn håndskrift, men samme preg). Tittelen er oransje.
- **Læreren i bildet:** læreren står foran grønnskjerm og havner nede til høyre. Foreslå gjerne rekvisitter og ting læreren gjør (løfter en ball, trykker sammen en fjær, filmer ute …). Skriv det inn i manus som **[Du:** …**]**, med en liste over rekvisitter øverst.
- **DrNormann-logoen** står øverst til høyre gjennom hele videoen. Fysikkhjelp-logoen bare i starten og slutten.
- **Miniatyrbilde** til hver video, etter malen i lærerens eksempel («ARBEID i fysikken»): stor hvit tittel, grønn lysende undertittel, læreren til høyre med grønn glød, nøkkeltegning og formel, DrNormann-logo. Litt små-spektakulært. Er det et eksperiment i videoen, skal det med.
- **Opptaket kommer først**, og animasjonen tilpasses det læreren faktisk sier og gjør.
- **Lengde:** ca. 3 minutter (ca. 340 ord tale + pauser for det læreren gjør).
- **Notasjon** etter [NOTASJON.md](https://github.com/Realfagsambassaden/Plattform/blob/main/NOTASJON.md): punktum som desimaltegn, naturkonstanter i rett skrift, g = 9.81 m/s², SI-enheter med prefikser, gjeldende siffer.
- **Intro og outro som i Arbeid-videoen, men med grønn DrNormann:** kort DrNormann-intro i negativ der «Dr. Normann» er **neongrønn** (som logoen i hjørnet) → miniatyrbildet som tittelkort → videoen → Dashman-stinger hvis det finnes → outro med den grønne DrNormann-logoen på dempet tavle. Grønn «DrNormann» er lærerens kjennemerke. Intromusikken er alltid den fra Arbeid-videoen v2 (`_verktoy/lyd/intro_musikk.wav`), og outroen får samme musikk litt svakere som tones ut (`outro_musikk.wav`). Lages med `_verktoy/intro_gronn.py` og `_verktoy/outro_gronn.py`.
- **Overganger** gjerne med svisj-lyd og litt leken bevegelse (viskelær over tavla, «SPJONG!», «boing»), slik det er vanlig på YouTube.
- **Morsomme øyeblikk** fra opptaket (f.eks. når læreren rigger opp eller tuller litt) kan klippes inn som en kort kald start før introen. Hold den kort og ta bort teknisk prat (f.eks. «trykke på wireless GoPro og greier»).
- **Avslappet, men kort.** Ta med det beste av det læreren sier, kutt omtak, snubling og lange pauser (også kunstige pauser > ca. 1 s og øyeblikk der læreren bare ser inn i kameraet). Behold pauser der læreren gjør noe med rekvisitter.
- **Små ordkutt og dubbing:** fyllord og nølelyder tas bort («e lik k ganger x» → «lik k ganger x»). Ord kan dubbes inn fra et annet sted i opptaket for å få setningen slik læreren vil («gjør det» → «løfter den»). Kutt aldri starten av et ord («kkurat»); sjekk kuttene med tale-til-tekst.
- **Ingen grønnskjær** i håret eller kantene på læreren.
- **Leppesynk må stemme** (se «Klipping» i CLAUDE.md). Læreren merker det med en gang hvis bildet henger etter.
- **Mapper på Macen:** materialet til en video ligger i iCloud under `Filmprosjekt/DrNormann/<FAG>/<OMRÅDE>/<tema>/`, f.eks. `Filmprosjekt/DrNormann/INGENIØRFYSIKK/MEKANIKK—Ingeniør/Potensiell energi/` (opptaket `MEG.mov`, tegningene som PDF). Den ferdige videoen og miniatyrbildet legges i samme mappe.

- **Ting læreren gjør mot tavla skjer der han ser og har hånda:** stopper han bilen eller den krasjer, skal bilen/muren stå rett ved hånda hans (hånda kan godt være bak muren), og han skal se på Dashman – ikke på sin egen hånd. Her er det greit at tavla går inn i presentatørsonen.
- **Innramming:** sjekk at læreren ikke er skåret av mot høyre kant (særlig når opptaket speilvendes). Flytt ham inn (`midt` i `plan.json`), og flytt tavla tilsvarende.
- **Ordslutter:** kutt aldri slutten av et ord eller en setning («… ganger høyden», «… mv i andre»). Sjekk slutten av hver bit med tale-til-tekst.
- **Korte videoer** (TikTok/Instagram/Shorts) har egne manus: enkle «Visste du at …?»- og «Kåffer det?!»-eksperimenter, maks 1 minutt, med DrNormann-logoen og en peker til fysikkhjelp.no. Se «Korte videoer» i CLAUDE.md. Stilen læreren likte («Kopp opp ned», `korte/kopp-opp-ned/`): den mest spektakulære scenen først som krok, plutselige zoom inn/ut og hvite blink med svisj ved kutt, teksting ord for ord, emojier, store stempler («KÅFFER DET?! 🤯», «FAIL 😩»), **bloopers med morsom lyd** (skuffet trombone) og en kort forklaring på hva som gikk galt, forklaringen i fargede bokser, og til slutt svart skjerm med DrNormann-logoen, «Mer fysikk på fysikkhjelp.no» og ut-musikken.

(Flere faste ønsker for tone, åpning og avslutning noteres her etter hvert.)
