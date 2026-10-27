import pytest

from server.rules import evaluate, humidity_level, temperature_level


@pytest.mark.parametrize("humidity, level", [(68, "now"), (74.9, "now"), (75, "soon"), (84, "soon"),
                                             (85, "ok"), (95, "ok"), (97, "ok"), (98, "soon")])
def test_humidity_levels(humidity, level):
    assert humidity_level(humidity) == level


@pytest.mark.parametrize("temperature, level", [(11, "now"), (13, "soon"), (15, "ok"), (24, "ok"),
                                                (25, "soon"), (27.5, "now")])
def test_temperature_levels(temperature, level):
    assert temperature_level(temperature) == level


def test_all_good():
    result = evaluate(88, 21, day=6, harvest_day=14)
    assert result["status"] == {"level": "ok", "title": "Alles gut", "message": "Deine Pilze wachsen gut."}
    assert result["hints"] == []
    assert result["climate"]["humidity_label"] == "feucht genug"


def test_dry_gives_actionable_hint():
    result = evaluate(68, 21, day=6, harvest_day=14)
    assert result["status"]["level"] == "now"
    assert result["status"]["title"] == "Jetzt handeln"
    hint = result["hints"][0]
    assert hint["id"] == "zu-trocken"
    assert "Wasser" in hint["action"]


def test_most_urgent_hint_first():
    result = evaluate(80, 28, day=6, harvest_day=14)  # bald zu trocken + jetzt zu warm
    assert [h["id"] for h in result["hints"]] == ["zu-warm", "zu-trocken"]
    assert result["status"]["level"] == "now"


def test_harvest_ready():
    result = evaluate(90, 20, day=14, harvest_day=14)
    assert result["status"]["title"] == "Erntezeit!"
    assert result["growth"]["harvest_ready"] is True
    assert result["growth"]["progress"] == 1.0
