from pydantic import BaseModel, Field
from typing import Any

class MCPTool(BaseModel):
    name: str = Field(min_length=1)
    description: str = ""
    input_schema: dict[str, Any] = Field(default_factory=dict)

class MCPServer(BaseModel):
    name: str = Field(min_length=1)
    description: str = ""
    transport: str = "unknown"
    endpoint: str | None = None
    tools: list[MCPTool] = Field(default_factory=list)
    enabled: bool = True
