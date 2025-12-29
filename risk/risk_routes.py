from fastapi import APIRouter
from backend.risk.risk_guard import check_risk

router = APIRouter(prefix="/risk")

@router.get("/check")
def risk(pnl:float):
    return {"action": check_risk(pnl)}
