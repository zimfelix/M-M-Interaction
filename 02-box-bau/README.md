# Schritt 2 · Box-Bau

**Status: 🔄** Zeichnungen fertig (Front v1–v3) · Box bauen, Fotos und FreeCAD-Bilder fehlen

## Auf einen Blick

```
┌────────────── 335 mm ───────────────┐
│  Pilzkammer (250)       │ Bedienfeld│   oben: 4 LED-Streifen im Rahmen
│  3-mm-Plexi, Tür links  │  iPhone   │   rechts: Technikraum 85 mm
│                         │  ● Taster │   Taster beige mit Licht-Symbol
│                      ▌  │  ▭ Tank   │   ▌ Stangengriff beige
└─────────────────────────┴───────────┘   Sockel 30 mm, Höhe 250, Tiefe 200
```

## Das Wichtigste

- **Wie eine Mikrowelle:** links Kammer, rechts Bedienen + Technik (Folie 8: wenige Bedienelemente)
- **Gestell aus dem 3D-Drucker** (15 × 15-Profile, Prinzip Creality K2 Plus), alle Teile ≤ 250 mm
- **Tank vorn unten mit Sichtfenster**, Einfüllöffnung oben hinten; Wasser unten, Elektronik oben (Mapping zum Display, Folie 77–79)
- **Farbprinzip:** Anfassen = **beige** (Taster, Griffe), Rahmen schwarz/grau, **Orange nur für Warnungen** (Konsistenz, Folie 80)
- **Ein Taster, eine Bedeutung:** Licht an/aus (Affordance, Folie 72–74)
- **Neue Stände als neue Datei** (`-v2`, `-v3`); danach `python3 02-box-bau/export_svg.py`
- 3D-Modell zum Drehen: [`../04-final/3d-modell/`](../04-final/3d-modell/)

📘 Booklet S2: Die Skizzen 1 → 6 → 7 zeigen den Fortschritt der Box (Mikrowelle → Tank gut erreichbar → Orange nur für Warnungen).

## 1 · Front-Skizze: Aufbau wie eine Mikrowelle

![Front-Skizze](bilder/skizze-box.svg)

## 2 · Gestell aus dem 3D-Drucker (Prinzip K2 Plus)

![Gestell](bilder/skizze-gestell.svg)

## 3 · Sockel

![Sockel](bilder/skizze-sockel.svg)

## 4 · Technische Zeichnung Bedienfeld-Front

![Bedienfeld-Front](bilder/zeichnung-bedienfeld.svg)

## 5 · Farbvarianten 3D-Druck

Handybox rechts fest schwarz glänzend; Rahmen und Sockel aus beige, schwarz oder grau. **Seit v3 (02.11.):** Taster und Griffe fest **beige** (siehe Abschnitt 7). Damit sie sich abheben, ist der Rahmen schwarz oder grau; Variante C (beiger Rahmen) passt dazu nicht mehr.

![Farbvarianten](bilder/skizze-farben.svg)

## 6 · Front-Skizze v2: Wassertank gut erreichbar

Nachfüllen ist die Hauptaufgabe des Menschen (Tank-Variante A): Einfüllöffnung oben hinten, Trennwand (Wasser unten, Elektronik oben), Sichtfenster für den Wasserstand vorn unter dem Taster.

![Front-Skizze v2](bilder/skizze-box-v2.svg)

## 7 · Front-Skizze v3: Orange nur für Warnungen

Konsistenz mit dem Display (Folie 80): Orange bedeutet auf dem Display **Warnung**. Deshalb sind Taster, Türgriff und Deckelgriff **beige**, die Bedienfeld-Front schwarz glänzend; der Taster trägt ein eingeprägtes **Licht-Symbol** (Recognition, Folie 130; Affordance, 72–74). LEDs in der Zeichnung hellgelb (warmweißes Licht).

![Front-Skizze v3](bilder/skizze-box-v3.svg)

## Dateien

| Datei | Inhalt |
|---|---|
| [`zeichnungen/skizze-box.html`](zeichnungen/skizze-box.html) | Front-Skizze: Pilzkammer, Technikraum, Maße 335 × 250 × 200 |
| [`zeichnungen/skizze-gestell.html`](zeichnungen/skizze-gestell.html) | Gestell: Profile, Eckstück, LED-Profil, Teileliste |
| [`zeichnungen/skizze-sockel.html`](zeichnungen/skizze-sockel.html) | Sockel 30 mm, Bodenrahmen, Plexi-Wanne |
| [`zeichnungen/zeichnung-bedienfeld.html`](zeichnungen/zeichnung-bedienfeld.html) | Bedienfeld-Front 85 × 250 × 10 mit iPhone-Tasche |
| [`zeichnungen/skizze-box-v2.html`](zeichnungen/skizze-box-v2.html) | Front-Skizze v2: Einfüllöffnung, Trennwand, Tank unten vorn, Sichtfenster |
| [`zeichnungen/skizze-box-v3.html`](zeichnungen/skizze-box-v3.html) | Front-Skizze v3: Taster und alle Griffe beige, Taster mit Licht-Symbol, LEDs hellgelb |
| [`zeichnungen/skizze-farben.html`](zeichnungen/skizze-farben.html) | Drei Farbvarianten A/B/C für den 3D-Druck |
| [`masse-iphone-13-mini.md`](masse-iphone-13-mini.md) | iPhone-Maße aus Apples Zeichnung |
| [`export_svg.py`](export_svg.py) | erzeugt `bilder/*.svg` aus `zeichnungen/*.html` |

**Neue Stände als neue Datei anlegen** (z. B. `-v2`), bestehende Zeichnungen bleiben als Dokumentation. Danach `python3 02-box-bau/export_svg.py` ausführen und die Bilder mit committen. Schriften (OFL-Lizenz) liegen in `fonts/`.

## Links

- Ordner: `zeichnungen/` (Quellen, HTML, interaktiv: [`zeichnungen/index.html`](zeichnungen/index.html)) · `bilder/` (erzeugte SVGs, nicht von Hand bearbeiten) · `fonts/` (OFL-Lizenz)
- Oberfläche, Personas, Vorlesungsbezug: [`../01-konzept/`](../01-konzept/) · Entscheidungen (Maße, Material): [`../BRIEF.md`](../BRIEF.md)
- Weiter: [Übersicht](../README.md) · [Schritt 1](../01-konzept/) · [Schritt 3](../03-software/) · [Schritt 4](../04-final/)
