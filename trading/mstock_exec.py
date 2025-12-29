def place_real_order(symbol, qty, side):
    return {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "status": "LIVE_SENT"
    }
