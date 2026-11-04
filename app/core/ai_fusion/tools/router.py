class ToolRouter:
    def __init__(self, registry): self.registry = registry
    def route(self, name): return self.registry.get(name)
from .registry import tool_registry
tool_router = ToolRouter(tool_registry)
