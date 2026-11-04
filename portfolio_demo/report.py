import csv
from pathlib import Path
p=Path(__file__).parent
rows=list(csv.DictReader((p/"data"/"sample_leads.csv").open()))
out=p/"output"/"report.txt"
missing=sum(not r['email'] for r in rows)
dups=len(rows)-len({tuple(r.values()) for r in rows})
out.write_text(f"Rows: {len(rows)}")
out.write_text(out.read_text()+"\nMissing email: "+str(missing))
out.write_text(out.read_text()+"\nDuplicates: "+str(dups))
