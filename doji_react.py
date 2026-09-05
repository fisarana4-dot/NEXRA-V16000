import csv
r=list(csv.DictReader(open("m1_240.csv")))
for i in range(len(r)-5):
 o,h,l,c=map(float,[r[i]["open"],r[i]["high"],r[i]["low"],r[i]["close"]]);q=r[i+1:i+6];b=abs(c-o);rg=h-l
 if rg>0 and b/rg<=.15:
  hi=max(float(y["high"]) for y in q);lo=min(float(y["low"]) for y in q);print(i,round(hi-c,3),round(c-lo,3))
U=[];D=[]
for i in range(len(r)-5):
 o,h,l,c=map(float,[r[i]["open"],r[i]["high"],r[i]["low"],r[i]["close"]]);q=r[i+1:i+6];rg=h-l;b=abs(c-o)
 if rg>0 and b/rg<=.15:U.append(max(0,max(float(y["high"]) for y in q)-c));D.append(max(0,c-min(float(y["low"]) for y in q)))
