import csv
r=list(csv.DictReader(open("m1_240.csv")));H=[];L=[]
for i in range(1,len(r)-1):
 h=float(r[i]["high"]);l=float(r[i]["low"]);ph=float(r[i-1]["high"]);nh=float(r[i+1]["high"]);pl=float(r[i-1]["low"]);nl=float(r[i+1]["low"]);
 if h>ph and h>nh:H.append((i,h))
 if l<pl and l<nl:L.append((i,l))
print("SWING_HIGHS",len(H));print("SWING_LOWS",len(L));print("H",H[:10]);print("L",L[:10])
print("HIGH_STRUCTURE")
for i,(idx,v) in enumerate(H):print(idx,"HH" if i==0 or v>H[i-1][1] else "LH")
print("LOW_STRUCTURE")
for i,(idx,v) in enumerate(L):print(idx,"HL" if i==0 or v>L[i-1][1] else "LL")
