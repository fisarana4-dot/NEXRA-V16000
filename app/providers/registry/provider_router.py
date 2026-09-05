from app.core.ai_fusion.providers.gemini import GeminiProvider
from app.providers.registry.provider_registry import provider_registry
class ProviderRouter:
    def route(self, provider): return GeminiProvider() if provider=='gemini' else provider_registry.resolve(provider)
router=ProviderRouter()
