from fastapi.testclient import TestClient
from app.api_lead_saas import app
client = TestClient(app)
def test_health(): assert client.get("/health").json()["status"] == "healthy"
