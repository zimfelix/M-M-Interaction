# Schritt 2 · Box-Bau

**Status: 🔄 in progress** · Gesamtübersicht: [`../README.md`](../README.md)

Zeichnungen der Box als Bilder (direkt auf GitHub sichtbar). Lokal gibt es dieselben Zeichnungen interaktiv in [`zeichnungen/index.html`](zeichnungen/index.html).

```text
02-box-bau/
├── zeichnungen/   Quellen: eine HTML-Seite je Zeichnung + index.html als Übersicht
├── bilder/        daraus erzeugte SVGs (nicht von Hand bearbeiten)
├── fonts/         Schriften für die SVGs (OFL-Lizenz)
├── export_svg.py  zeichnungen/*.html → bilder/*.svg
└── masse-iphone-13-mini.md
```

## 1 · Front-Skizze: Aufbau wie eine Mikrowelle

![Front-Skizze](bilder/skizze-box.svg)

## 2 · Gestell aus dem 3D-Drucker (Prinzip K2 Plus)

![Gestell](bilder/skizze-gestell.svg)

## 3 · Sockel

![Sockel](bilder/skizze-sockel.svg)

## 4 · Technische Zeichnung Bedienfeld-Front

![Bedienfeld-Front](bilder/zeichnung-bedienfeld.svg)

## Neu: LED verdeckt im oberen Rahmen

Ergänzt die Zeichnungen oben, ersetzt sie nicht. Die älteren Stände bleiben als Dokumentation unverändert.

### 5 · Gestell V2: verdeckte LED-Streifen oben

![Gestell V2](bilder/skizze-gestell-v2.svg)

### 6 · Technische Zeichnung oberer Rahmen mit LED-Kanal

![Oberer Rahmen](bilder/zeichnung-oberer-rahmen.svg)

## Dateien

| Datei | Inhalt |
|---|---|
| [`zeichnungen/skizze-box.html`](zeichnungen/skizze-box.html) | Front-Skizze: Pilzkammer, Technikraum, Maße 335 × 250 × 200 |
| [`zeichnungen/skizze-gestell.html`](zeichnungen/skizze-gestell.html) | Gestell: Profile, Eckstück, LED-Profil, Teileliste |
| [`zeichnungen/skizze-sockel.html`](zeichnungen/skizze-sockel.html) | Sockel 30 mm, Bodenrahmen, Plexi-Wanne |
| [`zeichnungen/zeichnung-bedienfeld.html`](zeichnungen/zeichnung-bedienfeld.html) | Bedienfeld-Front 85 × 250 × 10 mit iPhone-Tasche |
| [`zeichnungen/skizze-gestell-v2.html`](zeichnungen/skizze-gestell-v2.html) | Gestell V2: obere Profile 21 × 27 mit verdeckter LED |
| [`zeichnungen/zeichnung-oberer-rahmen.html`](zeichnungen/zeichnung-oberer-rahmen.html) | Oberer Rahmen: Untersicht, Profil-Schnitt, Eckstück oben, Teile |
| [`masse-iphone-13-mini.md`](masse-iphone-13-mini.md) | iPhone-Maße aus Apples Zeichnung |
| [`export_svg.py`](export_svg.py) | erzeugt `bilder/*.svg` aus `zeichnungen/*.html` |

**Neue Stände als neue Datei anlegen** (z. B. `-v2`), bestehende Zeichnungen bleiben als Dokumentation. Danach `python3 02-box-bau/export_svg.py` ausführen und die Bilder mit committen. Schriften (OFL-Lizenz) liegen in `fonts/`.

## Verwandt

- Oberfläche, Personas, Vorlesungsbezug: [`../01-konzept/`](../01-konzept/)
- Entscheidungen (u. a. Maße und Material): [`../BRIEF.md`](../BRIEF.md)
