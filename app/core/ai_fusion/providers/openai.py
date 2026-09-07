import os
from openai import OpenAI
from .base.base_provider import BaseProvider
class OpenAIProvider(BaseProvider):
    name="openai"
    model="gpt-5"
    def __init__(self):
        self.key=os.getenv("OPENAI_API_KEY")
        self.client=None
    def status(self):
        s="READY" if self.key else "NOT_CONNECTED"
        return {"provider":self.name,"status":s}
    def ask(self,text):
        if not self.key: raise RuntimeError("OPENAI_API_KEY missing")
        if self.client is None: self.client=OpenAI(api_key=self.key)
        r=self.client.responses.create(model=self.model,input=text)
        return r.output_text
