from .base.base_provider import BaseProvider
class GrokProvider(BaseProvider):
    name="grok"
    def status(self): return {"provider":self.name,"status":"NOT_CONNECTED"}
