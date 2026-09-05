import csv
r=list(csv.DictReader(open("m1_240.csv")));H=[];L=[]
for i in range(1,len(r)-1):
 h=float(r[i]["high"]);l=float(r[i]["low"]);ph=float(r[i-1]["high"]);nh=float(r[i+1]["high"]);pl=float(r[i-1]["low"]);nl=float(r[i+1]["low"])
 if h>ph and h>nh:H.append((i,h))
 if l<pl and l<nl:L.append((i,l))
state="NONE";events=[]
for i,x in enumerate(r):
 c=float(x["close"]);bh=max((v for j,v in H if j<i),default=0);bl=min((v for j,v in L if j<i),default=0)
 if state=="NONE" and bh and c>bh:state="BULL";events.append((i,"BOS_BULL"))
 if state=="NONE" and bl and c<bl:state="BEAR";events.append((i,"BOS_BEAR"))
 if state=="BULL" and bl and c<bl:events.append((i,"CHoCH_BEAR"));state="BEAR"
 if state=="BEAR" and bh and c>bh:events.append((i,"CHoCH_BULL"));state="BULL"
print("EVENTS",len(events));print(*events,sep="\n")
print("CHOCH_RAW_SAVED")
