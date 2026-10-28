"""Vorführ-Szenarien und Zielwerte für den Simulator.

Neue Szenarien für die Präsentation nur hier ergänzen; Demo-Panel und API lesen die Liste automatisch.
"""

from __future__ import annotations

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
