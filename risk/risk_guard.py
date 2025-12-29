MAX_LOSS = -5000

def check_risk(pnl):
    return pnl <= MAX_LOSS
