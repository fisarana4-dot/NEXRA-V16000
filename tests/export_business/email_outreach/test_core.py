from app.export_business.email_outreach.models import EmailMessage
from app.export_business.email_outreach.transports import MockEmailTransport
def test_email_send():
    t=MockEmailTransport()
    m=EmailMessage(to="a@b.com",subject="Hi",body="Test")
    r=t.send(m)
    assert r["status"]=="sent"
    assert t.sent[0].to=="a@b.com"
from app.export_business.email_outreach.service import EmailService
def test_email_service():
    t=MockEmailTransport(); s=EmailService(t)
    m=EmailMessage(to="b@c.com",subject="Hi",body="Test")
    r=s.send(m)
    assert r["status"]=="sent"
