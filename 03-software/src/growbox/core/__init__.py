"""Stabiler Kern: Zustand und Regeln. Kennt weder FastAPI noch GPIO."""

from .rules import evaluate
from .state import BoxModel, BoxState

__all__ = ["BoxModel", "BoxState", "evaluate"]
