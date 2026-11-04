def verify(a,b): return a == b
def status(results):
    return "VERIFIED" if len(set(results)) == 1 else "UNVERIFIED"
def accept(results):
    return status(results) == "VERIFIED"
def source_ok(src):
    return isinstance(src,str) and bool(src.strip())
import time
def fresh(ts,max_age=86400):
    try: return time.time()-float(ts) <= max_age
    except: return False
