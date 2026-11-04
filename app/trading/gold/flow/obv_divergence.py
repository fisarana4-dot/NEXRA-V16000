class OBVEngine:
 def value(self,c,v):
  if len(c)!=len(v): raise ValueError("length")
  o=[0.0]
  for i in range(1,len(c)):
   o.append(o[-1]+(v[i] if c[i]>c[i-1] else -v[i] if c[i]<c[i-1] else 0))
  return o
obv_engine=OBVEngine()
