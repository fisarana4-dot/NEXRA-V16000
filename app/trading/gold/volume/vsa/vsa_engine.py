class VSAEngine:
 def analyze(self,d):
  if len(d)<21:return []
  k=("open","high","low","close","volume")
  if any(x not in d[-1] for x in k):raise ValueError("OHLCV")
