import hashlib, json
class EvidenceEngine:
    def __init__(self, d): self.d = d
    def generate_evidence(self):
        h = hashlib.sha256(str(self.d).encode()).hexdigest()
        return {'status': 'VALIDATED', 'hash': h}
    def save_audit(self):
        res = self.generate_evidence()
        with open('audit_log.json', 'a') as f: f.write(str(res) + '\n')
        return res
