"""Live-Updates: jede verbundene Ansicht bekommt jeden neuen Zustand (WS /ws)."""

from __future__ import annotations

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from ..core import BoxModel


class LiveClients:
    """Alle offenen WebSocket-Verbindungen (Display, App, Demo-Panel)."""

    def __init__(self) -> None:
        self._clients: set[WebSocket] = set()

    async def broadcast(self, snapshot: dict) -> None:
        for ws in list(self._clients):
            try:
                await ws.send_json(snapshot)
            except Exception:
                self._clients.discard(ws)

    def router(self, model: BoxModel) -> APIRouter:
        router = APIRouter()

        @router.websocket("/ws")
        async def live(ws: WebSocket) -> None:
            """Schickt sofort den Zustand und danach jede Änderung."""
            await ws.accept()
            self._clients.add(ws)
            try:
                await ws.send_json(model.snapshot())
                while True:
                    await ws.receive_text()  # Clients senden nichts; hält die Verbindung offen
            except WebSocketDisconnect:
                pass
            finally:
                self._clients.discard(ws)

        return router
