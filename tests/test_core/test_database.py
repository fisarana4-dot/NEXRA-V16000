import pytest
from sqlalchemy import create_engine
from app.models.user import User
from app.models.lead import Lead

def test_user(db):
    u = User(email="a@n.com", hashed_password="test-hash", is_active=True)
    db.add(u)
    db.commit()
    assert db.query(User).filter_by(email="a@n.com").first() is not None

def test_lead(db):
    lead = Lead(tenant_id="test", company_name="Duniya Traders")
    db.add(lead)
    db.commit()
    assert db.query(Lead).filter_by(company_name="Duniya Traders").first() is not None
