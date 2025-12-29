import time

class StrategyExecutor:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("STRATEGY STARTED")

    def stop(self):
        self.running = False
        print("STRATEGY STOPPED")

    def tick(self, ltp, ema, rsi):
        if not self.running:
            return None

        if rsi < 30 and ltp > ema:
            return "BUY"

        if rsi > 70 and ltp < ema:
            return "SELL"

        return None
