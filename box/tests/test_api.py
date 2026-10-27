import asyncio

from fastapi.testclient import TestClient

from server.hardware import SimulatedHardware
from server.main import create_app
from server.simulator import Simulator
from server.state import BoxModel


def make_client():
    hw = SimulatedHardware()
    app = create_app(hardware=hw, simulate_interval=None)
    return TestClient(app), hw


def test_state_and_light():
    client, hw = make_client()
    with client:
        assert client.get("/api/state").json()["light"]["on"] is False
        snap = client.post("/api/light", json={"on": True, "source": "display"}).json()
        assert snap["light"] == {"on": True, "source": "display"}
        assert hw.light_on is True  # LED wirklich geschaltet


def test_all_views_get_the_change():
    """Ein Zustand, mehrere Ansichten: eine Änderung erreicht jeden WebSocket-Client."""
    client, _ = make_client()
    with client, client.websocket_connect("/ws") as display, client.websocket_connect("/ws") as app_view:
        assert display.receive_json()["light"]["on"] is False
        assert app_view.receive_json()["light"]["on"] is False
        client.post("/api/light", json={"on": True, "source": "app"})
        assert display.receive_json()["light"]["source"] == "app"
        assert app_view.receive_json()["light"]["on"] is True


def test_physical_button_toggles_light():
    client, hw = make_client()
    with client:
        client.post("/api/demo/button")
        assert client.get("/api/state").json()["light"] == {"on": True, "source": "taster"}
        assert hw.light_on is True


def test_scenario_and_hint_done():
    client, _ = make_client()
    with client:
        snap = client.post("/api/demo/scenario", json={"name": "zu-trocken"}).json()
        assert snap["status"]["level"] == "now"
        snap = client.post("/api/hints/zu-trocken/done").json()
        assert snap["hints"][0]["resolving"] is True
        assert snap["climate"]["humidity_trend"] == "rising"
        assert client.post("/api/hints/gibt-es-nicht/done").status_code == 404
        assert client.post("/api/demo/scenario", json={"name": "unbekannt"}).status_code == 404


def test_display_is_served():
    client, _ = make_client()
    with client:
        assert "Licht" in client.get("/").text
        assert "Vorführ-Panel" in client.get("/demo/").text


def test_simulator_brings_humidity_back():
    async def scenario():
        model = BoxModel(SimulatedHardware())
        sim = Simulator(model)
        await sim.apply("zu-trocken")
        await sim.resolve("zu-trocken")
        for _ in range(20):
            await sim.step()
        return model.snapshot()

    snap = asyncio.run(scenario())
    assert snap["status"]["level"] == "ok"
    assert snap["hints"] == []
    assert snap["climate"]["humidity_trend"] is None
