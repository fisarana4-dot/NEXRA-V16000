import csv
f="data/gold/full/xauusd-m15-bid-2026-01-01-2026-08-08.csv"
r=list(csv.DictReader(open(f)))
print("M15_ROWS",len(r))
for i in range(500,len(r),700):print(i,r[i]["close"])
