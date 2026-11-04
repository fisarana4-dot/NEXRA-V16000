from fastapi import FastAPI
app = FastAPI(title="NEXRA MCP Server")
@app.get("/tools")
def get_tools(): return {"tools": ["verify_lead_email", "score_b2b_lead"]}
