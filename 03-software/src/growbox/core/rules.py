"""Regeln: Messwerte -> Zustand in drei Stufen + Hinweise mit Handlungsanweisung.

Zielwerte für Austernpilze (Fruchtungsphase): Luftfeuchte 85–95 %, Temperatur 15–24 °C.
Die Texte sind bewusst kurz, konkret und höflich (Vorlesung HCI, Folien 83–85).
"""

from __future__ import annotations

LEVELS = ("ok", "soon", "now")  # Alles gut / Bald kümmern / Jetzt handeln

STATUS_TEXT = {
    "soon": "Bald kümmern",
    "now": "Jetzt handeln",
}


def worst(*levels: str) -> str:
    """Die dringlichste von mehreren Stufen."""
    return max(levels, key=LEVELS.index, default="ok")


def humidity_level(humidity: float) -> str:
    if humidity < 75:
        return "now"
    if humidity < 85 or humidity > 97:
        return "soon"
    return "ok"


def temperature_level(temperature: float) -> str:
    if temperature < 12 or temperature > 27:
        return "now"
    if temperature < 15 or temperature > 24:
        return "soon"
    return "ok"


def humidity_label(humidity: float) -> str:
    if humidity < 85:
        return "zu trocken"
    if humidity > 97:
        return "sehr nass"
    return "feucht genug"


def temperature_label(temperature: float) -> str:
    if temperature < 15:
        return "zu kalt"
    if temperature > 24:
        return "zu warm"
    return "angenehm"


def _hint(hint_id: str, level: str, title: str, action: str, resolving: set[str]) -> dict:
    return {
        "id": hint_id,
        "level": level,
        "title": title,
        "action": action,
        "resolving": hint_id in resolving,
    }


def evaluate(
    humidity: float,
    temperature: float,
    day: int,
    harvest_day: int,
    resolving: set[str] | None = None,
) -> dict:
    """Bewertet die Messwerte und liefert Zustand, Klima, Hinweise und Wachstum."""
    resolving = resolving or set()
    hum_level = humidity_level(humidity)
    temp_level = temperature_level(temperature)

    hints = []
    if hum_level != "ok":
        if humidity < 85:
            hints.append(_hint("zu-trocken", hum_level, "Es ist zu trocken.",
                               "Bitte Wasser in die Schale füllen – bis zur Linie.", resolving))
        else:
            hints.append(_hint("zu-nass", hum_level, "Es ist sehr nass.",
                               "Bitte den Deckel kurz öffnen und lüften.", resolving))
    if temp_level != "ok":
        if temperature > 24:
            hints.append(_hint("zu-warm", temp_level, "Es ist zu warm.",
                               "Bitte die Box an einen kühleren Ort stellen (unter 24 °C).", resolving))
        else:
            hints.append(_hint("zu-kalt", temp_level, "Es ist zu kalt.",
                               "Bitte die Box an einen wärmeren Ort stellen (über 15 °C).", resolving))
    # Dringendstes zuerst
    hints.sort(key=lambda h: LEVELS.index(h["level"]), reverse=True)

    level = worst(*(h["level"] for h in hints))
    harvest_ready = day >= harvest_day
    if level == "ok":
        title, message = (("Erntezeit!", "Deine Pilze sind bereit.") if harvest_ready
                          else ("Alles gut", "Deine Pilze wachsen gut."))
    else:
        title, message = STATUS_TEXT[level], hints[0]["title"]

    return {
        "status": {"level": level, "title": title, "message": message},
        "climate": {
            "level": worst(hum_level, temp_level),
            "humidity": round(humidity),
            "humidity_label": humidity_label(humidity),
            "temperature": round(temperature, 1),
            "temperature_label": temperature_label(temperature),
        },
        "hints": hints,
        "growth": {
            "day": day,
            "harvest_day": harvest_day,
            "progress": round(min(1.0, day / harvest_day), 3),
            "harvest_ready": harvest_ready,
        },
    }
