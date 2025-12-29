MAX_LOSS = -5000

def check(pnl):
    if pnl < MAX_LOSS:
        return True
    return False
