from pathlib import Path
def validate(target,text):
 q=(ROOT/target).resolve(); ok=False
ROOT=Path(__file__).resolve().parents[2]
def validate(target,text):
 if not target or not text or Path(target).suffix!=".py": return False
 try: (ROOT/target).resolve().relative_to(ROOT)
 except ValueError: return False
 return True
