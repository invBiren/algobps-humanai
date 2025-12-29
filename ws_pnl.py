import asyncio, json, random
from backend.session_store import SESSION

async def pnl_ws(ws):
    await ws.accept()
    pnl = 0
    while True:
        await asyncio.sleep(1)
        pnl += random.randint(-300, 300)
        SESSION["pnl"] = pnl
        await ws.send_text(json.dumps({"pnl": pnl}))
