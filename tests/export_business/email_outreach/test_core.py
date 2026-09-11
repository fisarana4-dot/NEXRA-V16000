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
from unittest.mock import MagicMock,patch
from app.export_business.email_outreach.smtp import SMTPEmailTransport
def test_smtp_mock():
 m=MagicMock();m.__enter__.return_value=m
 msg=EmailMessage("to@x.com","Hi","Body",reply_to="r@x.com")
 with patch("app.export_business.email_outreach.smtp.smtplib.SMTP") as p:
  p.return_value.__enter__.return_value=m
  r=SMTPEmailTransport("h",587,"u","p","f@x.com").send(msg)
  assert r["status"]=="sent"
  assert m.send_message.called
  assert m.send_message.call_args[0][0]["Reply-To"]=="r@x.com"
def test_smtp_env(monkeypatch):
 monkeypatch.setenv("SMTP_HOST","envhost")
 t=SMTPEmailTransport();assert t.host=="envhost"
def test_smtp_not_configured():
 assert SMTPEmailTransport().send(None)["status"]=="NOT_CONFIGURED"
def test_smtp_auth():
 m=MagicMock();m.__enter__.return_value=m
 with patch("app.export_business.email_outreach.smtp.smtplib.SMTP") as p:
  p.return_value.__enter__.return_value=m
  SMTPEmailTransport("h",587,"u","p","f@x.com").send(EmailMessage("a","b","c"))
  assert m.login.called and m.starttls.called
