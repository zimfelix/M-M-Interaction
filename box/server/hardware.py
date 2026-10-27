"""Echte Hardware im Prototyp: ein Taster (Licht an/aus) und die LED.

Auf dem Raspberry Pi über gpiozero, am Laptop automatisch simuliert.
MM_HARDWARE=sim erzwingt die Simulation auch auf dem Pi.
"""

from __future__ import annotations

import logging
import os
from typing import Callable

log = logging.getLogger(__name__)

BUTTON_PIN = 17  # GPIO17 (Pin 11) -> Taster gegen GND (Pin 9)
LED_PIN = 18     # GPIO18 (Pin 12) -> Gate des MOSFET-Moduls für den LED-Streifen


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


class PiHardware:
    name = "gpiozero"

    def __init__(self) -> None:
        from gpiozero import Button, OutputDevice  # nur auf dem Pi vorhanden

        self._button = Button(BUTTON_PIN, bounce_time=0.05)
        self._led = OutputDevice(LED_PIN)

    def on_button_press(self, callback: Callable[[], None]) -> None:
        self._button.when_pressed = callback  # läuft in einem eigenen Thread von gpiozero

    def set_light(self, on: bool) -> None:
        if on:
            self._led.on()
        else:
            self._led.off()


def create_hardware():
    if os.environ.get("MM_HARDWARE") == "sim":
        return SimulatedHardware()
    try:
        return PiHardware()
    except Exception as exc:  # kein Pi, kein gpiozero oder keine Pins
        log.info("Keine GPIO-Hardware (%s) – Taster und LED werden simuliert.", exc)
        return SimulatedHardware()
