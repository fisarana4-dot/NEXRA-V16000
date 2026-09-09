from .contracts import MCPServer
class MCPRegistry:
    def __init__(self): self.servers = {}
    def register(self, server): self.servers[server.name] = server
    def get(self, name): return self.servers.get(name)
mcp_registry = MCPRegistry()
