import csv
r=list(csv.DictReader(open("m1_240.csv")));SH=[];SL=[]
for i in range(1,len(r)-1):
 h,l=float(r[i]["high"]),float(r[i]["low"]);ph,nh=float(r[i-1]["high"]),float(r[i+1]["high"]);pl,nl=float(r[i-1]["low"]),float(r[i+1]["low"])
 if h>ph and h>nh:SH.append((i,h))
 if l<pl and l<nl:SL.append((i,l))
SHS=[(j,v,"H" if i==0 else "HH" if v>SH[i-1][1] else "LH") for i,(j,v) in enumerate(SH)]
SLS=[(j,v,"L" if i==0 else "HL" if v>SL[i-1][1] else "LL") for i,(j,v) in enumerate(SL)]
E=sorted(SHS+SLS);print("STRUCTURE_EVENTS",len(E));print(*E,sep="\n")
state="NONE";states=[]
for i,v,t in E:states.append((i,t));state="BULL" if t=="HH" else state
HH=sum(t=="HH" for _,_,t in E);LH=sum(t=="LH" for _,_,t in E)
HL=sum(t=="HL" for _,_,t in E);LL=sum(t=="LL" for _,_,t in E)
print("HH",HH,"LH",LH,"HL",HL,"LL",LL)
bull=HH+HL;bear=LH+LL
bias="BULL" if bull>bear+3 else "BEAR" if bear>bull+3 else "RANGE"
print("STRUCTURE_BIAS",bias,"BULL_SCORE",bull,"BEAR_SCORE",bear)
score=0;score+=2 if bias=="BULL" else -2 if bias=="BEAR" else 0
print("STRUCT_SCORE",score)
last=r[-1];o,h,l,c=map(float,[last["open"],last["high"],last["low"],last["close"]])
rg=h-l;body=abs(c-o);bull_c=c>o;bear_c=c<o
cscore=1 if bull_c else -1 if bear_c else 0
print("CANDLE_SCORE",cscore,"TOTAL_PRE_VSA",score+cscore)
