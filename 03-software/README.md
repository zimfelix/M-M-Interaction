# Schritt 3 · Software

**Status: ⏸ nicht weitergeführt** (Projekt abgeschlossen 08.11.) · erster Entwurf, zeigt noch die alte Oberfläche (v1); Interface ging vor

```
Taster ──────► hardware/ ──┐
Display, App ► api/routes ─┼─► core/BoxModel ──► api/websocket ─► Display, App, Demo-Panel
Messwerte ───► simulation/ ┘   (core/rules)     └─► hardware/ ─► LED
```

## ✅ Final

- **Pi hält den einzigen Zustand**, Display und App sind Ansichten davon (MVC, Folie 99–100)
- **Stack:** Python + FastAPI (HTTP + WebSocket), Web-Oberfläche ohne Framework, gpiozero
- **Echt:** Taster, LED · **simuliert:** Feuchte, Temperatur
- **Regel:** `core/` importiert nie FastAPI oder gpiozero; neue Hardware = neue Datei in `hardware/`
- **Bis dahin:** Bedienfeld v7 läuft ohne Pi über `01-konzept/bedienfeld/iphone-server.sh`

## 🛤 Arbeitsweg

```
27.10. Architektur freigegeben ──► 28.10. Entwurf + Demo-Panel ──► 02.11. ruht (Interface vor Pi) ──► später: Pi, deploy/
```

## Dateien

```
03-software/
├── pyproject.toml   Dependencies
└── src/growbox/
    ├── main.py · config.py
    ├── core/        state.py (Zustand), rules.py (Bewertung, Texte)
    ├── hardware/    base.py, gpio.py (Pi), simulated.py
    ├── simulation/  scenarios.py, simulator.py
    ├── api/         routes.py, websocket.py, schemas.py
    └── web/demo/    Vorführ-Panel
```

**Lokal starten:** `cd 03-software && python3 -m venv .venv && .venv/bin/pip install -e . && .venv/bin/uvicorn growbox.main:app --port 8000` → Display `/`, Demo `/demo/`, API-Doku `/docs`

**Auf dem iPhone:** Server mit `--host 0.0.0.0` starten → Safari `http://<IP>:8000/` → Teilen → Zum Home-Bildschirm → Geführter Zugriff an, Auto-Sperre „Nie“, Ladekabel dran

## Links

[Bedienfeld](../01-konzept/bedienfeld/) · [Schnittstelle zur App](../01-konzept/begriffe-box-app.md) · [Übersicht](../README.md) · [01](../01-konzept/) · [02](../02-box-bau/) · [04](../04-final/)
