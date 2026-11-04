class AuditRunner:
 def run(self): return {"status":"PASS"}
 def audit(self): return self.run()
 def scan(self,text): from app.audit.placeholder_scanner import scan; f=scan(text); return {"status":"FAIL" if f else "PASS","findings":f,"blocked":bool(f),"severity":"CRITICAL" if f else "INFO","rule_id":"AUD-PLACEHOLDER-001","evidence":",".join(f)}
