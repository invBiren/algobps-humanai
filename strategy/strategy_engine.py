def ema_strategy(prices):
    return "BUY" if prices[-1] > sum(prices[-5:])/5 else "SELL"

def rsi_strategy(rsi):
    return "BUY" if rsi < 30 else "SELL" if rsi > 70 else "HOLD"
