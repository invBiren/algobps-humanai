def trail_sl(entry, ltp, sl, trail=5):
    if ltp - entry > trail:
        return max(sl, ltp - trail)
    return sl
