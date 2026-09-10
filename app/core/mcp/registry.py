from .contracts import MCPServer
class MCPRegistry:
    def __init__(self): self.servers = {}
    def register(self, server): self.servers[server.name] = server
    def get(self, name): return self.servers.get(name)
    def list_servers(self): return list(self.servers.values())
    def unregister(self,n): return self.servers.pop(n,None)
mcp_registry = MCPRegistry()
