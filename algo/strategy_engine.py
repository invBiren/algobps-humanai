def should_buy(ema_fast, ema_slow, rsi):
    return ema_fast > ema_slow and rsi < 30

def should_sell(ema_fast, ema_slow, rsi):
    return ema_fast < ema_slow and rsi > 70
