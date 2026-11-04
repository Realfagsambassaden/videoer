# Instruks for Claude: videoverkstedet til Realfagsambassaden

Du hjelper en fysikklærer å lage korte undervisningsvideoer til **fysikkhjelp.no** (og senere matematikkhjelp.no). Svar alltid på norsk (bokmål). Læreren er ikke programmerer: forklar i vanlige ord, og gjør git-arbeidet for hen.

Les også `LESMEG.md` i dette repoet. Avsnittet **«Lærerens stil»** der inneholder faste ønsker som alltid gjelder.

## Hva en video er

- Én video per lærestoff-side, **2–3 minutter** (aldri over 5).
- Du skriver **manus** (`manus.md`) og lager en **stum animasjon** i tavlestil (`anim.html` → `.mp4`).
- Læreren leser inn manuset over animasjonen og står selv i bildet **nede i høyre hjørne**. Så laster hen opp til YouTube.
- Sidene på nettstedet ligger i andre repoer (fagrepoene). Der står plassholderen «Video kommer» til videoen er ferdig. En automatisk nattjobb bytter plassholderen ut med videoen når YouTube-lenken står i `ferdige.yml` her. **Du rører aldri fagrepoene.**

## Mapper

```
CLAUDE.md, LESMEG.md
ferdige.yml          register: <fag>/<mappe>: <YouTube-lenke>
_verktoy/            lag.js (lager video fra anim.html), fonter, tavlebakgrunn, logo
fysikk-forkurs/      én mappe per fag (samme navn som fagrepoet på GitHub)
  01-hva-er-fysikk/  én mappe per side: manus.md, anim.html, formelbilder, tegninger
  01-02-overslag/
```

Mappenavn: `<kapittelnr>-<sidenr>-<sidenavn>`, f.eks. `02-01-si-enheter` for side `kapitler/02-…/01-si-enheter.qmd` i fagrepoet `Realfagsambassaden/fysikk-forkurs`. Sidene videoen hører til kan leses på github.com/Realfagsambassaden/fysikk-forkurs (offentlig).

## Arbeidsgang

1. **Hent siste versjon** først (`git pull`). Nattjobben retter av og til notasjon i manusene.
2. **Hva venter?** Plassholderne står i fagrepoet som `<!-- video: kommer (videoer/<fag>/<mappe>) -->`. Sammenlign med mappene her og med `ferdige.yml`. Vis lista: trenger manus / manus klart / venter på innspilling / ferdig.
3. **Manus først.** Les siden videoen hører til. Skriv `manus.md` etter mønsteret i de eksisterende mappene: tittel, varighet, scener med tidskoder (`### 2. Navn (0:14–0:44)`), det som skal sies som sitatblokk, og *På skjermen:* med hva som dukker opp når. 300–400 ord, ca. 140 ord i minuttet, skrevet for å *sies*. Regn ut alle tall i Python. **Vis manuset og juster til læreren er fornøyd før du lager animasjonen.** Læreren redigerer ofte manus selv i VS Code. Les fila på nytt før du endrer den.
4. **Animasjonen** (se regler under). Lag stillbilder av de travleste øyeblikkene først, se på dem, rett feil, og lag så hele videoen.
5. **Lagre:** commit og push til `main`. Det er greit her, fordi ingenting i dette repoet vises på nettsiden. `.mp4`, `scener/` og `sjekk/` skal ikke i git (se `.gitignore`).
6. **Når videoen er på YouTube:** sjekk at lenken virker, legg `<fag>/<mappe>: <lenke>` inn under `videoer:` i `ferdige.yml` (gjør `{}` om til en vanlig liste), commit og push. Nattjobben legger videoen ut på siden neste natt.

## Regler for innholdet

- **Kursnøytralt:** videoen skal kunne brukes i flere fag. Ingen «i dette kurset/forkurset», «kapittel 3», «forrige/neste video» – verken i manus eller på skjermen. Knytt til emnet, f.eks. «Grunnlag · Hva er fysikk?». «fysikkhjelp» og «oppgavene under videoen» er greit.
- **Notasjon** følger <https://github.com/Realfagsambassaden/Plattform/blob/main/NOTASJON.md> (les den). Kort: **punktum som desimaltegn** (9.81, 0.5), naturkonstanter i rett skrift (`\mathrm{g}`), **g = 9.81 m/s²** om ikke annet er oppgitt, SI-enheter med dekadiske prefikser (4.2 kJ, 35 mA), riktige gjeldende siffer. Gjelder manus, tekst på skjermen, aksetall og formelbilder. Muntlig i manus er «ni komma åtte én» greit.
- Skriv eget stoff. Ikke kopier fra lærebøker eller andres videoer.

## Regler for animasjonen

- 1920×1080, 30 bilder/s. Én scene per avsnitt i manuset, myk inn- og uttoning (0.4 s). Tidspunktene følger tidskodene i manuset.
- **Presentatørsonen x ≥ 1300 og y ≥ 420 skal alltid være tom**, også for ting som beveger seg gjennom den.
- Tavlestil: bakgrunn `#0d1110` med `_verktoy/tavle-bakgrunn.webp` svakt (opacity ca. 0.09), kritt `#ecefe6`, grønn `#6ef04a`, oransje `#f19c2c`, gul `#eee462`, turkis `#56d7b8`. Overskrifter i Montserrat, resten i Comic Neue (fontene ligger i `_verktoy/`). Logoen øverst til høyre.
- `anim.html` må definere `window.S = [[scene-id, sekunder], …]` og en **deterministisk** `window.render(sceneIndeks, t)` (samme t gir samme bilde), og ha et skjult element `#sone`. Felles filer hentes med `../../_verktoy/…`. Bruk de eksisterende `anim.html` som mal.
- Formler tegnes som PNG med matplotlib mathtext (`mathtext.fontset = 'cm'`), som i `fysikk-forkurs/01-02-overslag/formler.py`.

## Oppsett på Mac (første gang)

Krever Node.js, ffmpeg og Python med matplotlib. Sjekk med `node -v`, `ffmpeg -version`, `python3 -c "import matplotlib"`. Mangler noe, installer med Homebrew (`brew install node ffmpeg`, `pip3 install matplotlib`). Spør læreren før du installerer.

```
npm install                          # henter Playwright (står i package.json)
npx playwright install chromium      # nettleseren som tar bildene
```

## Lage video

Fra roten av repoet:

```
npm run preview -- fysikk-forkurs/01-02-overslag "0:5,3:20"   # stillbilder med sonen markert → <mappe>/sjekk/
npm run video   -- fysikk-forkurs/01-02-overslag              # hele videoen → <mappe>/<mappe>.mp4
```

(Det samme som `node _verktoy/lag.js <mappe> preview "…"` og `node _verktoy/lag.js <mappe> render`.) Se alltid på stillbildene før du lager hele videoen. Åpne den ferdige videoen for læreren (`open <fil>.mp4`).

## Status (4. november 2026)

- `fysikk-forkurs/01-hva-er-fysikk` og `fysikk-forkurs/01-02-overslag`: manus finnes og er rettet (notasjon v2, kursnøytralt). Læreren går gjennom manusene. **Animasjonene er utdaterte** (viser desimalkomma, g ≈ 9,8 og «Forkurs i fysikk · Kapittel 1» / kapittelliste) og må lages på nytt når manusene er godkjent. Formelbildene (`f*.png`) må også lages på nytt.
- Nye sider kommer hver natt i `Realfagsambassaden/fysikk-forkurs`, med plassholder for video.
