def build_bracket(order):
    entry = order["price"]
    sl = entry - order["sl"] if order["side"] == "BUY" else entry + order["sl"]
    target = entry + order["target"] if order["side"] == "BUY" else entry - order["target"]

    return {
        "entry": entry,
        "sl": sl,
        "target": target,
        "active": True
    }
