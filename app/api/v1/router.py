from fastapi import APIRouter

from app.api.v1.endpoints import decision
from app.api.v1.endpoints import xai
from app.api.v1.endpoints import tradingview
from app.api.v1.endpoints import gold_dashboard

router = APIRouter()

router.include_router(decision.router)
router.include_router(tradingview.router)
router.include_router(gold_dashboard.router)
