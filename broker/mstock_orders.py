import os

LIVE = os.getenv("LIVE_TRADING", "false") == "true"

def place_order(order):
    if not LIVE:
        return {"status": "SIMULATED", "order": order}

    # 🔥 REAL mStock API call here
    # requests.post("https://api.mstock.com/orders", ...)
    return {"status": "PLACED", "order": order}
