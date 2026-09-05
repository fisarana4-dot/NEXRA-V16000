def trail(d,e,p,s,a,x=1):
 q=p-e if d=="BUY" else e-p
 if q<a*x:return s
 n=p-a if d=="BUY" else p+a
 return max(s,n) if d=="BUY" else min(s,n)
