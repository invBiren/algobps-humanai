def update_trailing_sl(pos, ltp):
    if pos["side"] == "BUY":
        new_sl = max(pos["sl"], ltp - pos["trail"])
        pos["sl"] = new_sl
    else:
        new_sl = min(pos["sl"], ltp + pos["trail"])
        pos["sl"] = new_sl
    return pos
