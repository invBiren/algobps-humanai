TRAILS = {}

def update(symbol, ltp, sl, step=5):
    if symbol not in TRAILS:
        TRAILS[symbol] = sl
    if ltp - TRAILS[symbol] > step:
        TRAILS[symbol] = ltp - step
    return TRAILS[symbol]
