"""Server auf dem Pi: Schnittstelle (HTTP + WebSocket) für Display, App und Demo-Panel.

Start (im Ordner box/):  .venv/bin/uvicorn server.main:app --host 0.0.0.0 --port 8000
API-Doku für das App-Teammitglied: http://<pi>:8000/docs
"""

from __future__ import annotations

import asyncio
import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .hardware import create_hardware
from .simulator import SCENARIOS, Simulator
from .state import BoxModel

BOX_DIR = Path(__file__).resolve().parent.parent
log = logging.getLogger(__name__)


class LightRequest(BaseModel):
    on: bool
    source: str = Field("app", description="Wer schaltet: display, app, demo")


class ScenarioRequest(BaseModel):
    name: str


def create_app(hardware=None, simulate_interval: float | None = 1.0) -> FastAPI:
    hw = hardware or create_hardware()
    model = BoxModel(hw)
    simulator = Simulator(model)
    clients: set[WebSocket] = set()

    async def broadcast(snapshot: dict) -> None:
        for ws in list(clients):
            try:
                await ws.send_json(snapshot)
            except Exception:
                clients.discard(ws)

    model.subscribe(broadcast)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        loop = asyncio.get_running_loop()

        def on_press() -> None:  # kommt aus dem gpiozero-Thread
            loop.call_soon_threadsafe(lambda: loop.create_task(model.toggle_light("taster")))

        hw.on_button_press(on_press)
        task = loop.create_task(simulator.run(simulate_interval)) if simulate_interval else None
        yield
        if task:
            task.cancel()

    app = FastAPI(
        title="M-M Interaction – Growbox",
        version="0.1.0",
        description="Ein Zustand, mehrere Ansichten: Display an der Box, App und Demo-Panel.",
        lifespan=lifespan,
    )
    app.state.model = model
    app.state.simulator = simulator
    app.state.hardware = hw

    @app.get("/api/state", summary="Aktueller Zustand der Box")
    async def get_state() -> dict:
        return model.snapshot()

    @app.post("/api/light", summary="Licht an oder aus")
    async def set_light(req: LightRequest) -> dict:
        return await model.set_light(req.on, req.source)

    @app.post("/api/hints/{hint_id}/done", summary="Hinweis als erledigt bestätigen")
    async def hint_done(hint_id: str) -> dict:
        current = {h["id"] for h in model.snapshot()["hints"]}
        if hint_id not in current:
            raise HTTPException(404, f"Kein offener Hinweis '{hint_id}'.")
        return await simulator.resolve(hint_id)

    @app.get("/api/demo/scenarios", summary="Vorführ-Szenarien (nur Prototyp)")
    async def scenarios() -> list[dict]:
        return [{"name": name, "label": s["label"]} for name, s in SCENARIOS.items()]

    @app.post("/api/demo/scenario", summary="Szenario einstellen (nur Prototyp)")
    async def set_scenario(req: ScenarioRequest) -> dict:
        if req.name not in SCENARIOS:
            raise HTTPException(404, f"Unbekanntes Szenario '{req.name}'.")
        return await simulator.apply(req.name)

    @app.post("/api/demo/button", summary="Physischen Taster simulieren (nur Prototyp)")
    async def press_button() -> dict:
        return await model.toggle_light("taster")

    @app.websocket("/ws")
    async def live(ws: WebSocket) -> None:
        """Schickt sofort den Zustand und danach jede Änderung."""
        await ws.accept()
        clients.add(ws)
        try:
            await ws.send_json(model.snapshot())
            while True:
                await ws.receive_text()  # Clients senden nichts; hält die Verbindung offen
        except WebSocketDisconnect:
            pass
        finally:
            clients.discard(ws)

    app.mount("/demo", StaticFiles(directory=BOX_DIR / "demo", html=True), name="demo")
    app.mount("/", StaticFiles(directory=BOX_DIR / "ui", html=True), name="ui")
    return app


app = create_app()
