"""HTTP-Schnittstelle: Zustand lesen, Licht schalten, Hinweise bestätigen, Vorführung steuern."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from ..core import BoxModel
from ..simulation import SCENARIOS, Simulator
from .schemas import LightRequest, ScenarioRequest


def build_router(model: BoxModel, simulator: Simulator) -> APIRouter:
    router = APIRouter(prefix="/api")

    @router.get("/state", summary="Aktueller Zustand der Box")
    async def get_state() -> dict:
        return model.snapshot()

    @router.post("/light", summary="Licht an oder aus")
    async def set_light(req: LightRequest) -> dict:
        return await model.set_light(req.on, req.source)

    @router.post("/hints/{hint_id}/done", summary="Hinweis als erledigt bestätigen")
    async def hint_done(hint_id: str) -> dict:
        current = {h["id"] for h in model.snapshot()["hints"]}
        if hint_id not in current:
            raise HTTPException(404, f"Kein offener Hinweis '{hint_id}'.")
        return await simulator.resolve(hint_id)

    # --- nur für die Vorführung ---

    @router.get("/demo/scenarios", summary="Vorführ-Szenarien (nur Prototyp)")
    async def scenarios() -> list[dict]:
        return [{"name": name, "label": s["label"]} for name, s in SCENARIOS.items()]

    @router.post("/demo/scenario", summary="Szenario einstellen (nur Prototyp)")
    async def set_scenario(req: ScenarioRequest) -> dict:
        if req.name not in SCENARIOS:
            raise HTTPException(404, f"Unbekanntes Szenario '{req.name}'.")
        return await simulator.apply(req.name)

    @router.post("/demo/button", summary="Physischen Taster simulieren (nur Prototyp)")
    async def press_button() -> dict:
        return await model.toggle_light("taster")

    return router
