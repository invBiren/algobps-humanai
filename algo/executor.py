import time
from backend.strategy.ema_rsi import ema, rsi

RUNNING = False

def start(prices):
    global RUNNING
    RUNNING = True
    while RUNNING:
        if ema(prices) > prices[-1] and rsi(prices) > 60:
            print("BUY SIGNAL")
        time.sleep(1)

def stop():
    global RUNNING
    RUNNING = False
