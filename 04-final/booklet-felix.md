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

## Seite 1 · Nutzungskontext: Wer bedient die Box und wofür?

- **Aussage:** Die Box regelt das Klima selbst. Der Mensch hat nur wenige, klar erkennbare Aufgaben: nachfüllen, ernten, neu ansetzen.
- **Inhalt:** Aufgabe (Folie 5); Persona **Ingrid, 72** (Folie 118: fiktiver, idealtypischer Nutzer) mit Warum/Was/Wie (Folie 139, Hassenzahl); Tabelle „Box macht / Mensch macht“ (aus `README.md`); Aufteilung Box ↔ App in einem Satz.
- **Folien:** 5, 104–107 (nutzerzentriertes Vorgehen), 118, 139, 133 (Alter und Sehkraft als Nutzermerkmale)
- **Bild:** Persona-Kasten Ingrid; kleine Grafik Box ↔ App
- ⚠️ **Abstimmen:** Wer stellt die Personas insgesamt vor? Bei mir nur Ingrid, Typ B beim App-Teil.

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
