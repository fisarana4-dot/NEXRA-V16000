from app.core.mcp import MCPTool, MCPExecutor, MCPPermissionPolicy
from app.core.mcp.adapter import to_tool_contract
from app.export_business.email_outreach.models import EmailMessage
from app.export_business.email_outreach.transports import MockEmailTransport
def test_mcp_email_tool():
    t=MockEmailTransport()
    m=EmailMessage(to="client@example.com",subject="Test",body="Hello")
    tool=MCPTool(name="send_email",description="Send email")
    c=to_tool_contract(tool)
    assert c.name=="send_email"
    assert c.description=="Send email"
    assert c.parameters.type=="object"
    assert m.to=="client@example.com"
    assert m.subject=="Test"
    assert m.body=="Hello"
    r=t.send(m)
    assert r["status"]=="sent"
    assert t.sent[0].to=="client@example.com"
    p=MCPPermissionPolicy(["send_email"])
    e=MCPExecutor(p)
    assert e.check("send_email") is True
    assert e.check("delete_email") is False
    r=e.execute("send_email",to=m.to,subject=m.subject)
    assert r["status"]=="READY"
    assert r["tool"]=="send_email"
    assert r["args"]["to"]=="client@example.com"
    assert r["args"]["subject"]=="Test"
    r=e.execute("send_email",to=m.to,subject=m.subject,body=m.body)
    assert r["args"]["body"]=="Hello"
