from app.core.ai_fusion.providers.gemini import GeminiProvider
from app.core.ai_fusion.providers.groq import GroqProvider
from app.core.ai_fusion.providers.openai import OpenAIProvider
from app.providers.registry.provider_registry import provider_registry
class ProviderRouter:
    def route(self,provider):
        if provider=="gemini": return GeminiProvider()
        if provider=="openai": return OpenAIProvider()
        if provider=="groq": return GroqProvider()
        return provider_registry.resolve(provider)
router=ProviderRouter()
