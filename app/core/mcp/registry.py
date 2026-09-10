from .contracts import MCPServer
class MCPRegistry:
    def __init__(self): self.servers = {}
    def register(self, server):
        if not isinstance(server, MCPServer):
            raise TypeError("server must be MCPServer")
        if server.name in self.servers:
            raise ValueError("Server already registered")
        self.servers[server.name] = server
    def get(self, name): return self.servers.get(name)
    def list_servers(self): return list(self.servers.values())
    def unregister(self,n): return self.servers.pop(n,None)
    def has(self, name): return name in self.servers
    def list_tools(self):
        return [t for s in self.servers.values() for t in s.tools]
mcp_registry = MCPRegistry()
