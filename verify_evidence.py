import json, hmac, hashlib, os
k = os.environ["NEXRA_HASH_PEPPER"].encode()
d = json.load(open("verified_leads.json"))
for i in d:
    h = hmac.new(k, i["email"].encode(), hashlib.sha256)
    assert i["hash"] == h.hexdigest(), i["email"]
print("EVIDENCE VERIFIED", len(d), "leads")
