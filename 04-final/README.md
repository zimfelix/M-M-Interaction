# Schritt 4 · Final

**Status: ✅ abgegeben 08.11.2026** · Präsentation 05.11. gehalten · Booklet 29 Seiten als PDF

<img src="bilder/booklet-uebersicht.jpg" width="720" alt="Booklet: alle 29 Seiten">

## ✅ Final

- **Abgabe:** [`Zimmermann_Felix_WS2627_Booklet.pdf`](Zimmermann_Felix_WS2627_Booklet.pdf) (A4 einzeln, 10,6 MB), erzeugt aus [`booklet.html`](booklet.html) mit `python3 04-final/booklet-pdf.py` (Headless-Brave, Zwei-Seiten-Ansicht mit Cover links)
- **Aufbau:** 01 Cover · 02 Inhalt · 03 Zielgruppe · 04–06 Konzeptweg Box · 07–10 CAD & Bau · 11 Technik · 12–18 Bedienfeld · 19–24 App (Adelin) · 25–29 Promptverzeichnis
- **Gestaltung:** Grünton (Creme · Waldgrün · Salbei), Space Grotesk + Inter; feste Maße aus [`vorlage-seite.html`](vorlage-seite.html), Layout je Seite frei
- **Vorlesungsbezug:** Begriff steht im Text als „(Begriff)“ hinter der Aussage, die Leiste „Aus der Vorlesung“ wiederholt genau diese; keine Folien- und Seitennummern
- **Präsentation:** 5 Min., ohne Folien, live: 3D-Entwurf → Bedienfeld (Felix, 2 Min., Admin-Modus mit 2 Fällen) → App; gelobt: Fortschritt, Fachbegriffe, oranger Punkt
- **Evaluation:** nur analytisch (Nielsen-Check 9/10, Farbsimulation, Kontraste); Walkthrough und AttrakDiff stehen im Booklet als Ausblick

## 🛤 Arbeitsweg

```
05.11. Präsentation ✅ ──► 06.11. erstes Booklet, 13 Seiten, eigener Teil
   ──► 07.11. Teamtreffen: ein gemeinsames Booklet, Seiten Design & Bau eingebettet, Maß-Vorlage, 18 Seiten
   ──► 08.11. Inhalt als Kapitel-Strahl, Bedienung 15–17, Gesamtreview, App 19–24, Promptverzeichnis, Final-Check ──► Abgabe ✅ 29 Seiten
```

Aufgeräumt nach der Abgabe (08.11.): Planungsdateien, Doppelseiten-PDF, ungenutzte Bilder und Entwürfe gelöscht (in Git), Bedienfeld v6 nach `01-konzept/bedienfeld/verlauf/v6/`.

## Dateien

| Datei | Wofür |
|---|---|
| [`Zimmermann_Felix_WS2627_Booklet.pdf`](Zimmermann_Felix_WS2627_Booklet.pdf) | **die Abgabe** |
| [`booklet.html`](booklet.html) · [`booklet-pdf.py`](booklet-pdf.py) | Quelle (Doppelseiten, Pfeiltasten, `?uebersicht` mit Zoom) und PDF-Export |
| [`vorlage-seite.html`](vorlage-seite.html) | **Maß-Vorlage** für Booklet-Seiten: Seitenaufbau, Schriftgrößen, Textfarben, inhaltliche Regeln, zum Wiederverwenden |
| [`booklet-design-bau/seiten/`](booklet-design-bau/seiten/) | Seiten Zielgruppe, CAD, Prototyp, Features, Zwei Größen (eingebettet, Bilder eingebaut) |
| [`entscheidungen-folien.md`](entscheidungen-folien.md) | E1–E31 mit Folie und Persona, Nielsen-Check, Grenzen 📘 |
| [`praesentation.md`](praesentation.md) | Ablauf, Spickzettel mit Zeitmarken, Probelauf, Rückfragen (Muster für künftige Präsentationen) |
| [`bedienfeld-v7/`](bedienfeld-v7/) | abgegebener Stand des Bedienfelds; öffnen: `vorschau-iphone.html` |
| [`3d-modell/`](3d-modell/) | 3D-Modell zum Drehen: `growbox-3d-v2-60x35x25.html` |
| [`bilder/`](bilder/) | Booklet-Bilder (`booklet/`, `app/`, `design-bau/` mit Bau-Fotos), Farbsimulation, 3D-Modell, Übersicht |

## Links

[Übersicht](../README.md) · [Learnings + Baukasten](../learnings.md) · [BRIEF](../BRIEF.md) · Bedienfeld live: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi · [01](../01-konzept/) · [02](../02-box-bau/) · [03](../03-software/)
