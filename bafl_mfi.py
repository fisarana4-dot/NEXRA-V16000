import pandas as p
d=p.read_csv('data/bafl_6m_ohlcv.csv',skiprows=[1,2])
h=p.to_numeric(d.High);l=p.to_numeric(d.Low)
c=p.to_numeric(d.Close);v=p.to_numeric(d.Volume)
t=(h+l+c)/3
f=t*v
r=f.where(t.diff()>0,0).rolling(14).sum()
q=f.where(t.diff()<0,0).rolling(14).sum()
m=100-100/(1+r/q)
print(round(m.iloc[-1],2))
