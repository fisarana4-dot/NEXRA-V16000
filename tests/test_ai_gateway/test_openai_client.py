import pytest
from app.core.ai_fusion.providers.openai import OpenAIProvider
def test_openai_status_without_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert OpenAIProvider().status()["status"]=="NOT_CONNECTED"
def test_openai_ask_without_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        OpenAIProvider().ask("test")
