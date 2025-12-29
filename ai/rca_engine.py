class RCAEngine:

    def analyze(self, trade: dict):
        pnl = trade["pnl"]

        if pnl > 0:
            verdict = "GOOD TRADE"
            improvement = "Consider scaling position next time."
        else:
            verdict = "AVOIDABLE LOSS"
            improvement = (
                "Entry timing or SL placement could be refined."
            )

        return {
            "verdict": verdict,
            "pnl": pnl,
            "learning": improvement
        }


RCA_ENGINE = RCAEngine()
