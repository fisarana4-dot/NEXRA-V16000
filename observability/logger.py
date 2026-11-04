import json
class EMFLogger:
    @staticmethod
    def log(n, v):
        return json.dumps({"_aws": {"Timestamp": 1}, n: v})
