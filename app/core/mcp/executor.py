class MCPExecutor:
    def __init__(self, policy): self.policy = policy
    def check(self, name): return self.policy.allows(name)
    def execute(self, name, **kwargs):
        if not self.check(name): return {"status": "DENIED"}
        return {"status": "READY", "tool": name, "args": kwargs}
