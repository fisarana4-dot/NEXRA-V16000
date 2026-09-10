import pytest
from app.core.mcp.registry import MCPRegistry
from app.core.mcp.registry import MCPRegistry
from app.core.mcp.contracts import MCPServer
def test_registry():
 r=MCPRegistry()
 s=MCPServer(name="x")
 r.register(s)
 assert r.get("x") is s
def test_registry_missing():
 assert MCPRegistry().get("missing") is None
from app.core.mcp.policy import MCPPermissionPolicy
def test_policy():
 p=MCPPermissionPolicy(["gmail.search"])
 assert p.allows("gmail.search")
 assert not p.allows("unknown")
from app.core.mcp.executor import MCPExecutor
def test_executor_denied():
 e=MCPExecutor(MCPPermissionPolicy())
 assert e.execute("unknown")["status"] == "DENIED"
def test_executor_ready():
 e=MCPExecutor(MCPPermissionPolicy(["gmail.search"]))
 r=e.execute("gmail.search",q="test")
 assert r["status"] == "READY"
 assert r["tool"] == "gmail.search"
 assert r["args"]["q"] == "test"
from app.core.mcp.adapter import to_tool_contract
def test_adapter():
 t=MCPTool(name="gmail.search")
 c=to_tool_contract(t)
 assert c.name == "gmail.search"
from app.core.mcp.contracts import MCPTool
def test_registry_list(): r=MCPRegistry(); s=MCPServer(name="x"); r.register(s); assert r.list_servers()==[s]
def test_registry_unregister(): r=MCPRegistry(); s=MCPServer(name="x"); r.register(s); assert r.unregister("x") is s
def test_registry_list_tools():
    r=MCPRegistry(); s=MCPServer(name="x",tools=[MCPTool(name="a")]); r.register(s); assert r.list_tools()==[s.tools[0]]
def test_registry_duplicate():
    r=MCPRegistry(); r.register(MCPServer(name="x"))
    with pytest.raises(ValueError):
        r.register(MCPServer(name="x"))
def test_registry_invalid_server():
    with pytest.raises(TypeError):
        MCPRegistry().register("invalid")
