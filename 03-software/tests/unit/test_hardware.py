from growbox.hardware import SimulatedHardware, create_hardware


def test_simulation_can_be_forced(monkeypatch):
    monkeypatch.setenv("MM_HARDWARE", "sim")
    assert isinstance(create_hardware(), SimulatedHardware)


def test_falls_back_to_simulation_without_gpio(monkeypatch):
    monkeypatch.delenv("MM_HARDWARE", raising=False)
    assert create_hardware().name in {"simuliert", "gpiozero"}
