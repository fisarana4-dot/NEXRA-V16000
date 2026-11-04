def sl_ready(d):
 p=d.get("price");s=d.get("sl");x=d.get("direction")
 if not p or not s or p==s:return False
 return s<p if x=="BUY" else s>p if x=="SELL" else False
