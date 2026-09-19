import hashlib

import json
def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
def chain_hash(payload, previous_hash=""):
    raw=json.dumps(payload,sort_keys=True,separators=(",",":"))
    return sha256((previous_hash+raw).encode())
def verify_chain(records):
    prev=""
    for r in records:
        expected=chain_hash(r["payload"],prev)
        if r["hash"]!=expected: return False
        prev=r["hash"]
    return True
