"""Formate der Anfragen (Request-Bodies) – erscheinen so auch in /docs."""

from __future__ import annotations

from pydantic import BaseModel, Field


class LightRequest(BaseModel):
    on: bool
    source: str = Field("app", description="Wer schaltet: display, app, demo")


class ScenarioRequest(BaseModel):
    name: str
