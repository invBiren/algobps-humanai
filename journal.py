import json, datetime

FILE = "trades.json"

def log_trade(order):
    entry = {
        "time": str(datetime.datetime.now()),
        "order": order
    }

    try:
        data = json.load(open(FILE))
    except:
        data = []

    data.append(entry)
    json.dump(data, open(FILE, "w"), indent=2)
