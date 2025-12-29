from fastapi import APIRouter
from backend.session_store import SESSION

router = APIRouter()

@router.post("/order/place")
def place_order(symbol:str, side:str, qty:int, price:float|None=None):
    order = {
        "symbol": symbol,
        "side": side,
        "qty": qty,
        "price": price,
        "status": "placed"
    }
    SESSION.setdefault("orders", []).append(order)
    return order

@router.post("/order/bracket")
def bracket_order(symbol:str, side:str, qty:int, entry:float, sl:float, target:float):
    bo = {
        "symbol": symbol,
        "side": side,
        "qty": qty,
        "entry": entry,
        "sl": sl,
        "target": target,
        "type": "BRACKET"
    }
    SESSION.setdefault("orders", []).append(bo)
    return bo
