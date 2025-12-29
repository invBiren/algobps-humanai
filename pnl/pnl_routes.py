from fastapi import APIRouter
from backend.session_store import SESSION

router=APIRouter(prefix="/pnl")

@router.get("/equity")
def equity():
    return SESSION["equity"]
