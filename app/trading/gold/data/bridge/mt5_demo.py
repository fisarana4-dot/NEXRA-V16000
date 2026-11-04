from app.core.evidence.adapters.base import SourceAdapter
class MT5DemoBridge(SourceAdapter):
    def status(self): return "READY"
    def load_csv(self,p):
        import csv
        return list(csv.DictReader(open(p)))
