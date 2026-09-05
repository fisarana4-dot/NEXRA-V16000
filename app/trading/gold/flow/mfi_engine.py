class MFIEngine:
 def value(self,h,l,c,v,p=14):
  if len(c)<p+1:return 50.0
  t=[(h[i]+l[i]+c[i])/3 for i in range(len(c))]
  a=b=0.0
  for i in range(len(c)-p,len(c)):
   f=t[i]*v[i]
   a+=f if t[i]>t[i-1] else 0;b+=f if t[i]<t[i-1] else 0
  if b==0:return 100.0 if a else 50.0
  return 100-100/(1+a/b)
mfi_engine=MFIEngine()
