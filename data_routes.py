from fastapi import APIRouter
from backend.broker.mstock_data import get_orders, get_positions, get_funds

router = APIRouter()

@router.get("/orders", name="orders_list")
def orders():
    return get_orders()

@router.get("/positions", name="positions_list")
def positions():
    return get_positions()

@router.get("/funds", name="funds_list")
def funds():
    return get_funds()

from backend.broker.mstock_watchlist import get_watchlist

@router.get("/watchlist")
def watchlist():
    return get_watchlist()
