import requests
from backend.broker.mstock_auth import auth_headers

BASE = "https://api.mstock.trade/openapi/typea"

def safe_get(url):
    r = requests.get(url, headers=auth_headers(), timeout=10)
    if r.status_code != 200:
        return {"status": "error", "data": None}
    return r.json()

def get_orders():
    return safe_get(f"{BASE}/orders")

def get_positions():
    return safe_get(f"{BASE}/positions")

def get_funds():
    return safe_get(f"{BASE}/user/fundsummary")
