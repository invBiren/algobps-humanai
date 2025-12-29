"""
FastAPI mStock proxy/router

Place this file into your backend project (e.g. move/copy into
`C:\algobps-humanai\backend`), then include the router in your main app:

from backend_mstock_proxy import router as mstock_router
app.include_router(mstock_router)

This router implements the following endpoints for the frontend:
- POST /auth/login         -> proxies to mStock /connect/login (form-urlencoded)
- POST /auth/session       -> proxies to mStock /session/token (form-urlencoded)
- POST /auth/verifytotp    -> proxies to mStock /session/verifytotp (form-urlencoded)
- GET  /auth/logout        -> proxies to mStock /user/logout (GET with Authorization header)

It accepts form-data or JSON where sensible, and returns the mStock response JSON (status code and body).

Security note: Do NOT embed your `api_key` or `access_token` in client-side code. The proxy allows you to keep secrets server-side.
"""

from fastapi import APIRouter, Request, Form, HTTPException, Header
from fastapi.responses import JSONResponse
import httpx
from typing import Optional

router = APIRouter()
MSTOCK_BASE = "https://api.mstock.trade/openapi/typea"
MIRA_VERSION = "1"

async def forward_post(path: str, data: dict):
    url = f"{MSTOCK_BASE}{path}"
    headers = {
        "X-Mirae-Version": MIRA_VERSION,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.post(url, data=data, headers=headers)
        # Try to return JSON if possible
        try:
            body = r.json()
        except Exception:
            body = {"raw": r.text}
        return r.status_code, body

@router.post("/auth/login")
async def auth_login(request: Request, username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    """
    Accepts form-data (preferred) or JSON body with `username` and `password`.
    Proxies to mStock connect/login endpoint which expects x-www-form-urlencoded.
    """
    if not (username and password):
        # try JSON body
        try:
            body = await request.json()
        except Exception:
            body = {}
        username = username or body.get("username")
        password = password or body.get("password")

    if not (username and password):
        raise HTTPException(status_code=400, detail="username and password are required")

    data = {"username": username, "password": password}
    status, body = await forward_post("/connect/login", data)
    return JSONResponse(status_code=status, content=body)

@router.post("/auth/session")
async def auth_session(request: Request, api_key: Optional[str] = Form(None), request_token: Optional[str] = Form(None), checksum: Optional[str] = Form(None)):
    """
    Accepts form-data or JSON with `api_key`, `request_token` (OTP), `checksum`.
    Proxies to mStock /session/token and returns the response.
    """
    if not (api_key and request_token and checksum):
        try:
            body = await request.json()
        except Exception:
            body = {}
        api_key = api_key or body.get("api_key")
        request_token = request_token or body.get("request_token") or body.get("otp")
        checksum = checksum or body.get("checksum")

    if not (api_key and request_token and checksum):
        raise HTTPException(status_code=400, detail="api_key, request_token (OTP) and checksum are required")

    data = {"api_key": api_key, "request_token": request_token, "checksum": checksum}
    status, body = await forward_post("/session/token", data)
    return JSONResponse(status_code=status, content=body)

@router.post("/auth/verifytotp")
async def auth_verifytotp(request: Request, api_key: Optional[str] = Form(None), totp: Optional[str] = Form(None)):
    """
    Accepts form-data or JSON with `api_key` and `totp`, proxies to mStock /session/verifytotp.
    """
    if not (api_key and totp):
        try:
            body = await request.json()
        except Exception:
            body = {}
        api_key = api_key or body.get("api_key")
        totp = totp or body.get("totp")

    if not (api_key and totp):
        raise HTTPException(status_code=400, detail="api_key and totp are required")

    data = {"api_key": api_key, "totp": totp}
    status, body = await forward_post("/session/verifytotp", data)
    return JSONResponse(status_code=status, content=body)

@router.get("/auth/logout")
async def auth_logout(authorization: Optional[str] = Header(None)):
    """
    Proxies logout to mStock `/user/fundsummary` or `/logout` depending on doc.
    The mStock logout endpoint in docs is `GET /user/logout` with Authorization: token api_key:access_token
    Pass the client Authorization header through.
    """
    if not authorization:
        raise HTTPException(status_code=400, detail="Authorization header required (token api_key:access_token)")

    url = f"{MSTOCK_BASE}/logout"
    headers = {"X-Mirae-Version": MIRA_VERSION, "Authorization": authorization}
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(url, headers=headers)
        try:
            body = r.json()
        except Exception:
            body = {"raw": r.text}
        return JSONResponse(status_code=r.status_code, content=body)

# Additional helper endpoints for fundsummary as example
@router.get("/user/fundsummary")
async def user_fundsummary(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=400, detail="Authorization header required (token api_key:access_token)")
    url = f"{MSTOCK_BASE}/user/fundsummary"
    headers = {"X-Mirae-Version": MIRA_VERSION, "Authorization": authorization}
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(url, headers=headers)
        try:
            body = r.json()
        except Exception:
            body = {"raw": r.text}
        return JSONResponse(status_code=r.status_code, content=body)
