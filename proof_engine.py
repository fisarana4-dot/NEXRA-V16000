import hashlib
import json
import time

class ProofEngine:
    @staticmethod
    def generate_proof(data: dict) -> dict:
        t = time.time()
        p = {"data": data, "timestamp": t}
        enc = json.dumps(p, sort_keys=True).encode()
