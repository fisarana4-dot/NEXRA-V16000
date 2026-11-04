from .base.base_provider import BaseProvider
class MetaProvider(BaseProvider):
    name="meta"
    def status(self): return {"provider":self.name,"status":"NOT_CONNECTED"}
