from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.broker.mstock_auth import login_mstock

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    api_key: str
    userId: str
    password: str

@router.post("/login")
def login(payload: LoginRequest):
    try:
        return login_mstock(
            payload.api_key,
            payload.userId,
            payload.password
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/session")
def session():
    return {"status": "active"}
