"""Hardware-Anschluss: auf dem Pi echt, sonst automatisch simuliert."""

from __future__ import annotations

import logging

from .. import config
from .base import Hardware
from .simulated import SimulatedHardware

log = logging.getLogger(__name__)

__all__ = ["Hardware", "SimulatedHardware", "create_hardware"]


def create_hardware() -> Hardware:
    if config.force_simulation():
        return SimulatedHardware()
    try:
        from .gpio import PiHardware

        return PiHardware()
    except Exception as exc:  # kein Pi, kein gpiozero oder keine Pins
        log.info("Keine GPIO-Hardware (%s) – Taster und LED werden simuliert.", exc)
        return SimulatedHardware()
