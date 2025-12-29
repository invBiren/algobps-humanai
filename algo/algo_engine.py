import time, threading
from backend.session_store import SESSION
from backend.trading.order_engine import place_order

RUNNING=False

def ema_strategy(symbol):
    global RUNNING
    RUNNING=True
    price=100
    while RUNNING:
        price+=1
        if price%5==0:
            place_order(symbol,"BUY",1)
        time.sleep(2)

def start(symbol):
    t=threading.Thread(target=ema_strategy,args=(symbol,))
    t.start()

def stop():
    global RUNNING
    RUNNING=False
