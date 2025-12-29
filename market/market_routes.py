from fastapi import APIRouter, WebSocket
from backend.market.ltp_ws import ltp_feed

router = APIRouter()

@router.websocket("/ltp")
async def ltp_socket(ws: WebSocket):
    await ws.accept()
    await ltp_feed(ws)
