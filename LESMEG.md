# Videoer – Realfagsambassaden

Manus og animasjoner til videoene på fysikkhjelp.no og matematikkhjelp.no. Hver lærestoff-side får én video på 2–3 minutter (maks 5). Videoene lages i **videochatten** (instruks i prosjektdokumentet `claude/instruks-videochat.md`), ikke av nattjobben.

Ingenting i dette repoet vises direkte på nettsidene. Videoene lastes opp til YouTube og legges inn på sidene i fagrepoene.

## Mapper

```
_verktoy/                  felles: lag.js, fonter, tavlebakgrunn, logo
ferdige.yml                register over ferdige videoer: <fag>/<mappe> → YouTube-lenke
fysikk-forkurs/            én mappe per fag (samme navn som fagrepoet)
  01-hva-er-fysikk/        én mappe per side: manus.md, anim.html, bilder til animasjonen
  01-02-overslag/
ingeniorfysikk/            (når det kommer videoer der)
```

Mappenavnet er `<kapittelnr>-<sidenr>-<sidenavn>`, f.eks. `07-02-konstant-akselerasjon` for side `kapitler/07-…/02-konstant-akselerasjon.qmd`. Første side i kapittel 1 heter bare `01-hva-er-fysikk`.

## Arbeidsflyt

1. **Nattjobben** lager siden i fagrepoet og legger inn en plassholder der videoen skal stå:
   ```
   <!-- video: kommer (videoer/<fag>/<mappe>) -->
   ![Video kommer](../../bilder/video-kommer.png){fig-alt="Video kommer"}
   ```
2. **Videochatten** lager manus sammen med læreren. Læreren kan redigere `manus.md` selv i VS Code (se under). Når manus er godkjent, lages animasjonen og en ferdig `.mp4` uten lyd, som sendes til læreren. `.mp4` lagres ikke i git.
3. **Læreren** leser inn manuset og står selv i bildet **nede i høyre hjørne**, og laster opp til YouTube. Sonen fra x = 1300 og y = 420 i et 1920×1080-bilde (ca. nederste høyre tredjedel) er alltid tom i animasjonen.
4. **Videochatten** legger lenken inn i `ferdige.yml` (`<fag>/<mappe>: <lenke>`).
5. **Nattjobben** bytter plassholderen (begge linjene) ut med `{{< video <lenke> >}}` på siden. Først da vises videoen.

## Redigere manus i VS Code

1. Klon repoet én gang: Cmd+Shift+P → **Git: Clone** → `https://github.com/Realfagsambassaden/videoer`.
2. Hent siste versjon før du begynner (synk-pilene nederst til venstre).
3. Rediger `<fag>/<mappe>/manus.md`. Cmd+K V gir forhåndsvisning.
4. Lagre, skriv en melding i Source Control, **Commit** og **Sync Changes**.
5. Si fra i videochatten at manus er klart.

## Lage videoen

Krever Node med Playwright (Chromium) og ffmpeg. Kjøres fra roten av repoet:

```
node _verktoy/lag.js fysikk-forkurs/01-hva-er-fysikk preview "0:8,3:38"   # stillbilder med sonen markert, i sjekk/
node _verktoy/lag.js fysikk-forkurs/01-hva-er-fysikk render               # hele videoen
```

## Regler for animasjonen

- 1920×1080, 30 bilder/s. Én scene per avsnitt i manuset, med myk inn- og uttoning (0.4 s).
- Ingenting i presentatørsonen, heller ikke bevegelige ting som passerer gjennom den.
- Farger og skrift som på nettstedet: tavle `#0d1110`, kritt `#ecefe6`, grønn `#6ef04a`, oransje `#f19c2c`, gul `#eee462`, turkis `#56d7b8`. Overskrifter i Montserrat, resten i Comic Neue. Logoen øverst til høyre. (matematikkhjelp.no får sin egen logo og blå aksentfarge når det kommer videoer der.)
- Formler tegnes som bilder med matplotlib (mathtext, `cm`). **Alt i videoen følger [notasjonsreglene](https://github.com/Realfagsambassaden/Plattform/blob/main/NOTASJON.md)**: manus, tekst på skjermen, aksetall og formelbilder. Punktum som desimaltegn (`9.81`, `0.5`), naturkonstanter oppreist (`\mathrm{g}`), g = 9.81 m/s², SI-enheter med dekadiske prefikser (`4.2\ \mathrm{kJ}`), og gjeldende siffer.
- Tidspunktene i `render()` skal følge tidskodene i manuset.
- Se stillbilder av de travleste øyeblikkene før hele videoen lages.

## Lærerens stil

- **Kursnøytrale videoer.** En video skal kunne brukes i flere fag og løyper. Ikke referer til et bestemt kurs, kapittel eller rekkefølge: ikke «i dette kurset/forkurset», «i kapittel 3», «forrige video» eller «neste gang ser vi på …». Det gjelder både manus og tekst på skjermen. Knytt i stedet videoen til emnet (f.eks. «Grunnlag · Hva er fysikk?»). Henvisninger til nettstedet («fysikkhjelp») og til «oppgavene under videoen» er greit.

(Flere faste ønsker for tone, åpning og avslutning noteres her etter hvert.)
