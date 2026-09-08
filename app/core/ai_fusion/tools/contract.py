from pydantic import BaseModel,Field
from .schema import ToolParameterSchema
class ToolContract(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    parameters: ToolParameterSchema
