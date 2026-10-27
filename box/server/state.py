"""Das Modell: der einzige Zustand der Box (single source of truth).

Display, App und Taster ändern nur dieses Modell; jede Änderung wird an alle
Ansichten verteilt (Model View Controller, Vorlesung HCI Folie 99).
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Awaitable, Callable

from .rules import evaluate

log = logging.getLogger(__name__)

Listener = Callable[[dict], Awaitable[None]]


@dataclass
class BoxState:
    light_on: bool = False
    light_source: str | None = None  # wer zuletzt geschaltet hat: display, app, taster, demo
    humidity: float = 88.0           # % relative Luftfeuchte
    temperature: float = 21.0        # °C
    humidity_trend: str | None = None  # "rising" / "falling" während der Simulator nachregelt
    temperature_trend: str | None = None
    day: int = 6
    harvest_day: int = 14
    scenario: str | None = "alles-gut"
    resolving: set[str] = field(default_factory=set)  # Hinweise, die gerade erledigt werden


class BoxModel:
    def __init__(self, hardware) -> None:
        self.state = BoxState()
        self.hardware = hardware
        self._listeners: list[Listener] = []

    def subscribe(self, listener: Listener) -> Callable[[], None]:
        self._listeners.append(listener)
        return lambda: self._listeners.remove(listener)

    def snapshot(self) -> dict:
        s = self.state
        result = evaluate(s.humidity, s.temperature, s.day, s.harvest_day, s.resolving)
        result["climate"]["humidity_trend"] = s.humidity_trend
        result["climate"]["temperature_trend"] = s.temperature_trend
        result["light"] = {"on": s.light_on, "source": s.light_source}
        result["scenario"] = s.scenario
        result["hardware"] = self.hardware.name
        return result

    async def set_light(self, on: bool, source: str) -> dict:
        self.state.light_on = on
        self.state.light_source = source
        self.hardware.set_light(on)
        return await self.notify()

    async def toggle_light(self, source: str) -> dict:
        return await self.set_light(not self.state.light_on, source)

    async def update(self, **values) -> dict:
        for key, value in values.items():
            if not hasattr(self.state, key):
                raise AttributeError(f"Unbekannter Zustandswert: {key}")
            setattr(self.state, key, value)
        return await self.notify()

    async def notify(self) -> dict:
        snap = self.snapshot()
        for listener in list(self._listeners):
            try:
                await listener(snap)
            except Exception:  # eine kaputte Ansicht darf die anderen nicht blockieren
                log.exception("Ansicht konnte nicht aktualisiert werden")
        return snap
