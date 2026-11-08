# M-M Interaction – Projektregeln für Agenten

Uni-Projekt (HCI, Prof. Zagel, Option B): Interaktionskonzept und Prototyp für eine Growbox mit eingebautem iPhone als Touch-Display, physischem Taster und App. Schwerpunkt ist die **Mensch-Maschine-Interaktion**, nicht die Technik.

**Status: ✅ abgeschlossen** (Präsentation 05.11., Booklet abgegeben 08.11.2026). Bei Wiederaufnahme oder Rückblick zuerst `README.md` lesen (Gesamtzusammenfassung, bekannte Ungenauigkeiten), dann `BRIEF.md`. Wiederverwendbare Gestaltung für neue Booklets und Präsentationen steht in `BAUKASTEN.md`; die abgegebene PDF nicht überschreiben.

## Dateien

- `README.md` – Gesamtzusammenfassung (Ergebnis, Booklet-Aufbau, Arbeitsweg, Grenzen) und Ordnerstruktur nach Projektschritten (`01-konzept/` … `04-final/`); Software-Aufbau in `03-software/README.md`.
- `BRIEF.md` – Ausgangslage, offene Punkte und **alle bestätigten Entscheidungen** (Tabelle „Entscheidungen“). Zu Beginn jeder Arbeit lesen.
- `01-konzept/HCI-KONZEPTE.md` – Vorlesungskonzepte mit Foliennummern und Bezug zur Growbox. Bei Konzept-, Design- und Evaluationsentscheidungen sowie beim Booklet lesen.
- `BAUKASTEN.md` – Gestaltung für künftige Booklets und Präsentationen (Anordnung, Schriftgrößen, Kopf/Fuß, Folienbezug, Grafik-Muster); für Agenten in neuen Projekten.
- `learnings.md` – Learnings aus den Präsentationen für **weitere Uni-Projekte** (nicht für Coding/Harness). Neue Erkenntnisse von Felix dort als „offen“ eintragen.

## Arbeitsabsprachen

- **Modus:** Shipping (bis zur Abgabe). Erklärungen kurz und entscheidungsorientiert.
- **Rollen:** Felix baut Box, Hardware und Verkabelung selbst. Die App baut ein anderes Teammitglied. Der Agent liefert Konzept, Software und Anleitungen.
- **Autonomie:** Innerhalb eines freigegebenen Schritts selbst schreiben, testen und lokal committen. **Rückfrage vor:** Push, neuen Dependencies, Architekturänderungen, Einkäufen.
- **Kein Bau ohne Zustimmung:** Erst Konzept und Architektur vorschlagen, bauen erst nach Freigabe.
- **Git:** Vor jedem Commit `git status` prüfen und nur eigene Änderungen gezielt stagen (kein `git add -A`); fremde Änderungen ansprechen.
- **Bedienfeld geändert?** Danach `sh 01-konzept/bedienfeld/screenshot.sh` ausführen (Bild in der README) und die Präsentationsansicht auf denselben claude.ai-Link neu veröffentlichen (https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi; `vorschau-praesentation.html` mit `index.html` als `aktuell/index.html`, dabei `data-src="index.html"` zu `aktuell/index.html` ändern). Nur dieser eine Link wird gepflegt (seit 2026-11-04), **für Mac und Handy**: am Mac das Display im schwarzen Rahmen, am Handy füllt das Bedienfeld den Bildschirm; nur das Display, ohne iPhone-Statusleiste, ✕/⋯ und Home-Strich, weil das iPhone nur Platzhalter für ein festes Display ist. Das README-Bild zeigt dieselbe Ansicht (`screenshot.sh` rendert `vorschau-praesentation.html`); `vorschau-iphone.html` bleibt nur lokal zum Vergleich der Handy-Ansichten, `verlauf/vorschau-einzeln.html` (Archiv) und der iPhone-Link `LCnX…` werden nicht mehr veröffentlicht.
- **README-Aufbau (Uni-Projekt):** Root-README und jede Ordner-README (`01-…` bis `04-…`) bringen den **Inhalt direkt und kurz**, damit Felix nur diese Dateien lesen muss: Status (1 Zeile) → **Bild(er) ganz oben** → **✅ Final** (Entscheidungen, Stichpunkte) → **🛤 Arbeitsweg** (Fortschritt als Zeitleiste/Grafik, ggf. kleine Bilder) → **Dateien** (kurze Tabelle, 📘 = Booklet) → **Links** in einer Zeile ganz unten. Bei Änderungen in einem Ordner dessen README mitpflegen. Für Felix Stichpunkte, Tabellen, Grafiken statt Fließtext; ausführlicher nur in Dateien für Agenten.
- **Entscheidungen** sofort in `BRIEF.md` eintragen; Überholtes ersetzen statt anhängen.
