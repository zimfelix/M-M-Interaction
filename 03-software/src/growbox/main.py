"""Setzt die Growbox-App zusammen: Hardware + Kern + Simulator + Schnittstelle + Oberflächen.

Start (im Ordner 03-software/):  .venv/bin/uvicorn growbox.main:app --host 0.0.0.0 --port 8000
API-Doku für das App-Teammitglied: http://<pi>:8000/docs
"""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import config
from .api import LiveClients, build_router
from .core import BoxModel
from .hardware import Hardware, create_hardware
from .simulation import Simulator

WEB_DIR = Path(__file__).resolve().parent / "web"
# Das Bedienfeld gehört zum Konzept und liegt deshalb in 01-konzept/bedienfeld/
DISPLAY_DIR = Path(__file__).resolve().parents[3] / "01-konzept" / "bedienfeld"


def create_app(
    hardware: Hardware | None = None,
    simulate_interval: float | None = config.SIMULATE_INTERVAL_S,
) -> FastAPI:
    hw = hardware or create_hardware()
    model = BoxModel(hw)
    simulator = Simulator(model)
    live = LiveClients()
    model.subscribe(live.broadcast)

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

    app.include_router(build_router(model, simulator))
    app.include_router(live.router(model))
    # Statische Oberflächen zuletzt, damit "/" die API nicht verdeckt
    app.mount("/demo", StaticFiles(directory=WEB_DIR / "demo", html=True), name="demo")
    app.mount("/", StaticFiles(directory=DISPLAY_DIR, html=True), name="display")
    return app


app = create_app()
