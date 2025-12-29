BACKEND /auth/login Fix

What this file does
- Explains a minimal FastAPI change to ensure `/auth/login` accepts POST (both form-data and JSON).
- Shows how to apply the change and verify the server.

Important: I cannot edit files outside the workspace. Please copy the snippet below into your backend route file (likely `C:\algobps-humanai\backend\main.py` or the router file where `/auth/...` are defined).

1) Backup your file before editing (PowerShell):

```powershell
Copy-Item 'C:\algobps-humanai\backend\main.py' 'C:\algobps-humanai\backend\main.py.bak'
```

2) Insert (or replace existing `/auth/login` handler) with the snippet below.

Snippet (FastAPI) — paste into your backend route file

```python
# --- BEGIN SNIPPET ---
from fastapi import Request, Form, HTTPException

# If your app variable is named `app` (FastAPI instance) use @app.post
# If you use APIRouter (`router = APIRouter()`), change decorator to @router.post('/login')
@app.post("/auth/login")
async def auth_login(request: Request,
                     api_key: str = Form(None),
                     username: str = Form(None),
                     password: str = Form(None)):
    """
    Accepts credentials either as form-data (preferred by current frontend)
    or JSON (fallback). Returns OTP/send-login response.
    """
    # If no form values were provided and content-type is JSON, read JSON
    if (api_key is None or username is None or password is None) and request.headers.get("content-type", "").startswith("application/json"):
        try:
            body = await request.json()
        except Exception:
            body = {}
        api_key = api_key or body.get("api_key")
        username = username or body.get("username")
        password = password or body.get("password")

    # Validate input
    if not (api_key and username and password):
        raise HTTPException(status_code=400, detail="Missing api_key, username or password")

    # ----- Integrate your existing auth/OTP logic here -----
    # Example placeholder behaviour: verify credentials and send OTP
    # Replace the logic below with your project's implementation.

    # Example: pretend to send OTP and return success
    return {"status": "ok", "detail": "OTP sent (placeholder)"}

# --- END SNIPPET ---
```

3) If your backend uses routers with prefix `/auth`
- If your router is included like `app.include_router(router, prefix='/auth')`, then use:

```python
@router.post('/login')
async def auth_login(...):
    # same body
```

4) Restart the server (from parent folder of `backend`) in PowerShell:

```powershell
Set-Location 'C:\algobps-humanai'
uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

(Make sure to use two hyphens `--reload`.)

5) Verify routes and test
- Create and run the helper `print_routes.py` (below) to confirm `/auth/login` allows POST.
- Use the sample PowerShell tests described in this package to check OPTIONS and POST.

If you'd like, paste the original handler here and I will prepare a precise in-place diff for you to apply.

If anything goes wrong, restore backup:
```powershell
Move-Item -Path 'C:\algobps-humanai\backend\main.py.bak' -Destination 'C:\algobps-humanai\backend\main.py' -Force
```

End of instructions.
