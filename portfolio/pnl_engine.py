POSITIONS = []

def update_position(symbol, qty, price):
    POSITIONS.append({"symbol": symbol, "qty": qty, "price": price})

def portfolio_pnl(ltp_map):
    pnl = 0
    for p in POSITIONS:
        pnl += (ltp_map.get(p["symbol"], p["price"]) - p["price"]) * p["qty"]
    return round(pnl, 2)
