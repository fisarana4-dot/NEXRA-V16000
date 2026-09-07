import os
from openai import OpenAI
from .base.base_provider import BaseProvider
class GroqProvider(BaseProvider):
    name="groq"
    model="openai/gpt-oss-120b"
    def __init__(self):
        self.key=os.getenv("GROQ_API_KEY")
        self.client=None
        self.base_url="https://api.groq.com/openai/v1"
    def status(self):
        s="READY" if self.key else "NOT_CONNECTED"
        return {"provider":self.name,"status":s}
    def ask(self,text):
        if not self.key: raise RuntimeError("GROQ_API_KEY missing")
        if self.client is None: self.client=OpenAI(api_key=self.key,base_url=self.base_url)
        r=self.client.responses.create(model=self.model,input=text)
        return r.output_text
