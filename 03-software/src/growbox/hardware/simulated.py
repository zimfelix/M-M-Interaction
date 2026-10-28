"""Simulierte Hardware für Laptop und Tests: merkt sich nur den Zustand."""

from __future__ import annotations

from typing import Callable


class SimulatedHardware:
    name = "simuliert"

    def __init__(self) -> None:
        self.light_on = False
        self._on_press: Callable[[], None] | None = None

    def on_button_press(self, callback: Callable[[], None]) -> None:
        self._on_press = callback

    def press_button(self) -> None:
        """Simuliert einen Tastendruck (Tests)."""
        if self._on_press:
            self._on_press()

    def set_light(self, on: bool) -> None:
        self.light_on = on
