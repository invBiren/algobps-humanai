from fastapi import APIRouter, HTTPException
import requests
from backend.session_store import SESSION

router = APIRouter()

MSTOCK_ORDER_URL = "https://api.mstock.trade/openapi/typea/orders/place"

@router.post("/orders/place")
def place_order(
    exchange: str,
    tradingsymbol: str,
    quantity: int,
    transaction_type: str,
    order_type: str = "MARKET",
    product: str = "MIS"
):
    if not SESSION.get("connected"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    headers = {
        "X-Mirae-Version": "1",
        "Authorization": f"token {SESSION['api_key']}:{SESSION['access_token']}",
        "Content-Type": "application/json"
    }

    payload = {
        "exchange": exchange,
        "tradingsymbol": tradingsymbol,
        "quantity": quantity,
        "transaction_type": transaction_type,
        "order_type": order_type,
        "product": product
    }

    r = requests.post(MSTOCK_ORDER_URL, json=payload, headers=headers)

    if r.status_code != 200:
        raise HTTPException(status_code=500, detail=r.text)

    return r.json()
