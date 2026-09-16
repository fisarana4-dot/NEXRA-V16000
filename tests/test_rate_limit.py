from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.core.rate_limit import RateLimitMiddleware
class R:
 def __init__(s): s.d={}
 async def incr(s,k): s.d[k]=s.d.get(k,0)+1; return s.d[k]
 async def expire(s,k,w): pass
def test_rate_limit(monkeypatch):
 r=R()
 async def gr(): return r
 monkeypatch.setattr("app.core.rate_limit.get_redis",gr)
 app=FastAPI()
 app.add_middleware(RateLimitMiddleware,limit=2,window=60)
 @app.get("/x")
 def x(): return {"ok":1}
 with TestClient(app) as c:
  assert c.get("/x").status_code==200
def test_rate_limit_blocks_after_limit(monkeypatch):
 r=R()
 async def gr(): return r
 monkeypatch.setattr("app.core.rate_limit.get_redis",gr)
 app=FastAPI()
 app.add_middleware(RateLimitMiddleware,limit=2,window=60)
 @app.get("/y")
 def y(): return {"ok":1}
 with TestClient(app) as c:
  assert c.get("/y").status_code==200
  assert c.get("/y").status_code==200
  assert c.get("/y").status_code==429
