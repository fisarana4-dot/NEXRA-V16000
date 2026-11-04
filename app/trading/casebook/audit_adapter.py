from app.audit.audit_record import AuditRecord
def to_audit(c):
 a=AuditRecord("CASEBOOK","PASS")
 a.engine_id=c.engine_id
 a.decision=c.decision
 a.score=c.score
 a.entry=c.entry
 a.sl=c.sl
 a.tp=c.tp
 return a
from app.audit.audit_report import report
def audit_report(c):
 a=to_audit(c)
 return report({"status":"PASS","blocked":0,"evidence":str(a.__dict__)})
