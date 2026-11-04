from fastapi import FastAPI
from datetime import datetime,timezone
from app.bridge.operations import APPROVED
app=FastAPI()
@app.get("/health")
def health():return {"status":"ok","ops":sorted(APPROVED)}
from fastapi import HTTPException
@app.get("/ops/{op}")
def op(op):
 if op not in APPROVED:raise HTTPException(403)
 return {"op":op,"approved":1,"bridge":"online","system":{"uvicorn":"running","approved_ops":sorted(APPROVED),"timestamp":datetime.now(timezone.utc).isoformat()}}
