class RateLimitMiddleware:
 def __init__(self,app,limit=60,window=60):
  pass
from app.core.redis import get_redis
from redis.exceptions import RedisError
from starlette.responses import JSONResponse
class RateLimitMiddleware:
 def __init__(self,app,limit=60,window=60):
  self.app=app
  self.limit=limit
  self.window=window
 async def __call__(self,scope,receive,send):
  if scope["type"]!="http":
   return await self.app(scope,receive,send)
  r=await get_redis()
  key="nexra:rl:"+scope.get("path","/")
  try:
   count=await r.incr(key)
   if count==1:
    await r.expire(key,self.window)
   if count>self.limit:
    return await JSONResponse({"detail":"Rate limit exceeded"},status_code=429)(scope,receive,send)
  except RedisError:
   pass
  await self.app(scope,receive,send)
