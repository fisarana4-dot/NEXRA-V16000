class AIStrategyScout:
 def analyze(self, prices):
  if len(prices)<3: return {"decision":"WAIT"}
  a,b,c=prices[-3:]
  if c>b>a: return {"decision":"LONG"}
  if c<b<a: return {"decision":"SHORT"}
  return {"decision":"WAIT"}
