class ToolExecutor:
    def __init__(self, router): self.router = router
    def execute(self, name): return self.router.route(name)
    def run(self, name, **kwargs):
        tool = self.router.route(name)
        if tool is None: return {"status":"NOT_FOUND"}
        if tool.handler is None: return {"status":"NO_HANDLER"}
        return tool.handler(**kwargs)
from .router import tool_router
tool_executor = ToolExecutor(tool_router)
