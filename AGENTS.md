# M-M Interaction – Projektregeln für Agenten

Uni-Projekt (HCI, Prof. Zagel, Option B): Interaktionskonzept und Prototyp für eine Growbox mit eingebautem iPhone als Touch-Display, physischem Taster und App. Schwerpunkt ist die **Mensch-Maschine-Interaktion**, nicht die Technik.

## Dateien

- `BRIEF.md` – Ausgangslage, offene Punkte und **alle bestätigten Entscheidungen** (Tabelle „Entscheidungen“). Zu Beginn jeder Arbeit lesen.
- `01-konzept/HCI-KONZEPTE.md` – Vorlesungskonzepte mit Foliennummern und Bezug zur Growbox. Bei Konzept-, Design- und Evaluationsentscheidungen sowie beim Booklet lesen.
- `README.md` – Ordnerstruktur nach Projektschritten (`01-konzept/` … `04-final/`); Software-Aufbau in `03-software/README.md`.

## Arbeitsabsprachen

- **Modus:** Shipping. Erklärungen kurz und entscheidungsorientiert.
- **Rollen:** Felix baut Box, Hardware und Verkabelung selbst. Die App baut ein anderes Teammitglied. Der Agent liefert Konzept, Software und Anleitungen.
- **Autonomie:** Innerhalb eines freigegebenen Schritts selbst schreiben, testen und lokal committen. **Rückfrage vor:** Push, neuen Dependencies, Architekturänderungen, Einkäufen.
- **Kein Bau ohne Zustimmung:** Erst Konzept und Architektur vorschlagen, bauen erst nach Freigabe.
- **Git:** Vor jedem Commit `git status` prüfen und nur eigene Änderungen gezielt stagen (kein `git add -A`); fremde Änderungen ansprechen.
- **Bedienfeld geändert?** Danach `sh 01-konzept/bedienfeld/screenshot.sh` ausführen (Bild in der README) und die Vorschau auf denselben claude.ai-Link neu veröffentlichen (https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi; `vorschau-iphone.html` mit `index.html` als `aktuell/index.html`). Dabei `data-src="index.html"` zu `aktuell/index.html` ändern. Nur dieser eine Link wird gepflegt (seit 2026-11-04); die Einzelansicht `vorschau-einzeln.html` wird nicht mehr veröffentlicht.
- **Entscheidungen** sofort in `BRIEF.md` eintragen; Überholtes ersetzen statt anhängen.
