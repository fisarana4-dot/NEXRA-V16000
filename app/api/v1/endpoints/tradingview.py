import hashlib
import hmac
import json

from fastapi import APIRouter, Header, HTTPException, Request, status
from datetime import datetime; from app.core.evidence.store import init,save
from app.core.config import settings
from app.core.evidence.contract import Evidence
from app.trading.gold.connectors.tradingview import TradingViewConnector
connector=TradingViewConnector()
from app.trading.gold.strategy.strategy_engine import strategy
router=APIRouter(prefix="/tradingview",tags=["tradingview"])

def verify_webhook_signature(body: bytes, signature: str | None) -> None:
 secret = settings.TRADINGVIEW_WEBHOOK_SECRET
 if not secret or not signature:
  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid webhook signature")
 expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
 if not hmac.compare_digest(signature, expected):
  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid webhook signature")

@router.post("/webhook")
async def tradingview_webhook(request: Request, x_tradingview_signature: str | None = Header(default=None)):
 body = await request.body()
 verify_webhook_signature(body, x_tradingview_signature)
 try:
  payload = json.loads(body)
 except json.JSONDecodeError as exc:
  raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid JSON payload") from exc
 if not isinstance(payload, dict):
  raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Webhook payload must be an object")
 tv=connector.parse(payload);init();save(Evidence("TRADINGVIEW","GOLD",tv,datetime.utcnow().isoformat(),{}),"pending")
 return {"status":"received","source":"TradingView","decision":strategy.run(tv),"tv_data":tv}
