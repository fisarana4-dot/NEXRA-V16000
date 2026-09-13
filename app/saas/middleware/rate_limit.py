from fastapi import HTTPException
LIMITS = {}
def check_rate_limit(tid: str, limit: int = 60):
    cnt = LIMITS.get(tid, 0)
    if cnt >= limit: raise HTTPException(429, "Rate limit exceeded")
    LIMITS[tid] = cnt + 1
