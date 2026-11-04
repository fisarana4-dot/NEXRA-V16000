from app.core.mcp.contracts import MCPTool, MCPServer
def test_tool():
    t=MCPTool(name="gmail.search")
    assert t.name == "gmail.search"


def test_server():
    s=MCPServer(name="gmail", transport="http")
    assert s.name == "gmail"
    assert s.transport == "http"
import pytest
def test_tool_name_required():
    with pytest.raises(Exception):
        MCPTool(name="")
def test_server_name_required():
    with pytest.raises(Exception):
        MCPServer(name="")
def test_server_transport_invalid():
    with pytest.raises(ValueError):
        MCPServer(name="x",transport="ftp")
