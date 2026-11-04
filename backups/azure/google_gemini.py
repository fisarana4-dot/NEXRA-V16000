from app.intelligence.providers.gemini import GeminiProvider as WorkingGemini
class GeminiProvider(WorkingGemini):
 name="gemini"
 def status(self): return {"provider":self.name,"status":"READY"}
