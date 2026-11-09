# TikTok-rekka (15 snutter, november 2026)

Ferdige filer: `Filmprosjekt/ArtiFyssik/TikTok/` på Macen (filnavnet starter med nummeret under). Alle er stående 1080×1920, med DrNormann-logo, teksting ord for ord og sluttkort «Mer fysikk på fysikkhjelp.no». Oppsett per snutt: `korte/<mappe>/klipp.json`, laget med `korte/_tiktok/lag.py`.

| Nr | Mappe | Lengde | Krok (første sekunder) | Forslag til tekst på TikTok | Emneknagger |
|---|---|---|---|---|---|
| 01 | `gjennom-jorda` | 39 s | «Hoppe GJENNOM jorda?» | Hvor lang tid tar det å falle gjennom jorda til Kina? 🌍⬇️ | #fysikk #realfag #lærpåtiktok #jorda |
| 02 | `snurrings` | 21 s | «Hva i alle dager skjedde der?» | Ball + karusell = ??? Corioliseffekten på lekeplassen 🎠⚽ | #fysikk #coriolis #eksperiment |
| 03 | `kopp-opp-ned` | 57 s | «KÅFFER DET?!» | Kan luft holde opp cola? 🥤 | #fysikk #eksperiment #lufttrykk |
| 04 | `male-g` | 59 s | «Er g virkelig 9.81?» | Vi målte tyngdeakselerasjonen med en huske … og ringte vaktmesteren 📞 | #fysikk #pendel #newton |
| 05 | `friksjon` | 32 s | «Kenny har en plan 💡» | Hvor skal Kenny skli neste gang? Kommenter! 👇 | #fysikk #friksjon #ideer |
| 06 | `bottetarnet` | 33 s | «Kan Kenny velte bøttetårnet?» | Fire forsøk og ett tyngdepunkt 🪣💥 | #fysikk #tyngdepunkt #fail |
| 07 | `botter-pa-hodet` | 28 s | «Fysikk-advarsel ⚠️» | Hvis du ikke har skjønt at fysikk er viktig … 🪣🪣 | #fysikk #kødd #studentliv |
| 08 | `gardinen` | 14 s | «POV: Du har endelig skjønt fysikk 😎» | POV: Newtons lover sitter 😎 | #fysikk #pov #newton |
| 09 | `treghetsloven` | 20 s | «Hva skjer når tralla stopper?» | Newtons første lov på en tralle 🛒 | #fysikk #newton #treghet |
| 10 | `treghet-bloopers` | 26 s | «Fysikktime gone wrong 😅» | Bloopers fra treghetsloven 🎬 | #fysikk #bloopers #newton |
| 11 | `tralla-ute` | 27 s | «Newtons 2. lov på en tralle» | ΣF = m·a – og på nynorsk er det dp/dt 🤓 | #fysikk #newton #nynorsk |
| 12 | `tralle-anmeldelse` | 28 s | «Ærlig anmeldelse av tralla» | Treghet: 10/10 ⭐⭐⭐⭐⭐ | #fysikk #anmeldelse #tralle |
| 13 | `sola-pa-banen` | 36 s | «Hvis sola var en ball på Lerkendal» | Hvor på banen skal planetene egentlig ligge? Svar i kommentarene 👇 | #astronomi #solsystemet #rbk |
| 14 | `ballong` | 22 s | «Stikk hull i en vannballong 💦» | Vanntrykket virker vinkelrett på veggen 💦 | #fysikk #trykk #eksperiment |
| 15 | `vaktmesteren` | 28 s | «Fysikere uten målebånd 📏❌» | Når vaktmesteren er italiensk 🇮🇹🤌 | #fysikk #studentliv #humor |

## Råd for publisering

- Legg ut én om dagen, gjerne på ettermiddag eller kveld, og svar på kommentarene den første timen.
- Start med de sterkeste krokene: 01, 06, 09, 13, 02.
- 05 og 13 slutter med et spørsmål til seerne – de er laget for å få kommentarer.
- 3–5 emneknagger holder; de hjelper TikTok å forstå temaet, men gir ikke visninger i seg selv.

## Kjent

- Tekstingen er tidsatt fra tale-til-tekst og rettet for hånd. Utydelige replikker (f.eks. den italienske samtalen) er ikke tekstet.
- Kildestiene i `klipp.json` peker på kopier i skyøkta (`/home/claude/kilder/…`, `/mnt/user-data/uploads/…`). Bytt dem til stiene på Macen (`Filmprosjekt/ArtiFyssik/…`, `Filmprosjekt/DrNormann/…`) før en ny kjøring. Kødd-opptakene og friksjon er snudd 90° med `transpose=1` først (`ArtiFyssik/TikTok/arbeid/kilder/k_*.mov`).
