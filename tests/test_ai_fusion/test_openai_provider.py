import pytest
from app.core.ai_fusion.providers import openai as mod
def test_missing_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert mod.OpenAIProvider().status()["status"] == "NOT_CONNECTED"
    with pytest.raises(RuntimeError, match="OPENAI_API_KEY missing"):
        mod.OpenAIProvider().ask("test")
