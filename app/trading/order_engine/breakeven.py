def protect(d,e,p,s,r):
 if p-e>=r:return max(s,e)
 if e-p>=r:return min(s,e)
 return s
