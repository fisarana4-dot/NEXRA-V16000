import sys
from pathlib import Path
from tools.nexra_forge.forge import apply
def build(spec):
 s=Path(spec).read_text(encoding="utf-8").splitlines()
 p=s[0]; text="\n".join(s[1:])+"\n"
 return apply(p,text)
if __name__=="__main__": print(build(sys.argv[1]))
