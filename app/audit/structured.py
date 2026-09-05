def make_record(n,ok,r="R0",s="INFO",e=""):
 return {"name":n,"status":"PASS" if ok else "FAIL","rule":r,"severity":s,"evidence":e,"blocked":not ok}
