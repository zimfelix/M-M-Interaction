"""Einstellungen an einer Stelle: Pins und Hardware-Modus.

Neue Aktoren (Vernebler, Lüfter, LED-Streifen) bekommen ihre Pins ebenfalls hier.
"""

from __future__ import annotations

import os

BUTTON_PIN = 17  # GPIO17 (Pin 11) -> Taster gegen GND (Pin 9)
LED_PIN = 18     # GPIO18 (Pin 12) -> Gate des MOSFET-Moduls für den LED-Streifen
BUTTON_BOUNCE_S = 0.05

SIMULATE_INTERVAL_S = 1.0  # Takt, in dem der Simulator Messwerte nachregelt


def force_simulation() -> bool:
    """MM_HARDWARE=sim erzwingt die Simulation auch auf dem Pi."""
    return os.environ.get("MM_HARDWARE") == "sim"
