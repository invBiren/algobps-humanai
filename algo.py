import time, requests

def simple_ema_strategy(session, symbol="NIFTY"):
    """
    Very basic demo strategy:
    BUY if available cash > threshold
    """
    try:
        headers = {
            "X-Mirae-Version": "1",
            "Authorization": f"token {session['api_key']}:{session['access_token']}",
            "Content-Type": "application/json"
        }

        # Example logic placeholder
        order = {
            "exchange": "NSE",
            "tradingsymbol": symbol,
            "quantity": 1,
            "transaction_type": "BUY",
            "order_type": "MARKET",
            "product": "MIS"
        }

        requests.post(
            "https://api.mstock.trade/openapi/typea/orders/place",
            headers=headers,
            json=order
        )

    except Exception as e:
        print("Algo error:", e)
