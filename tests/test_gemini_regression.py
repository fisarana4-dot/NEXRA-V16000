from app.intelligence.providers.gemini import GeminiProvider
def test_gemini_provider(): p=GeminiProvider(); assert p.name=="gemini" and callable(p.ask)
