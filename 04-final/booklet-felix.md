# Booklet · Felix' 5 Seiten: Box und Bedienfeld

Mein Teil: das **Hauptgerät**, also die physische Box und das Bedienfeld daran, erzählt an **Typ A · Ingrid**. Die App (Typ B) und weitere Teile kommen von den anderen Teammitgliedern. Die Stellen, die wir abstimmen müssen, sind unten mit ⚠️ markiert.

Jede Seite: **eine Aussage**, ein bis zwei Bilder, **Folien im Text ausdrücklich erklärt** (Muster aus [`entscheidungen-folien.md`](entscheidungen-folien.md): „Folie sagt … → deshalb …“). Das erfüllt die Kriterien von Folie 5: Theorie-Bezug, HCI-Grundprinzipien, Technologie.

## Einordnung ins Gesamt-Booklet (20 Seiten)

Das Booklet hat **20 Seiten, 5 pro Person**. Meine 5 Seiten sind der **Hauptteil zum Gerät**. Die anderen Teile (App, Typ B, gemeinsamer Rahmen) bauen darauf auf und verweisen zurück. Die Reihenfolge stimmen wir gemeinsam ab; ein Vorschlag:

```
Rahmen (Titel, Aufgabe, Vorgehen) → Felix: Box + Bedienfeld (Typ A) → App (Typ B) → Gamification / Evaluation / Fazit
```

## Gestaltung des Booklets (Vorschlag für alle 20 Seiten)

Das Booklet sieht aus wie das Produkt. Dann begründet die Gestaltung sich selbst: Wir zeigen äußere Konsistenz (Folie 80–81), statt nur darüber zu schreiben.

| Element | Vorschlag | Grund |
|---|---|---|
| **Farben** | Blau `#1525c4` als Akzentfläche (Kapitelbalken, Kästen); Grün `#3fcf7f` nur für „gut/erledigt“, Orange `#e69f00` nur für „Achtung“; Text schwarz auf Weiß | gleiche Bedeutung wie auf Box und App; Blau nie für kleine Schrift (Folie 20, 22) |
| **Schrift** | Barlow (wie das Bedienfeld), Überschriften Barlow Semi Condensed fett; Fließtext 10–11 pt | Wiedererkennung; gut lesbar gedruckt |
| **Raster** | pro Seite **eine Aussage** als Überschrift, ein großes Bild, Text in 2 Spalten | wie das Display: ein Blick, eine Aussage (Folie 16–17) |
| **Folienbezug** | ein wiederkehrender Kasten „📖 Folie 27: … → deshalb …“ in Blau mit weißer Schrift | macht das Bewertungskriterium von Folie 5 sichtbar |
| **Screenshots** | aus `bedienfeld-v6/`, mit nummerierten Markierungen (Kreise 1, 2, 3 …) statt Pfeil-Wirrwarr | Bild und Text lassen sich eindeutig zuordnen (Mapping, Folie 77–79) |
| **Personen** | kleines Symbol für Typ A und Typ B am Seitenrand, auf allen 20 Seiten gleich | man sieht sofort, für wen eine Entscheidung gilt |
| **Barrierefreiheit** | Kontrast ≥ 4,5 : 1, Status nie nur über Farbe (auch im Druck) | wir halten uns im Booklet an dieselben Regeln wie im Produkt |

⚠️ **Mit den anderen abstimmen:** Vorlage (z. B. gemeinsame Vorlage in Word, Pages oder Canva), Schrift, Farben und Folienkasten **vor** dem Schreiben festlegen. Sonst passen die 20 Seiten nicht zusammen.

## Überblick meiner 5 Seiten

```
S1 Nutzungskontext ──► S2 Die Box (Gestalt + Technik) ──► S3 Startbild
                                                              │
S5 Entwicklung + Evaluation ◄── S4 Ebenen + Use Cases Ingrid ◄┘
```

## Seite 1 · Vom Auftrag zum Konzept: Wer bedient die Box?

*Status: ✅ freigegeben 05.11. · offen: Einstiegsgeschichte*

✍️ **Einstieg (Felix ergänzt):** ein bis zwei Sätze „Wie bin ich drauf gekommen?“ (wo, was gab es dort, was ist aufgefallen); wenn passend mit Bezug zur unbedienbaren Mikrowelle (Folie 8).

**Aussage:** Die Box regelt das Klima selbst. Der Mensch hat nur drei Aufgaben, und genau diese müssen am Gerät leicht sein.

### Unser Konzept auf einen Blick

| | |
|---|---|
| **Konzept** | Eine Pilz-Growbox, die das Klima selbst regelt und am Gerät **radikal einfach** bedient wird: ein großer Zustand, drei Kacheln, ein Taster. Die App ist nur ein Zusatz. |
| **Ziel** | Jeder erkennt mit einem Blick, ob etwas zu tun ist, und erledigt die drei Aufgaben (nachfüllen, ernten, neu ansetzen) ohne Anleitung. |
| **Zielgruppe** | Alle Altersgruppen. Der Maßstab ist der schwächste Nutzer: **wenig Technikerfahrung, Lesebrille, unsichere Hände** (Persona Ingrid). Wer mehr will (Power-User), bekommt die App. |
| **Abgrenzung** | Kein Technik-Gadget mit vielen Einstellungen: Funktionen sind zweitrangig, die Interaktion steht im Mittelpunkt. |

### Auftrag und Vorgehen

Die Aufgabe (Folie 5, Option B) war eine Bedienoberfläche für eine Growbox. Wir haben daraus eine kleine Box für Pilze gemacht. Bedient wird sie **am Gerät** über ein eingebautes Touch-Display und einen Taster und **aus der Ferne** über eine App. Ich habe die Box und das Bedienfeld daran entworfen und gebaut. Die App stammt von einem anderen Teammitglied.

Wir sind nach dem **Double Diamond** und dem **User Centered Design** vorgegangen (Folie 104–107): erst das Problem verstehen, dann viele Lösungen skizzieren, eine auswählen, prototypisch umsetzen und prüfen.

```
Verstehen          Konzept              Prototyp                   Prüfen
Personas      →    3 Leitideen     →    Box-Skizzen v1 → v3    →   Nielsen-Check,
Box ↔ Mensch       Wahl: B              Bedienfeld v1 → v7         Farbsimulation,
                   „Radikal einfach“    (Papier → Klick-Prototyp)  Präsentation
```

### Für wen: Persona Ingrid

Eine **Persona** ist ein fiktiver, idealtypischer Nutzer (Folie 118). Unsere Personas decken bewusst verschiedene Altersgruppen ab, weil Alter, Vorkenntnisse und Sehkraft Nutzermerkmale sind (Folie 133). Für meinen Teil ist **Ingrid, 72** maßgeblich. Sie hat jahrzehntelang gegärtnert, nutzt aber kaum Touchscreens. Sie trägt eine Lesebrille, ihre Hände zittern leicht, und Technik misstraut sie.

Nach **Hassenzahl** (Folie 139) beschreiben wir Ingrid auf drei Ebenen:

| Ebene | Ingrid |
|---|---|
| **Warum** (Motiv) | etwas Sinnvolles pflegen, auch im Winter ohne Garten |
| **Was** (Handlungsziel) | Pilze ernten, ohne sich etwas merken oder einstellen zu müssen |
| **Wie** (motorisches Ziel) | einen echten Knopf drücken, große Flächen antippen, deutlich lesen |

Die zweite Persona, ein **Power-User**, der alles misst und auswertet, nutzt zusätzlich die App. Sie steht im App-Teil.

### Wer macht was?

Die wichtigste Entscheidung haben wir vor jedem Bildschirm getroffen: **Was regelt die Box selbst, und was bleibt dem Menschen?**

| Die Box regelt selbst | Der Mensch macht |
|---|---|
| Frischluft, Luftfeuchte, Wärme, Licht 8–20 Uhr | **Wasser nachfüllen** (ca. 1× pro Woche) |
| | **Ernten** |
| | **Neu ansetzen** (Kammer leeren, Zuchtset einsetzen) |

Daraus folgt die Leitfrage für alles Weitere: Braucht eine Aufgabe den Körper an der Box, gehört sie an die Box. Ist sie nur für Fortgeschrittene, gehört sie in die App.

### Drei Leitideen, eine Wahl

Wir haben drei Leitideen skizziert: **A „Pilz-Begleiter“** mit einer Spielfigur, **B „Radikal einfach“** mit einem großen Zustand und drei Kacheln und **C „Physisch zuerst“** mit Taster, Drehknopf und LED-Ring. Wir haben **B** gewählt. Eine Spielfigur (A) muss man erst deuten, bevor man weiß, ob etwas zu tun ist. Viele physische Elemente (C) erinnern an „die unbedienbare Mikrowelle“ (Folie 8). Von C bleibt **ein** Taster mit fester Bedeutung, von A der wachsende Pilz als leichte Gamification.

📷 **Bilder:** Persona-Kasten Ingrid · kleine Grafik „Box ↔ Mensch ↔ App“

## Seite 2 · Die Box: Gestalt, Bedienelemente, Technik

- **Aussage:** Aufgebaut wie eine Mikrowelle: links die Kammer, rechts Bedienfeld und Technik. Wenige, eindeutige Bedienelemente.
- **Inhalt:**
  - Folie 8 „Die unbedienbare Mikrowelle“ als Einstieg
  - **haptischer Licht-Taster**: Homunculus (33), Treffen ohne Zielen (49), Affordance (72–74)
  - **Tank mit Sichtfenster** = Mapping zur Anzeige „Wassertank“ (77–79)
  - Farbprinzip: Bedienteile heben sich vom Rahmen ab (Affordance)
  - **Technik** (Kriterium Folie 5): iPhone 13 mini als Display, Raspberry Pi als einziger Zustand, Taster/LED am Pi, App liest denselben Stand (**MVC**, 99–100)
- **Bilder:** `02-box-bau/bilder/skizze-box-v2.svg`, ggf. FreeCAD-Bild; Foto der gebauten Box (falls bis 08.11. fertig)
- ⚠️ **Abstimmen:** Entscheidungen A (Warnlicht) und B (Taster koppelt Display) vom 04.11. hier eintragen.

## Seite 3 · Das Startbild: ein Blick, eine Aussage

- **Aussage:** Aus der Ferne sieht man, ob etwas zu tun ist. Aus der Nähe sieht man, was.
- **Inhalt (E1–E5, E13, E14, E21–E25):**
  - **2 Zustände** mit Form + Farbe + Text (26, 23); **Warnpunkt blinkt** nur bei Warnung (27, 63)
  - **Ring** = Fortschritt/Countdown bis zur Ernte (G 10, Flow G 12)
  - **Werte** einheitlich, Tank als Füllstand `62 % · 4 T` (80, 86–87)
  - **3 Kacheln** KLIMA · MELDUNGEN · SORTEN (8, 50, 130)
  - **Blau nur als Fläche**, Schrift weiß, Kontrast gemessen (20, 22, 66, 76)
- **Bilder:** Screenshot Startbild „Alles gut“ (aus `bedienfeld-v6/`) mit 4–5 nummerierten Markierungen; daneben **`bilder/farbsimulation.png`** (eigene Messung)

## Seite 4 · Die Ebenen darunter: Ingrid handelt

- **Aussage:** Jede Ebene beantwortet eine Frage, und jede Handlung bekommt eine Rückmeldung.
- **Inhalt als kurze Use-Case-Kette (A2–A6 aus `praesentation.md`):**
  - Warnung „Wasser leer“ → Handlung + Knopf AUFGEFÜLLT (83–85, 59) → Bestätigung (82) → Verlauf **grün** (76)
  - **KLIMA:** Automatik sichtbar, kein Eingriff (56, 59, 60; „1 Min lüften“ nur in der App)
  - **SORTEN · Neu:** neu ansetzen nur mit 2 s Halten und Rückweg (61, 130)
  - **Einstellungen:** Sprache (ausgegraut, was fehlt: 75), Hoher Kontrast (66), Fehler melden (130)
- **Bilder:** 3–4 kleine Screenshots als Ablauf (Warnung → Meldungen → Klima → Einstellungen)
- ⚠️ **Abstimmen:** Übergang zur App (Typ B): ein Satz „Was Ingrid nicht braucht, liegt in der App“ und Verweis auf den App-Teil.

## Seite 5 · Entwicklung und Evaluation

- **Aussage:** Iterativ entwickelt (v1 → v6) und analytisch geprüft. Was wir noch nicht wissen, benennen wir.
- **Inhalt:**
  - Werdegang in 3 Bildern: v1 Kacheln → v4 Automatik sichtbar → v6 (Prototypen nach Houde & Hill, 122; formativ, 126)
  - Was die Folien geändert haben: z. B. Blinken nur für Warnung (27), Verlauf grün (59), Kontrast (66)
  - **Analytische Evaluation** (128): Farbsimulation, Kontrastmessung, Cognitive Walkthrough (129), Nielsen-Heuristiken (130)
  - **Ehrliche Grenzen:** Personas sind Annahmen; Messwerte simuliert; Sprachen nur angedeutet; kein Test mit echten Seniorinnen und Senioren (falls bis zur Abgabe nicht nachgeholt)
- **Bilder:** Werdegang-Leiste (Screenshots aus `01-konzept/bedienfeld/verlauf/` v1, v4 und `bedienfeld-v6/`)
- ⚠️ **Abstimmen:** Wer schreibt das gemeinsame Fazit und den Gamification-Teil (G 4–17)? Bei mir nur die Mechaniken am Bedienfeld.

## Noch zu erledigen

- [ ] Screenshots für S3–S5 aus `bedienfeld-v6/` erzeugen (Startbild markiert, Warnung, Meldungen, Klima, Einstellungen, Werdegang)
- [ ] Entscheidungen A/B vom 04.11. in S2 eintragen
- [ ] Mit den anderen abgleichen: Personas, App-Übergang, Fazit, Gamification
- [ ] Optional: Cognitive Walkthrough mit 1–2 Personen, Ergebnis in S5 und `evaluation/`

## 📥 Sammelstelle: Ergänzungen und Alternativen aus den Änderungen vom 04.11.

Gesammelt am 04.11., **Durchsicht am 05.11.** Nichts davon ist schon in den Seitenplan oben übernommen. Bei der Durchsicht je Punkt entscheiden: ✅ übernehmen · ❌ verwerfen · ⏸ später. Stand der Entscheidungen: `BRIEF.md`, Begründungen: E1–E31 in [`entscheidungen-folien.md`](entscheidungen-folien.md).

### Grundsatzfrage zuerst

| # | Frage | Alternativen | Empfehlung |
|---|---|---|---|
| G1 | **Welcher Stand kommt ins Booklet?** `bedienfeld-v6/` ist vom 02.11. eingefroren; seitdem gab es gut 20 Änderungen am Bedienfeld (Standby, Zeitraffer, Linien statt Rahmen …). | **A** nach der Präsentation neu einfrieren als `bedienfeld-v7/` und alle Screenshots daraus · **B** v6 lassen und die Änderungen nur auf S5 als Iteration zeigen | **A**, und v6 → v7 als Vorher/Nachher auf S5 nutzen. Nachteil: Screenshots für S3–S4 neu machen. |

### Ergänzungen je Seite

| # | Seite | Ergänzung | Folien | Art |
|---|---|---|---|---|
| 1 | S1 | Persona im Plan noch „Ingrid, 72“, in der Präsentation **ohne Altersangabe**. Einheitlich machen. | 118, 133 | Korrektur |
| 2 | S2 | Entscheidungen A/B sind gefallen: **kein physisches Warnlicht**, **Taster nur Licht**, **kein Ruhemodus**. Text aus „Entschieden am 04.11.“ in `entscheidungen-folien.md` übernehmen; den ⚠️-Punkt auf S2 streichen. | 60, 72–73, 27 | Ergänzung |
| 3 | S3 | **Minimalistisches Design** als eigene Aussage: ein Zustand, ein Ring, drei Werte, drei Kacheln, keine Uhr, Seltenes hinter dem Zahnrad. Gleiche Begründung wie in der Präsentation. | 130, 8, 38 | Ergänzung |
| 4 | S3 | **Große Knöpfe** ausdrücklich nennen: mindestens 44 pt, drei breite Kacheln. | 50, 63 | Ergänzung |
| 5 | S3 | Warnpunkt-Text ist veraltet („blinkt bei Warnung“). Neu: **Standby**, Display schwarz, nur der Punkt blinkt; in der normalen Ansicht blinkt nichts. | 27, 26, 23 | Korrektur |
| 6 | S3 oder S4 | **Neuer Grundsatz E31: Rahmen = drückbar, Linien = Information** (grün gut, orange Warnung). Starkes Beispiel für Affordance mit Vorher/Nachher-Bild (MELDUNGEN mit Box → mit Linien). | 72–73, 80 | Ergänzung, **eigener Kasten?** |
| 7 | S3 | **Gamification** genauer: Pilz wächst in drei Stufen, Schwierigkeit als 1–3 Pilze **wie ein Level**, Ernte als Hinweis statt Warnung. | G 10, G 12 | Ergänzung |
| 8 | S4 | Use-Case-Kette an die **Präsentation angleichen** (Case 1 Tank leer → Case 2 Ernte + neue Sorte → Case 3 Handy). Dann erzählen Booklet und Vortrag dieselbe Geschichte. | 143–150 (Storyboard) | Alternative zur Kette A2–A6 |
| 9 | S4 | **Abgestufte Bestätigung**: mitten im Wachstum 2 s halten, direkt nach der Ernte nur „Sicher?“, weil nichts verloren geht. Die Hürde passt zum Risiko. | 61, 130 | Ergänzung |
| 10 | S4 | Fehlermeldung jetzt **einzeilig**: „Wasser leer · Tank im Technikraum auffüllen“, Knopfwort nur noch auf dem Knopf. Abwägung nennen: kürzer und ruhiger, dafür steht das Knopfwort nicht mehr im Satz. | 83–85, 130 | Ergänzung |
| 11 | S4 | Einstellungen aktualisieren: **Hilfe** (statt „Fehler melden“), Darstellung mit **Individuell** (nur angezeigt), **Urlaub als einziger Modus**, oben immer sichtbar. | 60, 66, 75, 130 | Korrektur |
| 12 | S5 | **Was wir gestrichen haben** als Iterationsbeleg: Ruhemodus (Modusfehler), Uhr (minimalist design), Admin-Fälle von vielen auf zwei. Weniger ist hier das Ergebnis der Folien. | 60, 130 | Ergänzung |
| 13 | S5 | **Admin-Modus und Zeitraffer** offen als Werkzeuge für die Vorführung benennen, nicht als Funktion für Ingrid. | – | Ergänzung |
| 14 | S5 | Ehrliche Grenzen ergänzen: **fällt das Display aus, gibt es keine Warnung** (kein Warnlicht); die übrigen Warnungen (Tür offen, zu warm …) nennen das Knopfwort noch im Satz und sind damit uneinheitlich. | 61, 80 | Ergänzung |
| 15 | S5 | Die **Probelauf-Liste** aus `praesentation.md` als Aufgaben für einen **Cognitive Walkthrough** nutzen (Ziel klar? Aktion erkennbar? Rückmeldung?). | 129 | Alternative für die Evaluation |

### Gestaltung des Booklets

| # | Idee | Grund |
|---|---|---|
| 16 | Den Folienkasten „📖 Folie …“ statt als blaue Box **zwischen zwei blauen Linien** setzen, wie die Informationen auf dem Display. | Gleiche Regel im Produkt und im Booklet (äußere Konsistenz, 80). Im Druck ist ohnehin nichts drückbar; ein Rahmen hätte keine Bedeutung. |
| 17 | Screenshots mit nummerierten Markierungen weiterhin, aber Markierungen **nicht als Rahmen** um Bildteile, sondern als Kreise mit Zahl. | Rahmen bedeutet im Produkt „drückbar“; im Bild würde er das verwischen. |
