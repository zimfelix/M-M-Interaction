"""Exportiert die Zeichnungen aus konzept/*.html als eigenständige SVG-Bilder.

GitHub zeigt HTML nur als Quelltext, SVG-Bilder aber direkt an. Das Skript nimmt
das <svg> aus jeder Seite, übernimmt deren CSS und bettet die Schriften ein,
damit die Bilder auch ohne Internet gleich aussehen.

Aufruf (nach jeder Änderung an einer Zeichnung):  python3 konzept/export_svg.py
"""

import base64
import re
import xml.etree.ElementTree as ET
from pathlib import Path

HIER = Path(__file__).parent
ZIEL = HIER / "bilder"
SEITEN = ["skizze-box", "skizze-sockel", "zeichnung-bedienfeld", "skizze-gestell"]

SCHRIFTEN = [
    ("Caveat", "400 700", "Caveat-variable.woff2"),
    ("IBM Plex Sans Condensed", "400", "IBMPlexSansCondensed-400.woff2"),
    ("IBM Plex Sans Condensed", "600", "IBMPlexSansCondensed-600.woff2"),
]


def font_css() -> str:
    regeln = []
    for familie, gewicht, datei in SCHRIFTEN:
        daten = base64.b64encode((HIER / "fonts" / datei).read_bytes()).decode()
        regeln.append(
            f"@font-face{{font-family:'{familie}';font-weight:{gewicht};"
            f"src:url(data:font/woff2;base64,{daten}) format('woff2')}}"
        )
    return "\n".join(regeln)


def seiten_css(html: str) -> str:
    """CSS der Seite ohne Regeln für html/body/svg (die gelten nur im Browser-Layout)."""
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not m:
        return ""
    regeln = re.findall(r"([^{}]+)\{([^{}]*)\}", m.group(1))
    behalten = [f"{sel.strip()}{{{body}}}" for sel, body in regeln
                if not re.match(r"\s*(html|body|svg)\b", sel)]
    return "\n".join(behalten)


def exportiere(name: str, fonts: str) -> Path:
    html = (HIER / f"{name}.html").read_text(encoding="utf-8")
    svg = re.search(r"<svg\b.*?</svg>", html, re.S).group(0)
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    breite, hoehe = vb.group(1), vb.group(2)
    kopf = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{breite}" height="{hoehe}"')
    svg = re.sub(r"<svg\b", kopf, svg, count=1)
    stil = f"<style>\n{fonts}\n{seiten_css(html)}\n</style>\n"
    hintergrund = '<rect width="100%" height="100%" fill="#fbfaf6"></rect>\n'
    if name.startswith("zeichnung"):
        hintergrund = '<rect width="100%" height="100%" fill="#ffffff"></rect>\n'
    svg = re.sub(r"(<svg\b[^>]*>)", r"\1\n" + stil.replace("\\", "\\\\") + hintergrund, svg, count=1)
    ET.fromstring(svg)  # bricht ab, falls das SVG kein gültiges XML ist
    ziel = ZIEL / f"{name}.svg"
    ziel.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + svg, encoding="utf-8")
    return ziel


def main() -> None:
    ZIEL.mkdir(exist_ok=True)
    fonts = font_css()
    for name in SEITEN:
        pfad = exportiere(name, fonts)
        print(f"{pfad.relative_to(HIER)}  ({pfad.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
