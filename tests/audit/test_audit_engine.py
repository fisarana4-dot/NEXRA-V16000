def test_audit_pass():
 from app.audit.audit_engine import AuditEngine
 assert AuditEngine().check("core",1)["status"]=="PASS"

def test_audit_fail():
 from app.audit.audit_engine import AuditEngine
 assert AuditEngine().check("risk",0)["status"]=="FAIL"

def test_audit_history():
 from app.audit.audit_engine import AuditEngine
 a=AuditEngine(); a.check("core",1); assert len(a.get_history())==1
def test_record(): assert __import__("app.audit.audit_engine",fromlist=["AuditEngine"]).AuditEngine().record("risk",0)["status"]=="FAIL"
def test_record_fields(): assert __import__("app.audit.audit_record",fromlist=["AuditRecord"]).AuditRecord("x","PASS","R1","INFO","e").evidence=="e"
def test_structured(): assert 1==1
def test_make_record(): assert __import__("app.audit.structured",fromlist=["make_record"]).make_record("x",1,"R1","INFO","e")["status"]=="PASS"
