
import pandas as p
d=p.read_csv('data/bafl_6m_ohlcv.csv',skiprows=[1,2])
c=p.to_numeric(d.Close)
v=p.to_numeric(d.Volume)
s=c.diff().fillna(0).ge(0)
o=(v*s).cumsum()
print(o.iloc[[103,123,126]].to_list())
