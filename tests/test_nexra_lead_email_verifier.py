from app.integrations.lead_email_verifier import NexraLeadEngine
import pytest
def test_engine_initialization():
    assert "mailinator.com" in NexraLeadEngine().disposable_domains
def test_valid_email_syntax():
    assert NexraLeadEngine().validate_syntax("info@example.com")
def test_invalid_email_syntax():
    assert not NexraLeadEngine().validate_syntax("bad-email")
def test_disposable_email_rejected():
    assert NexraLeadEngine().process_lead("x@mailinator.com")["status"] == "REJECTED"
def test_invalid_lead_rejected():
    assert NexraLeadEngine().process_lead("bad")["status"] == "REJECTED"
def test_mx_lookup(monkeypatch):
    monkeypatch.setattr("dns.resolver.resolve", lambda *a: [type("M", (), {"exchange": "mx.test."})()])
    assert NexraLeadEngine().process_lead("a@example.com")["status"] == "DOMAIN_MX_VALID"
