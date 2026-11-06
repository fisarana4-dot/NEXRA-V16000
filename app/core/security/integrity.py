import hashlib

import json
def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
def chain_hash(payload, previous_hash=""):
    raw=json.dumps(payload,sort_keys=True,separators=(",",":"),allow_nan=False)
    return sha256((previous_hash+raw).encode())
def verify_chain(records):
    prev=""
    for r in records:
        if not isinstance(r,dict) or "payload" not in r or "hash" not in r: return False
        try:
            expected=chain_hash(r["payload"],prev)
        except (TypeError,ValueError): return False
        if r["hash"]!=expected: return False
        prev=r["hash"]
    return True
