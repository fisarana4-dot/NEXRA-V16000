from .base.base_provider import BaseProvider
class ClaudeProvider(BaseProvider):
    name="claude"
    def status(self): return {"provider":self.name,"status":"NOT_CONNECTED"}
