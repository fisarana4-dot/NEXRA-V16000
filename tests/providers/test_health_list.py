from app.core.ai_fusion.health import provider_health as h
def test_groq_in_health_providers():
 assert "groq" in h.PROVIDERS
def test_groq_in_chain():
 assert "groq" in h.chain()
