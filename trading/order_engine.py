from backend.session_store import SESSION

ORDERS=[]
TRAILS={}

def place_order(symbol, side, qty, price=None, sl=None, target=None):
    o={
        "symbol":symbol,"side":side,"qty":qty,
        "price":price,"sl":sl,"target":target,
        "status":"OPEN"
    }
    ORDERS.append(o)
    if sl:
        TRAILS[symbol]=sl
    return o

def update_ltp(symbol, ltp):
    if symbol in TRAILS:
        if ltp>TRAILS[symbol]:
            TRAILS[symbol]=ltp-5
    for o in ORDERS:
        if o["symbol"]==symbol and o["sl"] and ltp<=TRAILS[symbol]:
            o["status"]="SL_HIT"
