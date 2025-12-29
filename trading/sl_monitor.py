import asyncio

from trading.position_book import POSITION_BOOK
from ws_market import LAST_PRICE
from trading.paper_engine import PAPER_ENGINE
from system_state import SYSTEM_STATE
from trading.profit_lock import profit_lock_check


async def sl_monitor_loop():
    while True:
        profit_lock_check()
        await asyncio.sleep(1)
