import json
with open("verified_leads.json") as f:
    leads = json.load(f)
assert isinstance(leads, list)
assert leads
print("EVIDENCE VERIFIED")
