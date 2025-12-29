from fastapi import WebSocket
import asyncio
from backend.portfolio.pnl_engine import portfolio_pnl

async def pnl_stream(ws: WebSocket):
    await ws.accept()
    ltp = {"NIFTY":100,"BANKNIFTY":200}

    while True:
        pnl = portfolio_pnl(ltp)
        await ws.send_json({"pnl": pnl})
        await asyncio.sleep(1)
