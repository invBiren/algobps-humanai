from fastapi import APIRouter
from backend.session_store import SESSION

router = APIRouter()

@router.post("/algo/start")
def start_algo():
    SESSION["algo_running"] = True
    return {"status": "algo_started"}

@router.post("/algo/stop")
def stop_algo():
    SESSION["algo_running"] = False
    return {"status": "algo_stopped"}

@router.get("/risk/guard")
def risk_guard():
    if SESSION["pnl"] <= SESSION["mtm_limit"]:
        SESSION["algo_running"] = False
        return {"status": "algo_stopped_by_risk"}
    return {"status": "ok"}
