import os
from app.intelligence.providers.gemini import GeminiProvider as WorkingGemini
class GeminiProvider(WorkingGemini):
    name="gemini"
    def status(self):
        ok=bool(os.getenv("GEMINI_API_KEY"))
        s="CONFIGURED" if ok else "NOT_CONFIGURED"
        return {"provider":self.name,"status":s}
