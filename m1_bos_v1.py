import csv
r=list(csv.DictReader(open("m1_240.csv")));H=[];L=[]
for i in range(1,len(r)-1):
 h=float(r[i]["high"]);l=float(r[i]["low"]);ph=float(r[i-1]["high"]);nh=float(r[i+1]["high"]);pl=float(r[i-1]["low"]);nl=float(r[i+1]["low"])
 if h>ph and h>nh:H.append((i,h))
 if l<pl and l<nl:L.append((i,l))
lastH=lastL=0;bos=[]
for i,x in enumerate(r):
 c=float(x["close"]);bh=max((v for j,v in H if j<i),default=0);bl=min((v for j,v in L if j<i),default=0)
 if bh and c>bh and bh!=lastH:bos.append((i,"BULL_BOS",c,bh));lastH=bh
 if bl and c<bl and bl!=lastL:bos.append((i,"BEAR_BOS",c,bl));lastL=bl
print("BOS_COUNT",len(bos));print(*bos,sep="\n")
print("BOS_V1_READY")
