import csv
r=list(csv.DictReader(open("m1_240.csv")))
for i in range(1,len(r)): print(i,"HH" if float(r[i]["high"])>float(r[i-1]["high"]) else "LH","HL" if float(r[i]["low"])>float(r[i-1]["low"]) else "LL")
