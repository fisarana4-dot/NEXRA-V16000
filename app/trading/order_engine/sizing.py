def size(balance,risk_pct,entry,sl):
 risk=balance*risk_pct/100;dist=abs(entry-sl)
 if risk<=0 or dist<=0:return 0.0
 return risk/dist
