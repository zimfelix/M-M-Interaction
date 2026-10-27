# M-M Interaction

**Mensch-Maschine-Interaktion an einer Growbox** – Uni-Projekt im Fach Human-Computer Interaction (Option B „Bedienoberfläche für eine Growbox“).

- Kleine Plexiglas-Growbox (ca. 20 cm) für Pilze
- Bedienung **am Gerät** über ein Touch-Display und einen physischen Taster, **aus der Ferne** über eine App (eigenes Teammitglied)
- Leitidee: **radikal einfach** – ein großer Zustand auf einen Blick, drei große Bedienkacheln, für alle Altersgruppen

Status: Konzeptphase. Ausgangslage und Entscheidungen: [BRIEF.md](BRIEF.md) · Vorlesungsbezug: [HCI-KONZEPTE.md](HCI-KONZEPTE.md)

## Projektaufbau

```text
box/            Software auf dem Pi (Server, Display, Vorführ-Panel, Tests)
docs/api.md     Schnittstelle für die App
konzept/        Skizzen-Link und Material für Booklet und Präsentation
```

## Lokal starten (Laptop, ohne Hardware)

```bash
cd box
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt -r requirements-dev.txt
.venv/bin/uvicorn server.main:app --port 8000
```

- Display: http://127.0.0.1:8000/ (am besten im Vollbild)
- Vorführ-Panel: http://127.0.0.1:8000/demo/
- API-Doku für die App: http://127.0.0.1:8000/docs
- Tests: `.venv/bin/python -m pytest -q`

Ohne Raspberry Pi werden Taster und LED automatisch simuliert; Feuchte und Temperatur sind im Prototyp immer simuliert.
