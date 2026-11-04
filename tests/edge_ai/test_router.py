from src.edge_ai.router import EdgeAIRouter

def test_edge_routing():
    assert EdgeAIRouter().route("test") == "local_edge_routed"

def test_edge_ai_fallback():
    assert EdgeAIRouter().fallback() == "cloud_fallback_active"
