import json,subprocess,datetime,sys
from .ingest import ingest
from .hash import fingerprint
from . import store
class DecisionEvidenceLedger:
 def __init__(self,path="MASTER_STATUS.json"):
  self.path=path
 def run_tests(self):
  cmd=[sys.executable,"-m","pytest","--import-mode=importlib","tests/","-q"]
  return subprocess.run(cmd,text=True,capture_output=True)
 def compile(self):
  r=self.run_tests()
  ok=r.returncode==0
  import re;m=re.search(r"(\d+) passed",r.stdout)
  passed=int(m.group(1)) if m else 0
  sha=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
  ts=datetime.datetime.now(datetime.timezone.utc).isoformat()
  data={"system":"NEXRA-V16000","timestamp":ts,"tests":passed,"status":"PASS" if ok else "FAIL","exit":r.returncode,"git":sha}
  e=ingest("NEXRA","TEST_SUITE",data,ts,{"git":sha})
  h=fingerprint(e)
  payload={"system":"NEXRA-V16000","timestamp":ts,"tests":passed,"status":data["status"],"git":sha,"hash":h}
  with open(self.path,"w") as f: json.dump(payload,f,sort_keys=True,indent=2)
  store.init()
  store.save(e,h)
  return payload
