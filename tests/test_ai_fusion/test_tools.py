import pytest
from app.core.ai_fusion.tools.contract import ToolContract
from app.core.ai_fusion.tools.registry import ToolRegistry
from app.core.ai_fusion.tools.router import ToolRouter
from app.core.ai_fusion.tools.executor import ToolExecutor
from app.core.ai_fusion.tools.schema import ToolParameterSchema
def test_tool_schema_defaults():
    s=ToolParameterSchema(type="object")
    assert s.properties=={} and s.required==[]
def test_tool_schema_type_required():
    with pytest.raises(ValueError):
        ToolParameterSchema(type="")
def test_tool_schema_properties_and_required():
    s=ToolParameterSchema(type="object",properties={"x":{}},required=["x"])
    assert s.properties=={"x":{}} and s.required==["x"]
def test_tool_contract_valid():
    t=ToolContract(name="x",description="d",parameters=ToolParameterSchema(type="object"))
    assert t.name=="x" and t.handler is None
def test_tool_contract_name_required():
    with pytest.raises(ValueError):
        ToolContract(name="",description="d",parameters=ToolParameterSchema(type="object"))
def test_tool_registry_empty():
    assert ToolRegistry().tools=={}
def test_tool_registry_get():
    r=ToolRegistry(); t=ToolContract(name="x",description="d",parameters=ToolParameterSchema(type="object"))
    r.register(t); assert r.get("x") is t
def test_tool_registry_missing():
    assert ToolRegistry().get("missing") is None
def test_tool_registry_overwrite():
    r=ToolRegistry(); a=ToolContract(name="x",description="a",parameters=ToolParameterSchema(type="object"))
    b=ToolContract(name="x",description="b",parameters=ToolParameterSchema(type="object"))
    r.register(a); r.register(b); assert r.get("x") is b
def test_tool_registry_register_count():
    a=ToolContract(name="a",description="a",parameters=ToolParameterSchema(type="object"))
    r=ToolRegistry(); r.register(a); assert len(r.tools)==1
def test_tool_router_missing():
    r=ToolRouter(ToolRegistry()); assert r.route("missing") is None
def test_tool_router_registered():
    r=ToolRegistry(); t=ToolContract(name="x",description="d",parameters=ToolParameterSchema(type="object"))
    r.register(t); q=ToolRouter(r); assert q.route("x") is t
def test_tool_router_identity():
    r=ToolRegistry(); q=ToolRouter(r); assert q.route("x") is None
def test_tool_router_returns_same_tool():
    r=ToolRegistry(); t=ToolContract(name="x",description="d",parameters=ToolParameterSchema(type="object"))
    r.register(t); q=ToolRouter(r); assert q.route("x") is t
def test_tool_router_missing_registry():
    r=ToolRegistry(); q=ToolRouter(r); assert q.route("x") is None
def test_tool_executor_not_found():
    e=ToolExecutor(ToolRouter(ToolRegistry()))
    assert e.run("x")["status"]=="NOT_FOUND"
