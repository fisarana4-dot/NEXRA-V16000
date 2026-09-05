import csv
r=list(csv.DictReader(open("m1_240.csv")));H=[];L=[]
for i in range(1,len(r)-1):
 h=float(r[i]["high"]);l=float(r[i]["low"]);ph=float(r[i-1]["high"]);nh=float(r[i+1]["high"]);pl=float(r[i-1]["low"]);nl=float(r[i+1]["low"])
 if h>ph and h>nh:H.append((i,h))
 if l<pl and l<nl:L.append((i,l))
state="NONE";mss=[]
for i,x in enumerate(r):
 c=float(x["close"]);bh=max((v for j,v in H if j<i),default=0);bl=min((v for j,v in L if j<i),default=0)
 if state!="BEAR" and bl and c<bl:mss.append((i,"BEAR_MSS",c,bl));state="BEAR"
 if state!="BULL" and bh and c>bh:mss.append((i,"BULL_MSS",c,bh));state="BULL"
print("MSS_COUNT",len(mss));print(*mss,sep="\n")
print("MSS_RAW_SAVED")
