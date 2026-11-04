def score(e):
 return min(100,max(0,sum(e)))
def direction(e):
 b=sum(e.get("BUY",[]));s=sum(e.get("SELL",[]))
 return "BUY" if b>s else "SELL" if s>b else "WAIT"
