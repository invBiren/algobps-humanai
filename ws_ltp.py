import asyncio, json, random
from fastapi import WebSocket, WebSocketDisconnect

clients=set()
symbols=["NIFTY","BANKNIFTY","RELIANCE","INFY"]

async def ltp_ws(ws: WebSocket):
    await ws.accept()
    clients.add(ws)
    try:
        while True:
            await asyncio.sleep(1)
            for sym in symbols:
                data={
                    "symbol":sym,
                    "ltp":round(1000+random.uniform(-20,20),2)
                }
                for c in list(clients):
                    await c.send_text(json.dumps(data))
    except WebSocketDisconnect:
        clients.remove(ws)
