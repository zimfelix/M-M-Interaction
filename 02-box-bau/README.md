# Schritt 2 · Box-Bau

**Status: ✅** Zeichnungen V1–V3 · Prototyp im FabLab gedruckt und gebaut; CAD und Fotos im Booklet S. 07–10 und in `04-final/bilder/design-bau/`

<img src="bilder/skizze-box-v3.svg" width="420" alt="Front-Skizze v3"> <img src="../04-final/bilder/3d-modell.png" width="380" alt="3D-Modell">

## ✅ Final

- **Wie eine Mikrowelle:** links Pilzkammer (Plexi), rechts Technikraum mit Bedienfeld (Folie 8)
- **Ein Taster, eine Bedeutung:** Licht an/aus, beige mit Licht-Symbol (Affordance, Folie 72–74)
- **Tank** vorn unten mit **Sichtfenster**, Einfüllöffnung oben hinten (Mapping, Folie 77–79)
- **Beige = anfassen** (Taster, Griffe) · Rahmen schwarz/grau · **Orange nur für Warnungen** (Folie 80)
- **Gestell aus dem 3D-Drucker** (15 × 15-Profile), alle Teile ≤ 250 mm; LEDs verdeckt im oberen Rahmen
- **Kein Warnlicht** an der Box, die Warnung zeigt das Display
- 3D-Modell zum Drehen: [`../04-final/3d-modell/`](../04-final/3d-modell/)

## 🛤 Arbeitsweg 📘 Booklet S2

```
v1 Mikrowelle ──► v2 Tank gut erreichbar ──► v3 beige = anfassen ──► 3D-Modell
```

<img src="bilder/skizze-box.svg" width="260" alt="v1"> <img src="bilder/skizze-box-v2.svg" width="260" alt="v2"> <img src="bilder/skizze-box-v3.svg" width="260" alt="v3">

Bauzeichnungen: <img src="bilder/skizze-gestell-v2.svg" width="190" alt="Gestell"> <img src="bilder/skizze-sockel.svg" width="190" alt="Sockel"> <img src="bilder/zeichnung-bedienfeld.svg" width="190" alt="Bedienfeld-Front"> <img src="bilder/skizze-farben.svg" width="190" alt="Farbvarianten">

## Dateien

| Datei | Wofür |
|---|---|
| `zeichnungen/*.html` | Quellen, interaktiv: [`zeichnungen/index.html`](zeichnungen/index.html) |
| `bilder/*.svg` | daraus erzeugt (`python3 02-box-bau/export_svg.py`), nicht von Hand bearbeiten |
| [`masse-iphone-13-mini.md`](masse-iphone-13-mini.md) | iPhone-Maße für die Halterung |
| `fonts/` | Schriften der SVGs (OFL-Lizenz) |

Neue Stände als neue Datei (`-v2`, `-v3`), alte bleiben als Dokumentation.

## Links

[BRIEF (Maße, Material)](../BRIEF.md) · [Übersicht](../README.md) · [01](../01-konzept/) · [03](../03-software/) · [04](../04-final/)
