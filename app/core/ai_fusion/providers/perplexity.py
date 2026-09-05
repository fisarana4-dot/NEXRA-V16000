from .base.base_provider import BaseProvider
class PerplexityProvider(BaseProvider):
    name="perplexity"
    def status(self): return {"provider":self.name,"status":"NOT_CONNECTED"}
