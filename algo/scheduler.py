import threading
import time

STRATEGIES = {}
RUNNING = False

def register(name, fn):
    STRATEGIES[name] = fn

def start():
    global RUNNING
    RUNNING = True
    threading.Thread(target=loop, daemon=True).start()

def stop():
    global RUNNING
    RUNNING = False

def loop():
    while RUNNING:
        for s in STRATEGIES.values():
            s()
        time.sleep(1)
