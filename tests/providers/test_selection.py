import os
from app.core.ai_fusion.health import provider_health as h
def test_chain_selects_groq(monkeypatch):
 monkeypatch.setenv("GROQ_API_KEY","x")
 assert h.choose(h.chain())=="groq"
