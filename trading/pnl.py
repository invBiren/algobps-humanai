def calculate_pnl(positions):
    total = 0
    for p in positions:
        total += (p["ltp"] - p["avg_price"]) * p["qty"]
    return total
