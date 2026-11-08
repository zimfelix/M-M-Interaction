# M-M Interaction

**Status: ✅ abgeschlossen** · Präsentation 05.11.2026 · Booklet abgegeben 08.11.2026 (29 Seiten) · HCI, Prof. Zagel, Hochschule Coburg, WS 2026/27, Option B

[![Booklet: alle 29 Seiten](04-final/bilder/booklet-uebersicht.jpg)](04-final/Zimmermann_Felix_WS2627_Booklet.pdf)

**▶ Abgabe:** [`04-final/Zimmermann_Felix_WS2627_Booklet.pdf`](04-final/Zimmermann_Felix_WS2627_Booklet.pdf) · **▶ Bedienfeld live:** https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi (am Mac und Handy)

<img src="01-konzept/bedienfeld/bilder/vorschau-aktuell.png" width="260" alt="Bedienfeld v7"> <img src="04-final/bilder/3d-modell.png" width="440" alt="3D-Modell der Box">

## ✅ Final

**In einem Satz:** eine Pilz-Growbox, die das Klima selbst regelt und am Gerät **radikal einfach** bedient wird: ein großer Zustand, drei Kacheln, ein Taster. Die App ist ein Zusatz für alle, die mehr wollen.

| | |
|---|---|
| **Aufgabe** | Interaktionskonzept und Prototyp für eine Growbox; bewertet: Bezug zur Vorlesung, HCI-Grundprinzipien, beschriebene Technik (Booklet 50 % + Prototyp 50 %) |
| **Zielgruppe** | Maßstab ist **Ingrid, 72** (Lesebrille, unsichere Hände, nur die Box); der **Power-User** nutzt zusätzlich die App |
| **Leitregel** | **Die Box regelt selbst**, der Mensch macht nur: **nachfüllen · ernten · neu ansetzen** |
| **Box** | Aufbau **wie eine Mikrowelle**: links Pilzkammer aus Plexi, rechts Technikraum mit Bedienfeld; Gestell aus dem 3D-Drucker, gebaut im FabLab |
| **Bedienfeld** | iPhone 13 mini als Platzhalter für ein festes Display, Klick-Prototyp **v7**; Messwerte simuliert |
| **App** | Web-App von Adelin: Startseite = Kopie des Displays, Erweitert mit eigenen Werten und Statistiken |
| **Technik** | Raspberry Pi hält den einzigen Zustand, Display und App sind zwei Ansichten davon (MVC); Pi-Software nur als erster Entwurf |
| **Team** | Felix Schnapp · Ardit Becolli · Felix Zimmermann (Box, Design & Bau, Bedienfeld, Booklet S. 01–18) · Adelin Dinicu (App, S. 19–24) |

**Kernentscheidungen** (Begründung mit Folie: [`04-final/entscheidungen-folien.md`](04-final/entscheidungen-folien.md))

- **Leitidee „Radikal einfach“** statt Pilz-Begleiter (Spielfigur) oder „Physisch zuerst“ (nur Drehknopf und LEDs)
- **Status immer als Form + Farbe + Text:** grüner Haken „Alles gut“ · gelbes Warndreieck · beiger Pilz „Erntebereit“
- **Blau als Grundfarbe, Orange nur für Warnungen;** bei „Tank leer“ Standby: Display schwarz, nur ein **oranger Punkt blinkt**
- **Ein Taster, eine Bedeutung:** Licht an/aus, sonst nichts (kein Modus)
- **Rahmen = drückbar, Trennstrich = nur Info;** Ziele ≥ 44 pt, Kontrast ≥ 4,5 : 1
- **Eigene Werte und Analytics nur in der App,** die Box bleibt schlicht; Neu ansetzen mitten im Wachstum nur mit 2 s Halten
- **Bewusst weggelassen:** Uhr, Klima-Eingriff am Gerät, Signalton, Warnlicht

**Booklet** ([PDF](04-final/Zimmermann_Felix_WS2627_Booklet.pdf) · Quelle [`04-final/booklet.html`](04-final/booklet.html))

| Seiten | Kapitel | Inhalt |
|---|---|---|
| 01–02 | Cover · Inhalt | Inhalt als Kapitel-Strahl mit Vorschaubildern |
| 03 | Zielgruppe | Ingrid und Chris, vier Anforderungen ans Bedienfeld, Nutzungskontext |
| 04–06 | Konzeptweg Box | Aquarium → Mikrowelle (V1 → V3), Aufbau, haptische Elemente |
| 07–10 | CAD & Bau | FreeCAD, Rohdruck → Prototyp, alle Features, zwei Größen |
| 11 | Technik | Raspberry Pi, Regelkreis, ein Zustand (MVC) |
| 12–18 | Bedienfeld | Konzept (drei Ideen, V1 → Final, Farbe) · Bedienung (Alltag, neue Pilze, Einstellungen) · Weggelassen & offen |
| 19–24 | App | zwei Wege, Erweitert, Statistik, Gestrichenes, unterwegs |
| 25–29 | Promptverzeichnis | sinngemäße Prompts nach Projektstufen, App-Prompts von Adelin |

**Feedback zur Präsentation:** gelobt wurden der **Fortschritt vom Konzept zum Prototyp**, die **Entscheidungen mit Fachbegriffen der Folien** und der **orange Punkt**; Rückfrage „Warum Blau statt Schwarz?“ (Antwort auf S. 14).

**Nicht umgesetzt (Grenzen):** echte Sensoren und Pi-Software, Nutzertest (Cognitive Walkthrough, AttrakDiff); evaluiert wurde nur analytisch (Nielsen-Check, Farbsimulation, Kontraste).

**Bekannte Ungenauigkeiten im abgegebenen Booklet** (Final-Check 08.11., bewusst nicht mehr geändert): Tank-Befüllung S. 05 „Öffnung“ ↔ S. 06 „Schieber“ · S. 11 Schiebeschalter „An / Aus“ ↔ S. 06/13 Taster nur fürs Licht · S. 11 nennt nicht, dass Messwerte simuliert sind · Warnung heißt „Wasser leer“, „Tank leer“ und „Wasser fehlt“ · S. 21 zwei fehlende Zahlen.

## 🛤 Arbeitsweg

```
26.10. Start, Brief ──► 27.10. Architektur, Bedienfeld v1, Box V2 ──► 29.10. Tank-Entscheidung, Bedienfeld v2–v4
   ──► 02.11. Team zu viert, v5/v6 nach Folien-Review, Box V3 ──► 04.11. Admin-Modus, Spickzettel
   ──► 05.11. Präsentation ✅, v7 eingefroren ──► 06.11. erstes Booklet (13 S.)
   ──► 07.11. Teamtreffen, gemeinsames Booklet, Maß-Vorlage ──► 08.11. Bedienung, App, Promptverzeichnis, Abgabe ✅ (29 S.)

Commits je Tag   26.10. ▇ 9   27.10. ▇▇ 20   29.10. ▇▇ 21   02.11. ▇▇ 17   04.11. ▇▇▇▇ 36
                 05.11. ▇▇ 21   06.11. ▇ 12   07.11. ▇▇▇▇▇ 54   08.11. ▇▇▇▇▇▇ 65   (256 gesamt)
```

Schwerpunkt verschob sich bewusst: **Interaktion vor Technik.** Die Pi-Software ruht seit dem 29.10., die Zeit ging in Bedienfeld, Präsentation und Booklet.

## Dateien

```text
M-M-Interaction/
├── README.md        diese Zusammenfassung
├── BRIEF.md         alle Entscheidungen im Detail (Tabelle „Entscheidungen“)
├── AGENTS.md        Regeln für den KI-Agenten
├── BAUKASTEN.md     Gestaltung für künftige Booklets: Anordnung, Schrift, Kopf/Fuß, Folienbezug, Grafik-Muster
├── learnings.md     Learnings aus den Präsentationen für weitere Uni-Projekte
├── 01-konzept/      Personas, HCI-Konzepte mit Folien, Bedienfeld v7 + Verlauf v1–v6
├── 02-box-bau/      Skizzen und Zeichnungen der Box (V1–V3, Gestell, Farben)
├── 03-software/     erster Entwurf Pi-Software (FastAPI), ruht
└── 04-final/        Booklet (HTML + PDF), Maß-Vorlage, Entscheidungen E1–E31, Präsentation, 3D-Modell
```

| Frage | Datei |
|---|---|
| Was gilt? | [`BRIEF.md`](BRIEF.md) |
| Warum, mit welcher Folie? | [`04-final/entscheidungen-folien.md`](04-final/entscheidungen-folien.md) · [`01-konzept/HCI-KONZEPTE.md`](01-konzept/HCI-KONZEPTE.md) |
| Wie sieht das Bedienfeld aus? | [`01-konzept/bedienfeld/README.md`](01-konzept/bedienfeld/README.md) |
| Was nehme ich mit ins nächste Projekt? | [`BAUKASTEN.md`](BAUKASTEN.md) (Gestaltung, für den Agenten) · [`learnings.md`](learnings.md) (Präsentation) |

## Links

[Booklet-PDF](04-final/Zimmermann_Felix_WS2627_Booklet.pdf) · Bedienfeld live: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi · [3D-Modell](04-final/3d-modell/) · [Baukasten](BAUKASTEN.md) · [Learnings](learnings.md) · [BRIEF](BRIEF.md) · [01](01-konzept/) · [02](02-box-bau/) · [03](03-software/) · [04](04-final/)
