"""Echte Hardware auf dem Raspberry Pi über gpiozero: Taster (Licht an/aus) und LED."""

from __future__ import annotations

from typing import Callable

from .. import config


class PiHardware:
    name = "gpiozero"

    def __init__(self) -> None:
        from gpiozero import Button, OutputDevice  # nur auf dem Pi vorhanden

        self._button = Button(config.BUTTON_PIN, bounce_time=config.BUTTON_BOUNCE_S)
        self._led = OutputDevice(config.LED_PIN)

    def on_button_press(self, callback: Callable[[], None]) -> None:
        self._button.when_pressed = callback  # läuft in einem eigenen Thread von gpiozero

    def set_light(self, on: bool) -> None:
        if on:
            self._led.on()
        else:
            self._led.off()
