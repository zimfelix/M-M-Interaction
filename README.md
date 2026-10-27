# M-M Interaction

**Mensch-Maschine-Interaktion an einer Growbox** – Uni-Projekt im Fach Human-Computer Interaction (Option B „Bedienoberfläche für eine Growbox“).

- Kleine Growbox für Pilze, aufgebaut wie eine Mikrowelle: links Pilzkammer aus Plexi (ca. 20 cm), rechts Technikraum mit Bedienfeld
- Bedienung **am Gerät** über ein eingebautes iPhone 13 mini (Display) und einen physischen Taster, **aus der Ferne** über eine App (eigenes Teammitglied)
- Leitidee: **radikal einfach** – ein großer Zustand auf einen Blick, drei große Bedienkacheln, für alle Altersgruppen

Status: Konzept und Klick-Prototyp stehen, Box wird gebaut. Zeichnungen: [konzept/index.html](konzept/index.html). Ausgangslage und Entscheidungen: [BRIEF.md](BRIEF.md) · Vorlesungsbezug: [HCI-KONZEPTE.md](HCI-KONZEPTE.md)

## Projektaufbau

```text
box/            Software auf dem Pi (Server, Display, Vorführ-Panel, Tests)
docs/api.md     Schnittstelle für die App
konzept/        Zeichnungen der Box (index.html), Personas, Material fürs Booklet
```

## Lokal starten (Laptop, ohne Hardware)

```bash
cd box
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt -r requirements-dev.txt
.venv/bin/uvicorn server.main:app --port 8000
```

- Display: http://127.0.0.1:8000/ (am Laptop als Handy-Rahmen im Hochformat)
- Vorführ-Panel: http://127.0.0.1:8000/demo/
- API-Doku für die App: http://127.0.0.1:8000/docs
- Tests: `.venv/bin/python -m pytest -q`

Ohne Raspberry Pi werden Taster und LED automatisch simuliert; Feuchte und Temperatur sind im Prototyp immer simuliert.

## Auf dem iPhone anzeigen

1. Server im WLAN erreichbar starten: `.venv/bin/uvicorn server.main:app --host 0.0.0.0 --port 8000`
2. Auf dem iPhone in Safari `http://<IP des Pi oder Laptops>:8000/` öffnen → Teilen → **Zum Home-Bildschirm** (startet dann ohne Safari-Leisten).
3. In den iPhone-Einstellungen **Bedienungshilfen → Geführter Zugriff** aktivieren und in der App dreimal die Seitentaste drücken: Das iPhone bleibt dann auf der Growbox-Oberfläche.
4. Automatische Sperre auf „Nie“ stellen und das iPhone dauerhaft ans Ladekabel hängen.
