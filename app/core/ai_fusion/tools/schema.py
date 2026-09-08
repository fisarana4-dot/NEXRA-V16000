from pydantic import BaseModel, Field
class ToolParameterSchema(BaseModel):
    type: str = Field(min_length=1)
    properties: dict = Field(default_factory=dict)
    required: list[str] = Field(default_factory=list)
