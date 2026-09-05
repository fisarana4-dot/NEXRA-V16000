import json
from pathlib import Path
def save_case(case):
 p=Path("data/training/gold/market_training.jsonl")
 with p.open("a") as f:
  f.write(json.dumps(case)+"\n")
