from fastapi import APIRouter, WebSocket
import asyncio
import random

router = APIRouter()

@router.websocket("/ws/pnl")
async def pnl_socket(ws: WebSocket):
    await ws.accept()
    pnl = 0
    while True:
        pnl += random.randint(-20, 50)
        await ws.send_text(str(pnl))
        await asyncio.sleep(1)
