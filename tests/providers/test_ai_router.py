from app.core.ai_fusion.router.ai_router import AIRouter
def test_router_uses_selected_provider(monkeypatch):
 monkeypatch.setenv("GROQ_API_KEY","x")
 r=AIRouter()
 assert r.selected=="groq"
 assert r.provider.name=="groq"


def test_router_provider_matrix(monkeypatch):
 for p in ["gemini","groq","openai"]:
  monkeypatch.delenv("GEMINI_API_KEY",raising=False)
  monkeypatch.delenv("GROQ_API_KEY",raising=False)
  monkeypatch.delenv("OPENAI_API_KEY",raising=False)
  monkeypatch.setenv(p.upper()+"_API_KEY","x")
  r=AIRouter(); assert r.provider.name==p
