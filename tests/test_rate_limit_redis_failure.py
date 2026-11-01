from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.core.rate_limit import RateLimitMiddleware
import app.core.rate_limit as rate_limit
from redis.exceptions import RedisError

def test_redis_incr_failure_fails_open(monkeypatch):
    app = FastAPI()
    class FakeRedis:
        async def incr(self, key):
            raise RedisError("Redis unavailable")
    redis = FakeRedis()
    async def fake_get_redis():
        return redis
    monkeypatch.setattr(rate_limit, "get_redis", fake_get_redis)
    app.add_middleware(RateLimitMiddleware)
    @app.get("/")
    def home():
        return {"status": "ok"}
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
