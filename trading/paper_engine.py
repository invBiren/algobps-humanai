from fastapi import APIRouter
from backend.trading.position_book import POSITION_BOOK

router = APIRouter()

ALGO_RUNNING = False

@router.post("/algo/start")
def start_algo():
    global ALGO_RUNNING
    ALGO_RUNNING = True

    POSITION_BOOK.append({
        "symbol": "NIFTY",
        "qty": 1,
        "avg_price": 22000,
        "pnl": 100
    })

    return {"status": "started"}

@router.post("/algo/stop")
def stop_algo():
    global ALGO_RUNNING
    ALGO_RUNNING = False
    return {"status": "stopped"}
