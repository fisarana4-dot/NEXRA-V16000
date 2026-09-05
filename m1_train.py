import csv
r=list(csv.DictReader(open("m1_240.csv")))
print("TRAIN_CANDLES",len(r))
def anatomy(x):
 o,h,l,c=map(float,[x["open"],x["high"],x["low"],x["close"]])
 r=h-l;b=abs(c-o);u=h-max(o,c);d=min(o,c)-l
 return {"range":r,"body":b,"upper":u,"lower":d}
def side(x):return "BULL" if x["close"]>x["open"] else "BEAR" if x["close"]<x["open"] else "DOJI"
A=[anatomy(x) for x in r]
print("BULL",sum(side(x)=="BULL" for x in r),"BEAR",sum(side(x)=="BEAR" for x in r),"DOJI",sum(side(x)=="DOJI" for x in r))
def doji(x):return x["range"]>0 and x["body"]/x["range"]<=.15
print("DOJI_LIKE",sum(doji(x) for x in A))
