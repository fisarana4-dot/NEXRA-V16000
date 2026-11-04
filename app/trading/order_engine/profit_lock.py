def lock(d,e,p,s,r,x=.5):
 q=p-e if d=="BUY" else e-p
 if q<r:return s
 n=e+(q*x) if d=="BUY" else e-(q*x)
 return max(s,n) if d=="BUY" else min(s,n)
