from app.core.ai_fusion.router.ai_router import AIRouter
def test_router_uses_selected_provider(monkeypatch):
 monkeypatch.setenv("GROQ_API_KEY","x")
 r=AIRouter()
 assert r.selected=="groq"
 assert r.provider.name=="groq"
