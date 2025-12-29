from backend.strategy.ema_rsi import ema, rsi
from backend.trading.order_executor import execute_order
from backend.risk.risk_guard import check_risk

def run_strategy(symbol, prices, qty):
    e = ema(prices)
    r = rsi(prices)

    if r < 30:
        execute_order(symbol, "BUY", qty)
    elif r > 70:
        execute_order(symbol, "SELL", qty)

def enforce_risk(pnl, positions):
    if check_risk(pnl):
        for p in positions:
            execute_order(p["symbol"], "SELL", p["qty"])
