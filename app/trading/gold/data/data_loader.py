import csv
TIME_FIELDS = {"Date", "time", "timestamp"}
class GoldDataLoader:
    def load(self,p):
        with open(p, newline="") as source:
            rows=[]
            for raw in csv.DictReader(source):
                row={key:(value if key in TIME_FIELDS else float(value)) for key,value in raw.items()}
                if "tick_volume" in row and "volume" not in row:
                    row["volume"]=row["tick_volume"]
                rows.append(row)
            return rows
data_loader=GoldDataLoader()
