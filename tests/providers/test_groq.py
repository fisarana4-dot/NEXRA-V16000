from app.core.ai_fusion.providers.groq import GroqProvider
def test_groq_status(monkeypatch):
 monkeypatch.delenv("GROQ_API_KEY", raising=False)
 assert GroqProvider().status()["status"]=="NOT_CONNECTED"
from app.providers.registry.provider_router import router
def test_groq_router():
 assert router.route("groq").name=="groq"
