from fastapi import APIRouter
router = APIRouter(prefix="/api/v1")
@router.get("/status")
def status(): return {"status": "online"}
@router.get("/capabilities")
def capabilities(): return {"tools": ["mcp"]}
@router.post("/task")
def task(p: dict): return {"status": "queued"}
@router.post("/decision")
def decision(d: dict): return {"status": "ok"}
