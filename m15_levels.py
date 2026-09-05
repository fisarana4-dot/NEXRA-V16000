import csv
m=list(csv.DictReader(open("m1_240.csv")));v=list(csv.DictReader(open("data/gold/full/xauusd-m15-bid-2026-01-01-2026-08-08.csv")))
t=int(m[-1]["timestamp"]);x=[z for z in v if int(z["timestamp"])<=t][-1]
print("M15_CONTEXT",x)
i=v.index(x);vs=[float(z["volume"]) for z in v[max(0,i-20):i]]
avg=sum(vs)/len(vs);rvol=float(x["volume"])/avg if avg else 0
print("M15_VOL",x["volume"],"BASE",round(avg,4),"RVOL",round(rvol,2))
sp=float(x["high"])-float(x["low"]);o=float(x["open"]);c=float(x["close"]);h=float(x["high"]);l=float(x["low"])
clv=((c-l)-(h-c))/sp if sp else 0
print("M15_SPREAD",round(sp,3),"CLV",round(clv,2),"RVOL",round(rvol,2))
vscore=2 if rvol>=1.5 and clv>=0.5 else 1 if clv>0 else -1
print("VSA_SCORE",vscore,"TOTAL_SCORE",3+vscore)
cl=[float(z["close"]) for z in v];e9=sum(cl[-9:])/9;e21=sum(cl[-21:])/21
trend="BULL" if c>e9 and e9>e21 else "BEAR" if c<e9 and e9<e21 else "MIXED"
tscore=2 if trend=="BULL" else -2 if trend=="BEAR" else 0
print("M15_TREND",trend,"TREND_SCORE",tscore,"TOTAL",5+tscore)
d=[cl[i]-cl[i-1] for i in range(1,len(cl))];g=[max(x,0) for x in d];z=[max(-x,0) for x in d]
ag=sum(g[-14:])/14;az=sum(z[-14:])/14;rsi=100 if az==0 else 100-100/(1+ag/az)
print("M15_RSI",round(rsi,2))
rs=[]
for k in range(14,len(cl)):a=cl[k-14:k+1];rs.append(100-100/(1+sum(max(a[j]-a[j-1],0) for j in range(1,len(a)))/max(sum(max(a[j-1]-a[j],0) for j in range(1,len(a))),1e-9)))
print("RSI_SERIES",len(rs),"LAST",round(rs[-1],2))
f="data/gold/full/xauusd-m15-bid-2026-01-01-2026-08-08.csv";v=list(csv.DictReader(open(f)))
c=[float(x["close"]) for x in v];h=[float(x["high"]) for x in v];l=[float(x["low"]) for x in v]
lv=sorted(h[-50:]+l[-50:]);p=c[-1];k=min(lv,key=lambda x:abs(x-p))
print("M15_KEY_LEVEL",round(k,3),"PRICE",round(p,3))
scores=[(2 if x in h[-20:] else 0)+(2 if x in l[-20:] else 0) for x in lv]
best=max(zip(lv,scores),key=lambda z:z[1]);print("LEVEL_SCORE",best)
