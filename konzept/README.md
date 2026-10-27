# Konzept-Material

Aktueller Stand der Box als Bilder (direkt auf GitHub sichtbar). Lokal gibt es dieselben Zeichnungen interaktiv in [`index.html`](index.html).

## 1 · Front-Skizze: Aufbau wie eine Mikrowelle

![Front-Skizze](bilder/skizze-box.svg)

## 2 · Gestell aus dem 3D-Drucker (Prinzip K2 Plus)

![Gestell](bilder/skizze-gestell.svg)

## 3 · Sockel

![Sockel](bilder/skizze-sockel.svg)

## 4 · Technische Zeichnung Bedienfeld-Front

![Bedienfeld-Front](bilder/zeichnung-bedienfeld.svg)

## Dateien

| Datei | Inhalt |
|---|---|
| [`skizze-box.html`](skizze-box.html) | Front-Skizze: Pilzkammer, Technikraum, Maße 335 × 250 × 200 |
| [`skizze-gestell.html`](skizze-gestell.html) | Gestell: Profile, Eckstück, LED-Profil, Teileliste |
| [`skizze-sockel.html`](skizze-sockel.html) | Sockel 30 mm, Bodenrahmen, Plexi-Wanne |
| [`zeichnung-bedienfeld.html`](zeichnung-bedienfeld.html) | Bedienfeld-Front 85 × 250 × 10 mit iPhone-Tasche |
| [`masse-iphone-13-mini.md`](masse-iphone-13-mini.md) | iPhone-Maße aus Apples Zeichnung |
| [`export_svg.py`](export_svg.py) | erzeugt `bilder/*.svg` aus den HTML-Seiten |

**Nach jeder Änderung an einer Zeichnung:** `python3 konzept/export_svg.py` ausführen und die Bilder mit committen. Schriften (OFL-Lizenz) liegen in `fonts/`.

## Oberfläche und Nutzer

- **Konzept-Skizzen der Oberfläche (Blätter 01–14 mit Vorlesungsbezug):** https://claude.ai/artifact/7MF2tG589SHFE4ghP35TE9 – privat
- **Personas und Storyboards:** [`personas-storyboard.md`](personas-storyboard.md)
- **Vorlesungskonzepte mit Foliennummern:** [`../HCI-KONZEPTE.md`](../HCI-KONZEPTE.md)
- **Entscheidungen:** [`../BRIEF.md`](../BRIEF.md)

Hier ablegen: Fotos vom Papierprototyp, Testprotokolle, AttrakDiff-Ergebnisse.
