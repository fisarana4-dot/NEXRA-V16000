import sys,subprocess,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def backup(p):
 b=Path(str(p)+".bak"); shutil.copy2(p,b) if Path(p).exists() else None
def restore(p,old):
 if old is None: Path(p).unlink(missing_ok=True)
 else: Path(p).write_text(old,encoding="utf-8")
def compile_file(p):
 return subprocess.run(["python","-m","py_compile",str(p)],cwd=ROOT).returncode==0
def tests():
 return subprocess.run(["pytest","-q","tests"],cwd=ROOT).returncode==0
def apply(p,text):
 old=Path(p).read_text() if Path(p).exists() else None
 backup(p); Path(p).write_text(text,encoding="utf-8")
 if not compile_file(p): restore(p,old); return False
 if not tests(): restore(p,old); return False
 return True
def main():
 a=sys.argv[1:]
 print("FORGE_ARGS",a)
 if len(a)<3 or a[0]!="apply": return False
 p=a[1]; text=" ".join(a[2:])
 return apply(p,text)
if __name__=="__main__": print(main())
