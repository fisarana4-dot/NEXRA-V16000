from .base.base_provider import BaseProvider
class CopilotProvider(BaseProvider):
    name="copilot"
    def status(self): return {"provider":self.name,"status":"NOT_CONNECTED"}
