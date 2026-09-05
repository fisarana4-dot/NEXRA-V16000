
import requests,time
from app.core.evidence.ingest import ingest
from app.core.evidence.store import save

def collect():
 d=requests.get("https://xaus.com/api/v1/intraday?symbol=xau&hours=6", timeout=10).json()
 e=ingest("XAUS","GOLD",{"points":d["points"]},str(int(time.time())))
 return e


from app.core.evidence.hash import fingerprint
def save_live(): e=collect();save(e,fingerprint(e));return len(e.data["points"])
