import re
import dns.resolver
import csv
from datetime import datetime, timezone
class NexraLeadEngine:
    def __init__(self):
        self.disposable_domains = {'mailinator.com', 'tempmail.com'}
    def validate_syntax(self, email):
        return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))
    def process_lead(self, email):
        if not self.validate_syntax(email):
            return {"status": "REJECTED", "reason": "Invalid Syntax"}
        domain = email.rsplit("@", 1)[1].lower()
        if domain in self.disposable_domains:
            return {"status": "REJECTED", "reason": "Disposable Domain"}
        try:
            mx = dns.resolver.resolve(domain, "MX")
            return {"status":"DOMAIN_MX_VALID","mx":str(mx[0].exchange)}
        except Exception:
            return {"status": "RISKY"}
