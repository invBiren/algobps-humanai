from fastapi import APIRouter

router = APIRouter()

ORDERS = []
POSITIONS = {}
PNL = 0.0

@router.get("/orders")
def orders():
    return ORDERS

@router.get("/positions")
def positions():
    return POSITIONS

@router.get("/pnl")
def pnl():
    return {"pnl": PNL}

@router.post("/buy/{symbol}")
def buy(symbol: str, qty: int = 1):
    POSITIONS[symbol] = POSITIONS.get(symbol, 0) + qty
    ORDERS.append({"symbol": symbol, "qty": qty, "side": "BUY"})
    return {"status": "OK"}

@router.post("/sell/{symbol}")
def sell(symbol: str, qty: int = 1):
    POSITIONS[symbol] = POSITIONS.get(symbol, 0) - qty
    ORDERS.append({"symbol": symbol, "qty": qty, "side": "SELL"})
    return {"status": "OK"}

@router.post("/squareoff")
def squareoff():
    POSITIONS.clear()
    return {"status": "SQUARED"}
