from app.providers.gemini_provider import GeminiProvider as G
class GeminiProvider(G):
 name="gemini"
 def ask(s,text):return s.generate(text)["candidates"][0]["content"]["parts"][0]["text"]
gemini_provider=GeminiProvider()
