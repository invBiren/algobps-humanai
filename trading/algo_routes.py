from fastapi import APIRouter

router = APIRouter()
ALGO_RUNNING = False

@router.get("/start")
def start():
    global ALGO_RUNNING
    ALGO_RUNNING = True
    return {"algo": "running"}

@router.get("/stop")
def stop():
    global ALGO_RUNNING
    ALGO_RUNNING = False
    return {"algo": "stopped"}

@router.get("/status")
def status():
    return {"running": ALGO_RUNNING}
