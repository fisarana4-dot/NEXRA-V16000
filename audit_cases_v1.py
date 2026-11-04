cases=[("BULL",2,1,2,2,51,"BUY"),("WEAK",2,1,0,2,51,"NO_TRADE"),("BEAR",-2,-1,-2,-2,45,"SELL"),("TRAP",2,1,-1,2,52,"NO_TRADE"),("BOS",2,1,2,2,58,"BUY")]
for n,s,v,t,r,rs,e in cases:print(n,"SCORE",s+v+t+r,"RSI",rs,"EXPECTED",e)
for n,s,v,t,r,rs,e in cases:d="BUY" if s+v+t+r>=6 else "SELL" if s+v+t+r<=-6 else "NO_TRADE";print(n,d,e,d==e)
