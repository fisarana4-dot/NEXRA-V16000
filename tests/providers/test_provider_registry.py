from app.providers.registry.provider_registry import ProviderRegistry
def test_groq_registry():
 r=ProviderRegistry()
 assert r.get("groq")=="groq"
