def map_levels(highs,lows):
 return {"high":max(highs),"low":min(lows)} if highs and lows else {}
def sweep(price,high,low):
 if price>high:return "HIGH_SWEEP"
 if price<low:return "LOW_SWEEP"
 return "NONE"
