from trading.zero_loss_engine import ZERO_LOSS_ENGINE
from trading.risk_guard import RISK_GUARD


class TradeAdvisor:

    def evaluate(self, proposal: dict):
        """
        proposal = {
            symbol, price, sl, quantity, expected_profit, strategy
        }
        """

        capital = proposal["price"] * proposal["quantity"]
        allowed, reason = RISK_GUARD.can_trade(capital)
        if not allowed:
            return self.reject(reason)

        allowed, z_reason = ZERO_LOSS_ENGINE.can_enter_trade(
            proposal["expected_profit"]
        )
        if not allowed:
            return self.reject(z_reason)

        rr = abs(proposal["expected_profit"]) / max(
            abs(proposal["price"] - proposal["sl"]), 1
        )

        return {
            "decision": "APPROVE",
            "summary": {
                "risk_reward": round(rr, 2),
                "capital_used": capital,
                "logic": z_reason
            },
            "explanation": (
                "Trade meets zero-loss and risk criteria. "
                "Asymmetric payoff detected."
            )
        }

    def reject(self, reason):
        return {
            "decision": "REJECT",
            "reason": reason,
            "explanation": (
                "Trade violates capital or zero-loss constraints."
            )
        }


AI_ADVISOR = TradeAdvisor()
