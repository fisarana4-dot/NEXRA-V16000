import pandas as p
d=p.read_csv('data/bafl_6m_ohlcv.csv',skiprows=[1,2])
h=p.to_numeric(d.High);l=p.to_numeric(d.Low)
c=p.to_numeric(d.Close);o=p.to_numeric(d.Open)
v=p.to_numeric(d.Volume)
s=h-l
av=v.rolling(20).mean()
r9=v>av*1.5
print("R9",int(r9.sum()))
