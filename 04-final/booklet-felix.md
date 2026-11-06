# Booklet · Teil Felix: Box und Bedienfeld

Stand 06.11. nach der ersten Arbeitssitzung (2 h). Das Booklet ist **umgesetzt** als gemeinsames HTML-Booklet im Grünton: [`booklet.html`](booklet.html) (13 Seiten, davon S. 07–13 von Felix). Diese Datei ist nur noch der **Arbeitsstand zu Felix' Seiten**: was steht, was offen ist, was wegfällt. Der Plan für das Gesamt-Booklet (17 Seiten, Treffen am 07.11.) steht in [`booklet-plan.md`](booklet-plan.md), Begründungen mit Folien in [`entscheidungen-folien.md`](entscheidungen-folien.md) (E1–E31).

Begriff: **Seite** = Booklet-Seite, **Folie** = Vorlesungsfolie.

## Felix' Seiten im Gesamt-Booklet

| Jetzt | Plan | Seite | Status |
|---|---|---|---|
| 07 | 03 | **Für wen: Ingrid, 72.** Wer macht was, Persona (Hassenzahl), Leitideen A/B/C | ✅ umgesetzt · *veränderbar später* |
| – | 04 | **Konzeptweg V1 → V3** (Box und Oberfläche) mit Abwägungstabelle | 🆕 neu, siehe `booklet-plan.md` |
| 08 | 10 | **Wie eine Mikrowelle.** Skizze V3 annotiert 1–5, Technik | ✅ umgesetzt · Einstieg kürzen (Mikrowelle steht schon auf S. 02) |
| 09 | 11 | **Ein Taster. Eine Bedeutung.** Vorher/Nachher + Abwägung 1 | ✅ umgesetzt · hängt an Taster vs. Schiebeschalter |
| 10 | 12 | **Ein Blick. Eine Aussage.** Startbild annotiert, drei Zustände | ✅ umgesetzt |
| 11 | 13 | **Warum Blau statt Schwarz?** Abwägung 2 | ✅ umgesetzt |
| – | 14 | **Die erste Woche:** auspacken → Sorte wählen → Tag 1 → nachfüllen → ernten | 🆕 neu |
| 12 | 15 | **Eine Warnung. Ein Knopf.** Case 1 Tank leer, Case 2 Ernte | ✅ umgesetzt · *veränderbar später* |
| 13 | 16 | **Die Hürde passt zum Risiko.** 2 s halten, „Sicher?“, Eigene Sorte | ✅ umgesetzt · *veränderbar später* |
| – | 17 | **Abwägungen Bedienfeld** (Abwägung 3) | 🆕 neu, Stoff unten |

Bilder: Display-Zustände als echte Screenshots von Bedienfeld v7 in `bilder/booklet/`, Box-Skizzen aus `02-box-bau/bilder/`.

## Bausteine für die neuen Seiten

### S. 04 Konzeptweg: Auftrag und Vorgehen

- **Auftrag** (Folie 5, Option B): Bedienoberfläche für eine Growbox. Daraus wurde eine kleine Box für Pilze, bedient **am Gerät** (Display + Taster) und **aus der Ferne** (App).
- **Vorgehen** nach Double Diamond und User Centered Design (Folie 104–107):

```
Verstehen          Konzept              Prototyp                   Prüfen
Personas      →    3 Leitideen     →    Box V1 → V3            →   Nielsen-Check,
Box ↔ Mensch       Wahl: B              Bedienfeld v1 → v7         Farbsimulation,
                   „Radikal einfach“    (Papier → Klick-Prototyp)  Präsentation
```

- **Konzept auf einen Blick** (früher Seite 1, als Text für Titel oder S. 04):

| | |
|---|---|
| **Konzept** | Eine Pilz-Growbox, die das Klima selbst regelt und am Gerät **radikal einfach** bedient wird: ein großer Zustand, drei Kacheln, ein Taster. Die App ist ein Zusatz. |
| **Ziel** | Jeder erkennt mit einem Blick, ob etwas zu tun ist, und erledigt die drei Aufgaben ohne Anleitung. |
| **Zielgruppe** | Alle Altersgruppen; Maßstab ist der schwächste Nutzer (Persona Ingrid). Wer mehr will, bekommt die App. |
| **Abgrenzung** | Kein Technik-Gadget mit vielen Einstellungen: die Interaktion steht im Mittelpunkt. |

- ✍️ **Einstiegssatz Felix** noch offen: „Wie bin ich drauf gekommen?“ in ein bis zwei Sätzen, gern mit Bezug zur unbedienbaren Mikrowelle (Folie 8).

### S. 14 Die erste Woche

- Ablauf aus vorhandenen Bildschirmen: SORTEN → Sorte wählen → Starten (Tag 1) → Box regelt, Ring zählt → „Wasser leer“ → AUFGEFÜLLT → Erntebereit → Neue Sorte.
- Fehlt im Bedienfeld: eine **Ersteinrichtung** (die Box startet direkt mit „Auster, 15 Tage“). Entscheidung am 07.11.: nur zeigen, was da ist, oder neu bauen.
- Case 3 aus der Präsentation, **Handy verbinden**, gehört hierher als Übergang zur App.

### S. 17 Abwägungen Bedienfeld (Entscheidung · Grund (Folie) · Nachteil)

Kandidaten, die noch auf keiner Seite stehen. Die Nachteile sind Vorschläge, am 07.11. prüfen:

| Entscheidung | Grund (Folie) | Nachteil |
|---|---|---|
| Kein Ruhemodus, Standby nur bei „Tank leer“ | ein Modus weniger, weniger Modusfehler (60) | Display verbraucht dauerhaft Strom |
| KLIMA zeigt die Automatik, ohne Eingriff; „1 Min lüften“ nur in der App | Automatik sichtbar statt Eingriff (56, 59, 60), Fehler vermeiden (Murphy 61) | Ingrid kann am Gerät nicht selbst nachhelfen |
| Meldung einzeilig, Knopfwort nur auf dem Knopf | kürzer und ruhiger (83–85, 130) | das Knopfwort steht nicht mehr im Satz |
| Drei Kacheln statt fünf, Seltenes hinter dem Zahnrad | große Ziele (Fitts 50), minimalist design (130) | Urlaub, Sprache, Hilfe liegen einen Tipp tiefer |
| Sprache: andere Sprachen ausgegraut statt versteckt | logischer Constraint (75) | im Prototyp nur Deutsch |
| Schwierigkeit als 1–3 Pilze wie ein Level | Gamification: Progression (G 10) | Einstufung ist eine Annahme |

Gestrichene Funktionen als Iterationsbeleg (früher Seite „Sieben Stände“): Ruhemodus (60), Uhr auf dem Startbild (130), Warnlicht an der Box.

## Offen

- [ ] **Taster oder Schiebeschalter, Display immer an oder Handsensor?** Widerspruch zu S. 05/06 des Kollegen; betrifft S. 08–11 (siehe `booklet-plan.md`).
- [ ] **Persona einheitlich:** im Booklet „Ingrid, 72“, in der Präsentation ohne Alter.
- [ ] **Evaluation fehlt im Booklet**, seit die Seite „Geprüft. Und was offen ist.“ am 06.11. gestrichen wurde: Nielsen-Check 9/10, Farbsimulation, Kontrast 2,8 → 6,4. Steht sie in einem anderen Teil, oder kommt sie auf S. 17?
- [ ] Ehrliche Grenzen unterbringen: Messwerte simuliert, Personas sind Annahmen, kein Test mit Älteren, Admin-Modus und Zeitraffer nur für die Vorführung.
- [ ] Mit den anderen abgleichen: App-Übergang, Gamification-Teil, Fazit.

## Weggefallen (Stand vor dem HTML-Booklet)

- **„5 Seiten pro Person, 20 Seiten“:** ersetzt durch ein gemeinsames Booklet mit 15–18 Seiten.
- **Gestaltung Blau/Barlow:** ersetzt durch den Grünton (Creme, Waldgrün, Salbei; Manrope); Folienbezug zwischen zwei Linien und Nummernkreise sind umgesetzt.
- **Seitenpläne S1–S5 und Textentwurf Seite 2:** umgesetzt auf S. 07–13 (Langtext in Git, Commit `8a5b82e`).
- **Sammelstelle vom 04.11.:** erledigt bis auf die Punkte unter „Offen“ und die Kandidaten für S. 17 oben. Umgesetzt: Bedienfeld v7 als Grundlage, Entscheidungen A/B, minimalistisch, 44 pt, Standby, Rahmen = drückbar, gestufte Bestätigung, Case 1/2.
- **Seiten Konzept, Arbeitsweg, Evaluation** (alte S. 1, 9, 10 vom 06.11.): gestrichen, in Git (Commit `950d254`).
