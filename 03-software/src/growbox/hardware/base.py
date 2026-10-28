"""Schnittstelle, die jede Hardware erfüllen muss – echt (gpiozero) oder simuliert.

Der Kern (core/) kennt nur diese Schnittstelle, nie gpiozero selbst.
"""

from __future__ import annotations

from typing import Callable, Protocol


class Hardware(Protocol):
    name: str  # erscheint im Zustand als "hardware"

    def on_button_press(self, callback: Callable[[], None]) -> None:
        """callback aufrufen, wenn der physische Taster gedrückt wird."""

    def set_light(self, on: bool) -> None:
        """LED ein- oder ausschalten."""
