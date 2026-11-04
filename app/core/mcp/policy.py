class MCPPermissionPolicy:
    def __init__(self, allowed=None): self.allowed = set(allowed or [])
    def allows(self, name): return name in self.allowed
