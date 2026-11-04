from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.core.rate_limit import RateLimitMiddleware
import app.core.rate_limit as rate_limit

def test_rate_limit_middleware(monkeypatch):
    app = FastAPI()
    class FakeRedis:
        def __init__(self):
            self.count = 0
        async def incr(self, key):
            self.count += 1
            return self.count
        async def expire(self, key, window):
            return True
    redis = FakeRedis()
    async def fake_get_redis():
        return redis
    monkeypatch.setattr(rate_limit, "get_redis", fake_get_redis)
    app.add_middleware(RateLimitMiddleware, limit=1, window=60)
    @app.get("/")
    def home():
        return {"status": "ok"}
    client = TestClient(app)
    first = client.get("/")
    assert first.status_code == 200
    second = client.get("/")
    assert second.status_code == 429
    assert second.json()["detail"] == "Rate limit exceeded"
