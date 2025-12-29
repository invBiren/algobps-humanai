from trading.trade_journal import TRADE_JOURNAL
from trading.risk_guard import RISK_GUARD


class ZeroLossEngine:
    def __init__(self):
        self.trade_count = 0

    def reset(self):
        self.trade_count = 0

    def last_profit(self):
        trades = TRADE_JOURNAL.all()
        if not trades:
            return 0
        return trades[-1]["pnl"]

    def can_enter_trade(self, expected_profit):
        """
        Decide whether a new trade is allowed
        """
        self.trade_count += 1

        # Hard stop
        if self.trade_count > 5:
            return False, "Max trades reached"

        # First trade logic
        if self.trade_count == 1:
            if expected_profit < 1000:
                return False, "Trade-1 must have ≥ ₹1000 asymmetry"
            return True, "Trade-1 allowed"

        # Subsequent trades
        last_pnl = self.last_profit()

        # If last trade lost → reset
        if last_pnl <= 0:
            self.reset()
            return False, "Loss detected — reset to Trade-1 logic"

        # Dynamic SL logic
        allowed_sl = last_pnl * 0.10
        return True, f"Allowed with SL ≤ ₹{allowed_sl:.2f}"


ZERO_LOSS_ENGINE = ZeroLossEngine()
