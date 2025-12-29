JOURNAL=[]
def log_trade(symbol,qty,side,result):
    JOURNAL.append({
        "symbol":symbol,
        "qty":qty,
        "side":side,
        "result":str(result)
    })
