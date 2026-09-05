from .base.base_provider import BaseProvider
class OpenAIProvider(BaseProvider):
    name="openai"
    def status(self): return {"provider":self.name,"status":"NOT_CONNECTED"}
