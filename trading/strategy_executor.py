import threading, time
from backend.session_store import SESSION

_running = False

def start_strategy():
    global _running
    _running = True
    threading.Thread(target=_loop, daemon=True).start()

def stop_strategy():
    global _running
    _running = False

def _loop():
    while _running:
        if not SESSION.get("connected"):
            time.sleep(1); continue
        # TODO: fetch LTP → compute EMA/RSI → place orders
        time.sleep(2)
