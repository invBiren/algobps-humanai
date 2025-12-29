from fastapi import APIRouter

router = APIRouter()

POSITION_BOOK = [
    {"symbol": "NIFTY", "qty": 1, "avg_price": 22000, "pnl": 0}
]

@router.get("/user/positions")
def get_positions():
    return POSITION_BOOK

@router.post("/positions/squareoff")
def squareoff_all():
    POSITION_BOOK.clear()
    return {"status": "success", "message": "All positions squared off"}
