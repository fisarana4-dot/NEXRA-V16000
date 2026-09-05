from app.intelligence.providers.gemini import gemini_provider
class ProviderRouter:
 def route(s,p):return gemini_provider if p=="gemini" else p
router=ProviderRouter()
