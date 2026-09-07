import contextlib
from contextlib import asynccontextmanager
from app.core.database import init_db
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
@asynccontextmanager
async def lifespan(app):
    await init_db()
    yield
from app.api.v1.router import router
from app.api import auth
from app.api.v1.endpoints import decision, tradingview

app = FastAPI(title="NEXRA V16000", lifespan=lifespan)
FastAPIInstrumentor.instrument_app(app)
app.add_api_route("/health", lambda: {"status":"ok","system":"NEXRA V16000"}, methods=["GET"])

app.include_router(router)
app.include_router(auth.router)
app.include_router(decision.router)
app.include_router(tradingview.router)
