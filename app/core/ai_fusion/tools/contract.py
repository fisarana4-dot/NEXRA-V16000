from pydantic import BaseModel, Field
from typing import Callable, Any
from .schema import ToolParameterSchema
class ToolContract(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    parameters: ToolParameterSchema
    handler: Callable[..., Any] | None = None
