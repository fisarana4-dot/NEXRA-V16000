from pathlib import Path
ALLOWED={"create","update"}
ROOT=Path(__file__).resolve().parents[2]
def validate(s):
 if not isinstance(s,dict) or s.get("operation") not in ALLOWED:return False
t=s.get("target","");c=s.get("content","");r=s.get("reason")
t=s.get("target","");c=s.get("content","");r=s.get("reason")
if not t.endswith(".py") or not c or not r:return False
except ValueError:return False
