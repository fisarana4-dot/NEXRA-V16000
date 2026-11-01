from pathlib import Path
def test_sample_file_exists():
    assert Path("portfolio_demo/data/sample_leads.csv").is_file()
import csv
def test_row_count():
 r=list(csv.DictReader(open('portfolio_demo/data/sample_leads.csv')))
 assert len(r)==4
def test_duplicate_count():
 r=list(csv.DictReader(open("portfolio_demo/data/sample_leads.csv")))
 assert len(r)-len({tuple(x.values()) for x in r})==1
def test_missing_email():
 r=list(csv.DictReader(open("portfolio_demo/data/sample_leads.csv")))
 assert sum(not x['email'] for x in r)==1
