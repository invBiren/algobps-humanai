import requests

def fetch_orderbook(session):
    headers = {
        "X-Mirae-Version": "1",
        "Authorization": f"token {session['api_key']}:{session['access_token']}"
    }
    return requests.get(
        "https://api.mstock.trade/openapi/typea/orders",
        headers=headers
    ).json()
