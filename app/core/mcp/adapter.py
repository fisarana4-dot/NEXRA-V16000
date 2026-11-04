from .contracts import MCPServer, MCPTool
from openai.types.responses import FunctionToolParam
from app.core.ai_fusion.tools.contract import ToolContract
def to_tool_contract(tool: MCPTool, handler=None):
    return ToolContract(name=tool.name, description=tool.description or "MCP tool",
        parameters=ToolParameterSchema(**(tool.input_schema or {"type":"object"})), handler=handler)
def to_openai_tool(tool):
    return FunctionToolParam(type="function",name=tool.name,parameters=tool.input_schema or {"type":"object"},strict=False)
from app.core.ai_fusion.tools.schema import ToolParameterSchema
