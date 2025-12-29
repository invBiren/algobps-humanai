from fastapi import APIRouter
from backend.session_store import SESSION

router = APIRouter()

@router.get("/session/authority")
def authority():
    return SESSION
