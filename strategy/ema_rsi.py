def ema(prices, period=9):
    k = 2 / (period + 1)
    ema_val = prices[0]
    for p in prices[1:]:
        ema_val = p * k + ema_val * (1 - k)
    return ema_val

def rsi(prices, period=14):
    gains, losses = [], []
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        gains.append(max(diff, 0))
        losses.append(abs(min(diff, 0)))
    if not losses or sum(losses) == 0:
        return 100
    rs = (sum(gains) / period) / (sum(losses) / period)
    return 100 - (100 / (1 + rs))
