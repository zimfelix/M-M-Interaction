# Promptverzeichnis – Booklet Growbox (Box + Bedienfeld)

**Werkzeug:** Claude Code (Anthropic), Zeitraum bis 08.11.2026, Schwerpunkt Booklet 06.–08.11.
**Form:** Verdichtet. Die Prompts sind **sinngemäß zusammengefasst** und nach Arbeitsschritten gruppiert, nicht wörtlich protokolliert. Viele kleine Korrekturprompts („S. 13 Einleitung kürzer“) sind zu einer Zeile zusammengefasst.
**Rollen:** Box, Hardware und Verkabelung habe ich selbst gebaut, die Seiten zu Zielgruppe, CAD und Prototyp stammen von Ardit Becolli. Die KI hat Layout, Text-Entwürfe und den HTML-Satz des Booklets umgesetzt. Inhaltliche Auswahl, Freigaben und Korrekturen kamen von mir.

---

## 0 · Vorarbeit, auf die das Booklet aufbaut (bis 05.11.)

| # | Prompt (sinngemäß) | Ergebnis (Ordner) | Eigene Leistung |
|---|---|---|---|
| 0a | „Fasse die Vorlesungskonzepte mit Bezug zur Growbox zusammen (Affordance, Mapping, Feedback, Gestaltgesetze, Farbe).“ | `01-konzept/HCI-KONZEPTE.md` | Konzepte für das Projekt ausgewählt |
| 0b | „Entwickle mit mir zwei Personas und ein Storyboard: Ingrid (nur Box) und Power-User (App als Zusatz).“ | `01-konzept/personas-storyboard.md` | Zielgruppe und Leitregel „Box regelt selbst“ |
| 0c | „Baue das Bedienfeld als klickbaren Prototyp und iteriere nach unseren Entscheidungen (v1 → v7).“ | `01-konzept/bedienfeld/` | Leitidee B „Radikal einfach“, alle Iterationsentscheidungen |
| 0d | „Erstelle Front-Skizzen und Zeichnungen für die Box: Kammer links, Technikraum rechts, Taster, Tank mit Sichtfenster.“ | `02-box-bau/` | Box, Hardware und Verkabelung selbst gebaut, Maße am Bau angepasst |
| 0e | „Skizziere die Software-Architektur: Box-Modell mit Regeln, Simulation der Messwerte, Schnittstelle für Display und App.“ | `03-software/` (erster Entwurf, ruht) | Entscheidung „Interface vor Technik“ |

## 1 · Grundlage aus Konzept und Präsentation (04.–05.11.)

| # | Prompt (sinngemäß) | Ergebnis | Eigene Leistung |
|---|---|---|---|
| 1 | „Halte das Feedback aus der Präsentation fest und friere das Bedienfeld als v7 ein.“ | Feedback-Notizen, Spezifikation v7 | Feedback mitgeschrieben, entschieden, was übernommen wird |
| 2 | „Gleiche unsere Bedienfeld-Entscheidungen mit den Vorlesungskonzepten ab (z. B. Feedback, Mapping, Affordance, Gestaltgesetze) und ordne jeder Entscheidung den passenden Begriff zu.“ | `entscheidungen-folien.md` | Konzepte geprüft, unpassende Zuordnungen gestrichen |
| 3 | „Markiere in den Konzeptdateien, was ins Booklet gehört.“ | 📘-Marken | Auswahl der Inhalte |
| 4 | „Schreibe einen ersten Textentwurf für Seite 1: Konzept, Vorgehen, Persona Ingrid, Leitideen.“ | Entwurf `booklet-felix.md` | Persona und Leitideen aus unserem Konzept vorgegeben |

## 2 · Erste Booklet-Fassung und Abgleich mit dem Team (06.11.)

| # | Prompt (sinngemäß) | Ergebnis | Eigene Leistung |
|---|---|---|---|
| 5 | „Setze die Booklet-Seiten zu Box und Bedienfeld als HTML mit Doppelseiten-Ansicht um.“ | 10 Seiten HTML | Seitenplan, Reihenfolge |
| 6 | „Gleiche den Stil an die Seiten ‚Design & Bau‘ meines Kollegen an (Schrift, Farben).“ | gemeinsamer Stil, Grünton | Abstimmung mit dem Kollegen |
| 7 | „Erstelle einen Plan für das Teamtreffen am 07.11.: Abgleich, Konzeptweg V1–V3, Seitenplan, offene Fragen.“ | `booklet-plan.md` | Treffen geführt, Ergebnisse zurückgegeben |

## 3 · Gesamt-Booklet und Seitenstruktur (07.11.)

| # | Prompt (sinngemäß) | Ergebnis | Eigene Leistung |
|---|---|---|---|
| 8 | „Bau das Booklet auf Basis der Kollegen-Version neu auf und bette seine aktuellen Seiten ein.“ | 16–19 Seiten | Entscheidung für eine gemeinsame Fassung |
| 9 | „Gliedere das Bedienfeld in Konzept, Bedienung und Weggelassenes & Offen.“ | Kapitel 12–14 · 15–17 · 18 | Kapitelstruktur festgelegt |
| 10 | „Steig mit den Anforderungen ein: Nutzungskontext und vier Anforderungen ans Bedienfeld.“ | S. 03 | Anforderungen aus unserer Zielgruppe abgeleitet |
| 11 | „Verweise im Booklet über Fachbegriffe aus der Vorlesung statt über Foliennummern; setze unten pro Seite eine Leiste ‚Aus der Vorlesung‘.“ | Vorlesungsleisten | Begriffe pro Seite geprüft und gekürzt |
| 12 | „Leite aus S. 03 und den Kollegen-Seiten eine Vorlage für Maße, Typografie und Farben ab und wende sie auf alle Seiten an.“ | `vorlage-seite.html` | Referenzseite ausgewählt |

## 4 · Inhaltsseiten Box und Bedienfeld (07.11. abends)

| # | Prompt (sinngemäß) | Ergebnis | Eigene Leistung |
|---|---|---|---|
| 13 | „S. 04: Konzeptweg der Box V1 → V3 mit Skizzen und Entscheidungstabelle; begründe Murphy’s Law verständlich.“ | S. 04 | Skizzen und Varianten aus dem Bau |
| 14 | „S. 05–06: Was ist an der Box dran, und wie bedient man sie (Taster, Griffe, Schieber); nenne den Nachteil ehrlich.“ | S. 05–06 | Bedienelemente aus dem gebauten Prototyp, Nachteile selbst benannt |
| 15 | „S. 12: Leitideen A · B · C als Skizzen; benenne die Gamification beim äußeren Ring.“ | S. 12 | Ideen aus unserer Konzeptphase |
| 16 | „S. 13: zeige V1 → Final mit nummerierten Änderungen.“ | S. 13 | Änderungen v1–v7 aus eigener Iteration |
| 17 | „S. 14: Farbwahl begründen, Warnpunkt hervorheben.“ | S. 14 | Farbentscheidungen |

## 5 · Bedienung, Inhalt, Ausblick (07./08.11. nachts)

| # | Prompt (sinngemäß) | Ergebnis | Eigene Leistung |
|---|---|---|---|
| 18 | „S. 15: Alltag als Ablauf Standby → Meldung → Startbild, Status mit bekannten Zeichen (Haken, Warndreieck, Pilz).“ | S. 15 | Zeichenwahl (mentales Modell) |
| 19 | „S. 16: zwei Wege für eine neue Sorte (Katalog · selbst gestalten), Halten-Geste erklären.“ | S. 16 | Ablauf aus dem Bedienfeld |
| 20 | „S. 02: drei Entwürfe fürs Inhaltsverzeichnis zum Vergleich.“ | Entwurf B gewählt | Auswahl |
| 21 | „S. 18: Weggelassenes als Karten, Ausblick als Zeitstrahl.“ | S. 18 | entschieden, was weggelassen wurde |

## 6 · Gesamtreview und Feinschliff (08.11.)

| # | Prompt (sinngemäß) | Ergebnis | Eigene Leistung |
|---|---|---|---|
| 22 | „Mach ein Gesamtreview des Booklets und setz die Punkte um.“ | Korrekturen S. 11–18 | Review-Punkte bestätigt oder abgelehnt |
| 23 | Viele Einzelkorrekturen, z. B. „S. 06: Lichtschalter weckt nicht das Display“, „S. 14: Blau mit Farbsehen begründen statt mit Standby“, „S. 18: Karte Ruhemodus raus“. | ca. 30 kleine Änderungen | Fehler selbst gefunden, Formulierungen vorgegeben |

---

**Hinweis:** Die vollständige Historie aller Änderungen ist im Git-Verlauf des Projekts nachvollziehbar (rund 170 Commits zwischen 04.11. und 08.11.).
