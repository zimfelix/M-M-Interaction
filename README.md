# M-M Interaction

**Mensch-Maschine-Interaktion an einer Growbox** – Uni-Projekt im Fach Human-Computer Interaction (Option B „Bedienoberfläche für eine Growbox“).

- Kleine Growbox für Pilze, aufgebaut wie eine Mikrowelle: links Pilzkammer aus Plexi, rechts Technikraum mit Bedienfeld
- Bedienung **am Gerät** über ein eingebautes iPhone 13 mini (Display) und einen physischen Taster, **aus der Ferne** über eine App (eigenes Teammitglied)
- Leitidee: **radikal einfach** – ein großer Zustand auf einen Blick, wenige große Bedienelemente, für alle Altersgruppen

## Aktueller Stand (29.10.2026)

Präsentation **05.11.2026, 10:00** · Abgabe **08.11.2026, 23:59**. Schwerpunkt ist **Interface und Interaktion**, nicht der technische Prototyp.

```text
   Box-Bedienfeld (iPhone in der Box)      separate App (Teammitglied)
   = Layout aus dem Panel-Link             ├─ Seite 1: einfache Übersicht
   + physischer Taster                     ├─ 4 weitere Unterseiten
                                           └─ 1 davon: Advanced Analytics
                     ▲                          ▲
                     └──── Raspberry Pi ────────┘   (zurzeit keine Priorität)
```

| Baustein | Stand |
|---|---|
| **Bedienfeld (Box)** | Bleibt wie im [Panel-Prototyp](https://claude.ai/artifact/EGmf5bvFTK16eYGfKWVkPE): Status „Austernpilz · Fruchtung“, Luftfeuchte ±, Ein/Standby, Frischluft 60 s, Meldungen, Sorte/Phase; Demo-Panel mit 5 Szenarien (Tank leer, Tür offen, zu warm, Sensor aus, Tag 6). Optische Referenz: Klima-Bedienfeld mit Symboltasten links/rechts und runder Anzeige in der Mitte. |
| **App** | Separat: einfache Startseite + 5 Unterseiten wie bei normalen Apps, eine davon **Advanced Analytics**. |
| **Box (Bau)** | Zeichnungen fertig (`02-box-bau/`, Gestell V2, oberer Rahmen mit verdeckter LED); Bau läuft. FreeCAD-Bilder hat ein Teammitglied. |
| **Software (Pi)** | Server, Regeln, Simulation und API stehen (`03-software/`), das Display dort zeigt aber noch die **alte** Oberfläche (Licht · Klima · Hinweise). Zurzeit keine Priorität. |
| **Booklet** | Großteils als **Story**: einfacher Nutzer und Power-User, der alles trackt; dazu ein Ausschnitt aus dem Bauprozess mit Skizzen und 1–2 FreeCAD-Bildern. Jede Szene braucht einen HCI-Bezug mit Folie (`01-konzept/HCI-KONZEPTE.md`). Bausteine: `01-konzept/personas-storyboard.md`. |

**Offen**

- Wärme und Luftfeuchte überhaupt im Interface – oder **nur Licht**?
- Taster weiterhin fest **Licht an/aus**? Bleibt der 3-Stufen-Zustand („Alles gut / Bald kümmern / Jetzt handeln“)?
- Power-User-Persona: Kultur bleibt **Pilze** – also ein erfahrener Pilzzüchter, der alles tracken will.
- Display-Code und API an das neue Panel anpassen – erst wenn der Pi wieder Priorität hat.

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
