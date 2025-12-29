from backend.broker.mstock_orders import square_off_all

def square_off():
    square_off_all()


from backend.trading.squareoff import square_off

@router.get("/squareoff")
def squareoff_all():
    square_off(); return {"status":"squareoff_done"}
