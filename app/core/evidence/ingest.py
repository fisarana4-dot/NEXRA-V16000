from .contract import Evidence
def ingest(source,domain,data,timestamp,provenance=None):
 return Evidence(source,domain,data,timestamp,provenance)
