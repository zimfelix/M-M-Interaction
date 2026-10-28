"""Simulierte Messwerte (Feuchte, Temperatur) und Vorführ-Szenarien."""

from .scenarios import SCENARIOS
from .simulator import Simulator

__all__ = ["SCENARIOS", "Simulator"]
