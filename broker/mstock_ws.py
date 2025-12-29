import json
import threading
import websocket
import time

from broker.mstock_session import MSTOCK_SESSION
from broker.mstock_state import MSTOCK_STATE

class MStockWebSocket:
    def __init__(self):
        self.ws = None
        self.latest_price = None
        self.connected = False

    def connect(self):
        if not MSTOCK_SESSION.is_active():
            return

        def on_message(ws, message):
            data = json.loads(message)
            price = data.get("ltp")
            if price:
                self.latest_price = price

        def on_error(ws, error):
            self.connected = False
            MSTOCK_STATE.set_disconnected("Market feed error")

        def on_close(ws):
            self.connected = False
            MSTOCK_STATE.set_disconnected("Market feed disconnected")

        def on_open(ws):
            self.connected = True
            MSTOCK_STATE.last_message = "Market feed connected"

            # Subscribe (example – real payload may differ)
            sub_payload = {
                "action": "subscribe",
                "symbols": ["NIFTY 50"]
            }
            ws.send(json.dumps(sub_payload))

        self.ws = websocket.WebSocketApp(
            "wss://api.mstock.com/marketdata",  # official WS endpoint
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )

        threading.Thread(target=self.ws.run_forever, daemon=True).start()

    def get_price(self):
        return self.latest_price


MSTOCK_WS = MStockWebSocket()
