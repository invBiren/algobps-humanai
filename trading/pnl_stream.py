async def pnl_feed(ws):
    while True:
        await ws.send_json({
            "pnl": 1250.75,
            "day_pnl": 3420.10
        })
        await asyncio.sleep(1)
