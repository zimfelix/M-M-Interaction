#!/usr/bin/env python3
"""Booklet als PDF exportieren: Brave druckt booklet.html, danach wird die
Seitenanzeige auf "Zwei Seiten, Cover links" gesetzt (/PageLayout /TwoPageLeft),
damit S. 01 und S. 02 nebeneinander stehen statt das Cover allein.

Aufruf: python3 04-final/booklet-pdf.py  ->  04-final/Zimmermann_Felix_WS2627_Booklet.pdf
Nur Standardbibliothek; braucht Brave unter /Applications.
"""
import pathlib, re, subprocess, sys

HIER = pathlib.Path(__file__).resolve().parent
HTML = HIER / "booklet.html"
PDF = HIER / "Zimmermann_Felix_WS2627_Booklet.pdf"
BRAVE = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"


def drucken():
    subprocess.run([BRAVE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=15000", f"--print-to-pdf={PDF}", HTML.as_uri()],
                   check=True, capture_output=True)


def layout_setzen(data: bytes) -> bytes:
    # Inkrementelles Update: Katalog-Objekt mit /PageLayout neu anhängen, Rest bleibt unverändert.
    root = re.findall(rb"/Root (\d+) 0 R", data)[-1]
    m = re.search(rb"\n" + root + rb" 0 obj\s*(<<.*?>>)\s*endobj", data, re.S)
    katalog = re.sub(rb"/PageLayout\s*/\w+", b"", m.group(1))
    katalog = katalog[:2] + b"/PageLayout /TwoPageLeft\n" + katalog[2:]
    trailer = data[data.rindex(b"trailer"):]
    size = re.search(rb"/Size (\d+)", trailer).group(1)
    info = re.search(rb"/Info \d+ 0 R", trailer)
    prev = re.findall(rb"startxref\s*(\d+)", data)[-1]
    data = data.rstrip(b"\n") + b"\n"
    off = len(data)
    obj = root + b" 0 obj\n" + katalog + b"\nendobj\n"
    xref_pos = off + len(obj)
    xref = b"xref\n" + root + b" 1\n" + b"%010d 00000 n \n" % off
    tr = (b"trailer\n<</Size " + size + b" /Root " + root + b" 0 R"
          + (b" " + info.group(0) if info else b"") + b" /Prev " + prev + b">>\n"
          + b"startxref\n%d\n%%%%EOF\n" % xref_pos)
    return data + obj + xref + tr


if __name__ == "__main__":
    drucken()
    PDF.write_bytes(layout_setzen(PDF.read_bytes()))
    print(f"{PDF} (A4 einzeln, Zwei-Seiten-Ansicht, Cover links)", file=sys.stderr)
