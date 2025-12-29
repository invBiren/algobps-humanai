class TradeJournal:
    def __init__(self):
        self.trades = []

    def record(self, trade):
        self.trades.append(trade)

    def all(self):
        return self.trades


TRADE_JOURNAL = TradeJournal()
