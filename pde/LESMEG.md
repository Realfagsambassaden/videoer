# PDE-videoene (matematikk)

Fire korte filmer til PDE-delen (kompendiet IMAx3012, kapittel 3), med **animert Dashman** nede i høyre hjørne og bare lærerens stemme. Én film dekker høyst ett delkapittel, men noen samler flere, og hver film har høyst tre idéer.

| Film | Delkapittel | Idéer |
|---|---|---|
| `1-hva-er-en-pde` | 3.1 Introduksjon til PDE-er | ukjent funksjon av flere variabler · tre familier (likevekt, utjevning, bølge) · rand- og initialbetingelser |
| `2-endelige-differanser` | 3.3 Endelige differanser | derivert → differanse · randverdiproblem → ligningssystem · marsjere i tid: eksplisitt og implisitt skjema |
| `3-endelig-volum` | 3.2, 3.4, 3.5 Bevaringslover og EVM i 1D | bevaringsloven · bevaring i hver celle · randen og kilder |
| `4-endelig-volum-2d-og-tid` | 3.6, 3.7 (og 3.8) EVM i 2D og i tid | fire naboer · eksplisitt tidsskjema · tidssteget ved randen |

**Målet er alltid HVORFOR:** kort, men hver regel og hvert kriterium får en forklaring på hvorfor (vektet gjennomsnitt → r ≤ ½, halv avstand → dobbel ledningsevne, rotasjon → tre typer …).

## Grafisk språk (felles for alle fire filmene)

**Fra det generelle til det konkrete.** Hver film og hver del går samme vei: først idéen i generell form (ord + formel), så en figur som viser hva den betyr, og til slutt et konkret eksempel med tall. Kald start er bare en kort krok; selve forklaringen starter alltid generelt.

**Kartet (flytdiagram).** Øverst til venstre i starten av hver film, og kort mellom delene, vises et lite kart over hele PDE-delen. Boksen vi er i, lyser; resten er dempet. Ved hvert delskifte glir lyset videre (svisj):

```
PDE  ──►  type: varme · bølge · Laplace  ──►  betingelser: initial · rand
  │
  └──►  numerisk metode ──►  endelige differanser ──►  RVP: ligningssystem
                         │                        └──►  tid: eksplisitt · implisitt
                         └──►  endelig volum ──►  bevaring i cellen ──►  1D · 2D · tid
```

**Faste farger** (samme betydning i alle filmene og i formlene):

| Farge | Betyr |
|---|---|
| kritt (hvit) | kjente verdier, tekst |
| turkis `#56d7b8` | ukjente som skal finnes (U_i, T_P), initialbetingelser |
| oransje `#f19c2c` | randen og randbetingelser, titler |
| rød `#e0573d` | fluks / varme som strømmer |
| gul `#eee462` | kilder (S), viktige lapper og advarsler (r ≤ ½) |
| grønn `#6ef04a` | resultatet, bokser med det som skal huskes |

**Formler bygges, de dukker ikke bare opp.** Ledd flyr inn fra figuren der de kommer fra (stigningen fra grafen, fluksen fra pila, randverdien fra veggen) med «popp», ledd som forsvinner strykes over, og den ferdige formelen havner i en grønn boks. Hvert symbol får fargen til begrepet det står for.

**Hvert nytt begrep** (node, flate, fluks, stensil, eksplisitt, implisitt …) dukker opp som en liten merkelapp ved figuren i det øyeblikket det sies, og blir stående litt.

**Innlesing:** Les bare sitatblokkene. **[Dashman: …]** sier hva figuren gjør; det trenger du ikke tenke på. Ta en kort pause mellom avsnittene, og klapp før du tar noe på nytt. Én lydfil per film. God mikrofon er alt som trengs, ingen grønnskjerm.

Posituren til Dashman (fra riggen i `Realfagsambassaden/dashman`): `noytral`, `noytral_kopp`, `peker_tavla`, `peker_opp`, `armer_opp`, `tada`, `undrende`, `mystisk`, `lattermild`, `hoho`, `skuldre`, `gruble`, `overrasket`, `skrive`, og ekstra `lyspaere`, `svette`, `spm`, `utrop`.
