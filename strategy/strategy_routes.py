from fastapi import APIRouter
from backend.strategy.strategy_engine import ema_strategy

router = APIRouter(prefix="/strategy")

@router.post("/ema")
def ema(prices:list):
    return {"signal": ema_strategy(prices)}
