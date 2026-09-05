from .base.base_provider import BaseProvider
class DeepSeekProvider(BaseProvider):
    name="deepseek"
    def status(self): return {"provider":self.name,"status":"NOT_CONNECTED"}
