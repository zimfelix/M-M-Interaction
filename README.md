# M-M Interaction

**Mensch-Maschine-Interaktion an einer Growbox** – Uni-Projekt im Fach Human-Computer Interaction (Option B „Bedienoberfläche für eine Growbox“).

- Kleine Growbox für Pilze, aufgebaut wie eine Mikrowelle: links Pilzkammer aus Plexi, rechts Technikraum mit Bedienfeld
- Bedienung **am Gerät** über ein eingebautes iPhone 13 mini (Display) und einen physischen Taster, **aus der Ferne** über eine App (eigenes Teammitglied)
- Leitidee: **radikal einfach** – ein großer Zustand auf einen Blick, drei große Bedienkacheln, für alle Altersgruppen

Status: Konzept und Klick-Prototyp stehen, Box wird gebaut.

## Projektaufbau – nach Schritten

```text
M-M-Interaction/
├── BRIEF.md          Ziel, offene Punkte, alle bestätigten Entscheidungen
├── AGENTS.md         Arbeitsregeln für KI-Agenten
├── 01-konzept/       Interaktionskonzept: Personas, Storyboards, Vorlesungsbezug
├── 02-box-bau/       Zeichnungen der Box (Gestell, Sockel, Bedienfeld, LED-Rahmen)
├── 03-software/      Software auf dem Raspberry Pi: Server, Display, Demo-Panel, Tests
└── 04-evaluation/    Papierprototyp-Fotos, Testprotokolle, AttrakDiff
```

## Ich suche …

| … | hier |
|---|---|
| eine Entscheidung (Maße, Farben, Bedienkonzept) | [`BRIEF.md`](BRIEF.md) |
| Vorlesungskonzepte mit Foliennummern | [`01-konzept/HCI-KONZEPTE.md`](01-konzept/HCI-KONZEPTE.md) |
| Zeichnungen der Box | [`02-box-bau/README.md`](02-box-bau/README.md) |
| die Software starten oder testen | [`03-software/README.md`](03-software/README.md) |
| die Schnittstelle für die App | [`03-software/API.md`](03-software/API.md) |
| das Aussehen des Displays | [`03-software/src/growbox/web/display/`](03-software/src/growbox/web/display/) |
| die Regeln „Alles gut / Bald kümmern / Jetzt handeln“ | [`03-software/src/growbox/core/rules.py`](03-software/src/growbox/core/rules.py) |
| Vorführ-Szenarien für die Präsentation | [`03-software/src/growbox/simulation/scenarios.py`](03-software/src/growbox/simulation/scenarios.py) |
| GPIO-Pins von Taster und LED | [`03-software/src/growbox/config.py`](03-software/src/growbox/config.py) |

## Schnellstart (Laptop, ohne Hardware)

```bash
cd 03-software
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/uvicorn growbox.main:app --port 8000
```

Display: http://127.0.0.1:8000/ · Vorführ-Panel: http://127.0.0.1:8000/demo/ · Details: [`03-software/README.md`](03-software/README.md)
