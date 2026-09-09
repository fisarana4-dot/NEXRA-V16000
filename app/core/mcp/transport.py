class MCPTransport:
    def __init__(self, kind="unknown"): self.kind = kind
    def supports(self, kind): return kind in {"stdio", "http", "sse"}
