import csv
r=list(csv.DictReader(open("m1_240.csv")))
for i in range(1,len(r)-1):
 h=float(r[i]["high"]);ph=float(r[i-1]["high"]);nh=float(r[i+1]["high"])
 l=float(r[i]["low"]);pl=float(r[i-1]["low"]);nl=float(r[i+1]["low"])
 if h>ph and h>nh: print(i,"SWING_HIGH")
 if l<pl and l<nl: print(i,"SWING_LOW")
print("SWING_ENGINE_READY",len(r))
