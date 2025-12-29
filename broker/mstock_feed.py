import random
from broker.mstock_ws import MSTOCK_WS
from broker.mstock_session import MSTOCK_SESSION
from system_state import SYSTEM_STATE

class FeedController:
    def get_price(self):
        # Use real feed only if authenticated & connected
        if MSTOCK_SESSION.is_active() and MSTOCK_WS.connected:
            price = MSTOCK_WS.get_price()
            if price:
                return price

        # Fallback to mock
        SYSTEM_STATE.add_alert(
            "warning",
            "Using mock market data (real feed unavailable)"
        )
        return round(100 + random.uniform(-1, 1), 2)


FEED = FeedController()
