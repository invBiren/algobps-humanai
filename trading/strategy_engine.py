import random
def generate_signal():
    if random.random() > 0.7:
        return {"symbol":"NIFTY","side":"BUY"}
