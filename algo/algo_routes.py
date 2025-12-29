from fastapi import APIRouter

router = APIRouter()
RUNNING = False

@router.get("/start")
def start():
    global RUNNING
    RUNNING = True
    return {"running": True}

@router.get("/stop")
def stop():
    global RUNNING
    RUNNING = False
    return {"running": False}

@router.get("/status")
def status():
    return {"running": RUNNING}
