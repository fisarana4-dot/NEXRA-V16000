from app.saas.audit.service import AuditService
def test_audit(): s = AuditService(); l = s.log("LOGIN", "t1"); assert l.action == "LOGIN"
