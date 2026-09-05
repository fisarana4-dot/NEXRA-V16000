class AuditEngine:
 def __init__(self): self.history=[]
 def check(self,n,ok): x={"name":n,"status":"PASS" if ok else "FAIL"}; self.history.append(x); return x
 def record(self,n,ok): return self.check(n,ok)
 def get_history(self): return self.history
