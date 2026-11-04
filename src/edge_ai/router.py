class EdgeAIRouter:
    def route(self, prompt: str) -> str:
        return "local_edge_routed"


    def fallback(self) -> str:
        return "cloud_fallback_active"
