import pandas as p
d=p.read_csv('data/silver5y.csv')
from ta.volume import OnBalanceVolumeIndicator as O
print(O(d.Close,d.Volume).on_balance_volume().tail(3))
