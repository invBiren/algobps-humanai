def apply_risk(STATE):
    if STATE["pnl"] <= STATE["risk"]["mtm"]:
        STATE["algo"] = False
