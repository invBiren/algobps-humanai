import pandas as pd

def ema(series, n):
    return series.ewm(span=n).mean()

def rsi(series, n=14):
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(n).mean()
    loss = -delta.clip(upper=0).rolling(n).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def execute(df):
    df["ema_fast"] = ema(df["close"], 9)
    df["ema_slow"] = ema(df["close"], 21)
    df["rsi"] = rsi(df["close"])

    last = df.iloc[-1]

    if last.ema_fast > last.ema_slow and last.rsi > 55:
        return "BUY"
    if last.ema_fast < last.ema_slow and last.rsi < 45:
        return "SELL"

    return "HOLD"
