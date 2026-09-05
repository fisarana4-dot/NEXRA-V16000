
import pandas as p
d=p.read_csv('data/bafl_6m_ohlcv.csv',skiprows=[1,2])
c=p.to_numeric(d.Close)
r=c.diff()
u=r.clip(lower=0)
x=-r.clip(upper=0)
a=u.ewm(alpha=1/14,adjust=False).mean()
b=x.ewm(alpha=1/14,adjust=False).mean()
d.Volume=p.to_numeric(d.Volume)
d["OBV"]=d.Volume.mul(d.Close.diff().fillna(0).ge(0).map({1:1,0:-1})).cumsum()
d["RSI"]=100-100/(1+a/b)
print("RSI14",round(100-100/(1+a.iloc[-1]/b.iloc[-1]),2))
