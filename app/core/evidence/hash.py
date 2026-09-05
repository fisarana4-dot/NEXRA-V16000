import hashlib,json
def fingerprint(e):
 return hashlib.sha256(json.dumps(e.data,sort_keys=True).encode()).hexdigest()
