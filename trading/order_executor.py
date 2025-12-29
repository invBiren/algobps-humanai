from backend.broker.mstock_api import place_order

def execute_order(symbol, side, qty, price=None, order_type="MARKET"):
    return place_order({
        "symbol": symbol,
        "side": side,
        "quantity": qty,
        "order_type": order_type,
        "price": price
    })
