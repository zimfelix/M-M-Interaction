# Schritt 3 · Software

**Status: ⏸ ruht – erster Entwurf, nicht abgestimmt; zeigt noch die alte Oberfläche (v1). Priorität hatten Interface und Interaktion.** · Gesamtübersicht: [`../README.md`](../README.md)

Läuft auf dem Raspberry Pi (am Laptop ohne Hardware testbar). Der Pi hält den **einzigen Zustand** der Box; Display, App und Demo-Panel sind Ansichten davon.

## Aufbau

```text
03-software/
├── pyproject.toml        Dependencies
├── src/growbox/
│   ├── main.py           setzt alles zusammen (create_app)
│   ├── config.py         Pins, Takt, MM_HARDWARE
│   ├── core/             stabiler Kern: state.py (Zustand), rules.py (Bewertung, Texte)
│   ├── hardware/         base.py (Schnittstelle), gpio.py (Pi), simulated.py (Laptop/Tests)
│   ├── simulation/       scenarios.py (Vorführ-Szenarien), simulator.py (Messwerte)
│   ├── api/              routes.py (HTTP), websocket.py (Live-Updates), schemas.py
│   └── web/              demo/ (Vorführ-Panel); das Bedienfeld liegt in ../01-konzept/bedienfeld/
```

```text
Taster ──────► hardware/ ──┐
Display, App ► api/routes ─┼─► core/BoxModel ──► api/websocket ─► Display, App, Demo-Panel
Messwerte ───► simulation/ ┘   (bewertet mit   └─► hardware/ ─► LED
                                core/rules)
```

**Regel:** `core/` importiert nie FastAPI oder gpiozero. Neue Hardware (Vernebler, Lüfter, LED-Streifen) kommt als neue Datei in `hardware/` plus Pins in `config.py`; der Kern bleibt unverändert.

## Lokal starten (Laptop, ohne Hardware)

```bash
cd 03-software
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/uvicorn growbox.main:app --port 8000
```

- Display: http://127.0.0.1:8000/ (am Laptop als Handy-Rahmen im Hochformat)
- Vorführ-Panel: http://127.0.0.1:8000/demo/
- API-Doku für die App: http://127.0.0.1:8000/docs

Ohne Raspberry Pi werden Taster und LED automatisch simuliert (`MM_HARDWARE=sim` erzwingt das auch auf dem Pi); Feuchte und Temperatur sind im Prototyp immer simuliert. Auf dem Pi bringt Raspberry Pi OS `gpiozero` bereits mit.

## Auf dem iPhone anzeigen

1. Server im WLAN erreichbar starten: `.venv/bin/uvicorn growbox.main:app --host 0.0.0.0 --port 8000`
2. Auf dem iPhone in Safari `http://<IP des Pi oder Laptops>:8000/` öffnen → Teilen → **Zum Home-Bildschirm** (startet dann ohne Safari-Leisten).
3. In den iPhone-Einstellungen **Bedienungshilfen → Geführter Zugriff** aktivieren und in der App dreimal die Seitentaste drücken: Das iPhone bleibt dann auf der Growbox-Oberfläche.
4. Automatische Sperre auf „Nie“ stellen und das iPhone dauerhaft ans Ladekabel hängen.

## Später (wenn der Pi da ist)

- `deploy/`: Autostart beim Booten (systemd-Dienst) und Einrichtungsanleitung
