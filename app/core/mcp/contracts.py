from pydantic import BaseModel, Field
from pydantic import field_validator
from typing import Any

class MCPTool(BaseModel):
    name: str = Field(min_length=1)
    description: str = ""
    input_schema: dict[str, Any] = Field(default_factory=dict)

class MCPServer(BaseModel):
    name: str = Field(min_length=1)
    description: str = ""
    transport: str = "unknown"
    @field_validator("transport")
    @classmethod
    def validate_transport(cls,v):
        if v not in {"unknown","stdio","http","sse"}:
            raise ValueError("Invalid transport")
        return v
    endpoint: str | None = None
    tools: list[MCPTool] = Field(default_factory=list)
    enabled: bool = True
