from fastapi import APIRouter, WebSocket
import asyncio
import random

router = APIRouter()

@router.websocket("/pnl")
async def pnl_stream(ws: WebSocket):
    await ws.accept()
    pnl = 0.0
    try:
        while True:
            pnl += random.uniform(-250, 300)
            await ws.send_json({"pnl": round(pnl, 2)})
            await asyncio.sleep(1)
    except:
        return
