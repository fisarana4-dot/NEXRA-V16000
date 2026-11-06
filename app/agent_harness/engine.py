from dataclasses import dataclass
from typing import Any

@dataclass
class HarnessResult:
    status: str
    output: Any = None
    reason: str = ""

class AgentHarness:
    def __init__(self, max_retries: int = 2):
        if max_retries < 0:
            raise ValueError("Invalid retry limit")
        self.max_retries = max_retries

    def stop(self, reason: str) -> HarnessResult:
        return HarnessResult("STOPPED", reason=reason)

    def require_approval(self, reason: str) -> HarnessResult:
        return HarnessResult("HUMAN_APPROVAL", reason=reason)

    def authorize_tool(self, tool: str, allowed: set) -> bool:
        return isinstance(tool, str) and bool(tool.strip()) and isinstance(allowed, (set, frozenset)) and tool in allowed

    def execute_tool(self, tool: str, allowed: set, executor: Any) -> HarnessResult:
        if not self.authorize_tool(tool, allowed):
            return self.stop("Tool not authorized")
        if not callable(executor):
            return self.stop("Invalid executor")
        try:
            result = executor()
        except Exception as exc:
            return self.stop(type(exc).__name__)
        return HarnessResult("COMPLETED", output=result)
