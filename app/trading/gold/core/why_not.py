def explain(d):
 if d.get("blocked"):return "BLOCKED"
 if len(d.get("prices",[]))<3:return "DATA_INSUFFICIENT"
