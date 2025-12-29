import time, threading
from backend.session_store import SESSION

SESSION["equity"]=[100000]

def simulate():
    while True:
        SESSION["equity"].append(SESSION["equity"][-1]+10)
        time.sleep(3)

threading.Thread(target=simulate,daemon=True).start()
