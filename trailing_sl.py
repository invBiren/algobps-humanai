import time, requests

def trailing_sl(session, trail=20):
    highest = 0

    while True:
        try:
            headers = {
                "X-Mirae-Version": "1",
                "Authorization": f"token {session['api_key']}:{session['access_token']}"
            }

            r = requests.get(
                "https://api.mstock.trade/openapi/typea/user/positions",
                headers=headers
            ).json()

            pnl = sum(p.get("pnl", 0) for p in r.get("data", []))
            highest = max(highest, pnl)

            if pnl < highest - trail:
                requests.post(
                    "https://api.mstock.trade/openapi/typea/positions/squareoff",
                    headers=headers
                )
                break

        except:
            pass

        time.sleep(3)
