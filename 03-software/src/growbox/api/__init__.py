"""Web-Schnittstelle für Display, App und Demo-Panel (Details: 03-software/API.md)."""

from .routes import build_router
from .websocket import LiveClients

__all__ = ["LiveClients", "build_router"]
