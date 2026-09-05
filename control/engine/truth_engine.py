import ast,hashlib,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
IGNORE={".git","__pycache__",".pytest_cache","venv","control"}
def sha256(p):
 h=hashlib.sha256();f=open(p,"rb")
 for c in iter(lambda:f.read(65536),b""):h.update(c)
 f.close();return h.hexdigest()
def audit():
 files={}
 for p in ROOT.rglob("*.py"):
  if any(i in p.parts for i in IGNORE):continue
  rel=str(p.relative_to(ROOT));sz=p.stat().st_size
  st="EMPTY" if sz==0 else "LOGIC_PRESENT"
  files[rel]={"size":sz,"sha256":sha256(p),"status":st,"ast":ast_status(p)}
 r={"time":datetime.now(timezone.utc).isoformat(),"files":files}
 (ROOT/"control/ledger").mkdir(parents=True,exist_ok=True)
 (ROOT/"control/ledger/inventory.json").write_text(json.dumps(r,indent=2))
 print(f"FILES={len(files)}")

def ast_status(p):
 try: ast.parse(p.read_text());return "AST_VALID"
 except Exception as e:return "AST_ERROR"
print("AST scanner added")
if __name__=="__main__":audit()
