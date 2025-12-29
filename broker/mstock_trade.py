import requests
from backend.session_store import SESSION

BASE = "https://api.mstock.trade/openapi/typea"

def headers():
    return {
        "X-Mirae-Version": "1",
        "Authorization": f"token {SESSION['api_key']}:{SESSION['access_token']}"
    }

def place_order(payload):
    r = requests.post(f"{BASE}/orders/place", headers=headers(), json=payload)
    return r.json()
