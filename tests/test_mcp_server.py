from fastapi.testclient import TestClient
from app.mcp_server import app
def test_mcp_tools(): assert "verify_lead_email" in TestClient(app).get("/tools").json()["tools"]
