"""Simulierte Messwerte und Vorführ-Szenarien.

Feuchte und Temperatur sind im Prototyp nicht echt. Für die Präsentation lässt
sich jeder Zustand gezielt einstellen; nach „Erledigt“ regelt der Simulator den
Wert langsam zurück, damit man „Feuchte steigt …“ sieht (Folien 64–65).
"""

from __future__ import annotations

import asyncio

from .state import BoxModel

SCENARIOS: dict[str, dict] = {
    "alles-gut": {"label": "Alles gut", "humidity": 88.0, "temperature": 21.0, "day": 6},
    "bald-trocken": {"label": "Bald zu trocken", "humidity": 80.0, "temperature": 21.0, "day": 6},
    "zu-trocken": {"label": "Zu trocken", "humidity": 68.0, "temperature": 21.0, "day": 6},
    "zu-warm": {"label": "Zu warm", "humidity": 88.0, "temperature": 27.5, "day": 6},
    "erntezeit": {"label": "Erntezeit", "humidity": 90.0, "temperature": 20.0, "day": 14},
}

# Zielwerte, auf die ein erledigter Hinweis zurückführt
RESOLVE_TARGETS = {
    "zu-trocken": ("humidity", 88.0),
    "zu-nass": ("humidity", 90.0),
    "zu-warm": ("temperature", 21.0),
    "zu-kalt": ("temperature", 18.0),
}
STEP = {"humidity": 2.0, "temperature": 0.5}  # Änderung pro Takt


class Simulator:
    def __init__(self, model: BoxModel) -> None:
        self.model = model
        self.targets: dict[str, float] = {}

    async def apply(self, name: str) -> dict:
        values = {k: v for k, v in SCENARIOS[name].items() if k != "label"}
        self.targets.clear()
        return await self.model.update(
            **values, scenario=name, resolving=set(),
            humidity_trend=None, temperature_trend=None,
        )

    async def resolve(self, hint_id: str) -> dict:
        """Hinweis wurde als erledigt bestätigt: Wert langsam zurückführen."""
        field, target = RESOLVE_TARGETS[hint_id]
        self.targets[field] = target
        current = getattr(self.model.state, field)
        trend = "rising" if target > current else "falling"
        resolving = self.model.state.resolving | {hint_id}
        return await self.model.update(resolving=resolving, **{f"{field}_trend": trend})

    async def step(self) -> None:
        if not self.targets:
            return
        changes: dict = {}
        for field, target in list(self.targets.items()):
            current = getattr(self.model.state, field)
            delta = max(-STEP[field], min(STEP[field], target - current))
            value = current + delta
            changes[field] = value
            if abs(target - value) < 1e-6:
                del self.targets[field]
                changes[f"{field}_trend"] = None
        if not self.targets:
            changes["resolving"] = set()
        await self.model.update(**changes)

    async def run(self, interval: float = 1.0) -> None:
        while True:
            await asyncio.sleep(interval)
            await self.step()
