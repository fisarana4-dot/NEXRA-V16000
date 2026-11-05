import pytest
from app.ai_agents import buyer_discovery_agent as mod

def test_buyer_agent_delegates_to_gateway(monkeypatch):
    calls = {}
    expected = {"buyers": ["Buyer A"]}
    def fake_process(provider, request):
        calls["provider"] = provider
        calls["request"] = request
        return expected

    monkeypatch.setattr(mod.gateway, "process", fake_process)
    result = mod.buyer_agent.find_buyers("healthcare")
    assert calls["provider"] == "openai"
    assert calls["request"] == "healthcare"
    assert result == expected

def test_buyer_agent_propagates_gateway_error(monkeypatch):
    def fail_process(provider, request):
        raise RuntimeError("Gateway unavailable")
    monkeypatch.setattr(mod.gateway, "process", fail_process)
    with pytest.raises(RuntimeError, match="Gateway unavailable"):
        mod.buyer_agent.find_buyers("healthcare")

@pytest.mark.parametrize("market", ["", "   ", None, 123])
def test_buyer_agent_rejects_invalid_market(market):
    with pytest.raises(ValueError):

        mod.buyer_agent.find_buyers(market)
