import sys
from pathlib import Path
from tools.nexra_forge.spec_builder import validate
from tools.nexra_forge.forge import apply
def run(spec):
 s=Path(spec).read_text(encoding="utf-8").splitlines()
 target=s[0]; text="\n".join(s[1:])+"\n"
 if not validate(target,text): return False
 return apply(target,text)
if __name__=="__main__": print("NEXRA_FORGE: use tools/nexra SPEC_FILE") if len(sys.argv)<2 else print(run(sys.argv[1]))
