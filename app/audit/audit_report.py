import time
def report(x): return {"decision":"BLOCK" if x.get("blocked") else "PASS","timestamp":time.time(),"status":x.get("status","UNKNOWN"),"blocked":x.get("blocked",False),"findings":x.get("findings",[]),"severity":x.get("severity","INFO"),"rule_id":x.get("rule_id","R0"),"evidence":x.get("evidence","")}
