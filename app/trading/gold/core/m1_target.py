def target(d):
 r=abs(d["entry"]-d["sl"]);m=d.get("rr",2)
 return d["entry"]+r*m if d["direction"]=="BUY" else d["entry"]-r*m
