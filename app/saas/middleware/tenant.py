from starlette.middleware.base import BaseHTTPMiddleware
class SaaSContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, req, call_next):
        req.state.tenant_id = req.headers.get("X-Tenant-ID", "default")
        res = await call_next(req)
        res.headers["X-Tenant-ID"] = req.state.tenant_id
        return res
