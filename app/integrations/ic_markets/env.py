import os
from pathlib import Path
for x in Path(".env.icmarkets").read_text().splitlines():
 k,_,v=x.partition("="); os.environ[k]=v
