import asyncio
from starlette.websockets import WebSocketDisconnect

PRICES = {
    "NIFTY": 22500,
    "BANKNIFTY": 48200
}

async def ltp_feed(ws):
    try:
        while True:
            await ws.send_json(PRICES)
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        return
