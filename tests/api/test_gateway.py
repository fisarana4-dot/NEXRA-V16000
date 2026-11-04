from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_status(): r = client.get("/api/v1/status"); assert r.status_code == 200
def test_caps(): r = client.get("/api/v1/capabilities"); assert r.status_code == 200
def test_task(): r = client.post("/api/v1/task", json={"type": "test"}); assert r.status_code == 200
def test_dec(): r = client.post("/api/v1/decision", json={"context": {}}); assert r.status_code == 200
def test_tenant_hdr(): r = client.get("/api/v1/status", headers={"X-Tenant-ID": "t1"}); assert r.headers["X-Tenant-ID"] == "t1"
from app.saas.middleware.rate_limit import check_rate_limit, LIMITS
def test_rate_limit(): LIMITS["t_test"] = 60; import pytest; pytest.raises(Exception, check_rate_limit, "t_test")
