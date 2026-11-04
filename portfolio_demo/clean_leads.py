import csv
import sys
from pathlib import Path
def main():
    p = Path(__file__).parent / "data" / "sample_leads.csv"
    rows = list(csv.DictReader(p.open()))
    print('Rows:',len(rows))
    print('Missing email:',sum(not r['email'] for r in rows))
    print('Duplicates:',len(rows)-len({tuple(r.values()) for r in rows}))
if __name__ == "__main__":
    main()
