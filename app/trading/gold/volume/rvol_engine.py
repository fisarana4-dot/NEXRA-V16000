class RVOL20:
 def analyze(self,v):
  if len(v)<21: return {"status":"INSUFFICIENT_DATA"}
  avg=sum(v[-21:-1])/20
  r=v[-1]/avg if avg>0 else None
  if r is None: return {"rvol":None,"status":"ZERO_AVERAGE"}
  if r>1: return {"rvol":round(r,3),"status":"ABOVE_AVERAGE"}
  if r<1: return {"rvol":round(r,3),"status":"BELOW_AVERAGE"}
  return {"rvol":1.0,"status":"AT_AVERAGE"}
rvol_engine=RVOL20()
