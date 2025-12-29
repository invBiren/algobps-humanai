from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from backend.auth_routes import router as auth_router
from backend.algo.algo_routes import router as algo_router
from backend.trading.trade_routes import router as trade_router
from backend.market.market_routes import router as market_router

app = FastAPI(title="AlgoBPS HumanAI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(algo_router, prefix="/algo", tags=["Algo"])
app.include_router(trade_router, prefix="/trade", tags=["Trade"])
app.include_router(market_router, prefix="/market", tags=["Market"])

# Frontend served on SAME PORT
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
