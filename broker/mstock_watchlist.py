import requests
from backend.session_store import SESSION

BASE = "https://api.mstock.trade/openapi/typea"

def auth_headers():
    return {
        "X-Mirae-Version": "1",
        "Authorization": f"token {SESSION['api_key']}:{SESSION['access_token']}"
    }

def get_watchlist():
    r = requests.get(
        f"{BASE}/user/watchlist",
        headers=auth_headers(),
        timeout=10
    )
    if r.status_code != 200:
        raise Exception(r.text)
    return r.json()
