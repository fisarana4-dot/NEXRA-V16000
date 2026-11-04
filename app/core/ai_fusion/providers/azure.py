import os
import httpx
from .base.base_provider import BaseProvider
class AzureProvider(BaseProvider):
    name="azure"
    def __init__(self):
        self.endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        self.key=os.getenv("AZURE_OPENAI_API_KEY")
        self.model=os.getenv("AZURE_OPENAI_MODEL")
    def status(self):
        ok=bool(self.endpoint and self.key and self.model)
        s="READY" if ok else "NOT_CONFIGURED"
        return {"provider":self.name,"status":s}
    def ask(self,text):
        if self.status()["status"]!="READY":
            return "AZURE_NOT_CONFIGURED"
        u=self.endpoint.rstrip("/")+"/openai/v1/chat/completions"
        h={"api-key":self.key,"Content-Type":"application/json"}
        d={"model":self.model,"messages":[{"role":"user","content":text}]}
        try:
            r=httpx.post(u,headers=h,json=d,timeout=30)
            r.raise_for_status()
            return r.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return "AZURE_ERROR:"+type(e).__name__
