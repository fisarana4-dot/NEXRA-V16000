from app.audit.audit_engine import AuditEngine
from app.monitoring.diagnostic import Diagnostic
a=AuditEngine();r=a.check('order',1);print(r)
d=Diagnostic('E2','T2','order_engine',r['status'],'audit_pass');print(d)
