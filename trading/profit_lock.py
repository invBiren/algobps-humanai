from trading.position_book import POSITION_BOOK
from ws_market import LAST_PRICE
from trading.paper_engine import PAPER_ENGINE
from system_state import SYSTEM_STATE


PROFIT_TRIGGER = 20      # points in profit to activate lock
TRAIL_DISTANCE = 10      # points behind price


def profit_lock_check():
    for trade_id, pos in list(POSITION_BOOK.all().items()):
        symbol = pos["symbol"]
        entry = pos["entry_price"]
        qty = pos["quantity"]

        current_price = LAST_PRICE.get(symbol)
        if current_price is None:
            continue

        pnl_points = current_price - entry

        # Activate zero-loss
        if pnl_points >= PROFIT_TRIGGER:
            new_sl = max(pos["sl"], entry)

            # Trail SL further
            trailing_sl = current_price - TRAIL_DISTANCE
            new_sl = max(new_sl, trailing_sl)

            if new_sl > pos["sl"]:
                pos["sl"] = new_sl
                SYSTEM_STATE.raise_alert(
                    f"SL moved to {new_sl:.2f} for {symbol}"
                )

        # Exit on SL
        if current_price <= pos["sl"]:
            PAPER_ENGINE.exit_trade(trade_id, current_price)
            SYSTEM_STATE.raise_alert(
                f"PROFIT LOCK EXIT {symbol} @ {current_price:.2f}"
            )
