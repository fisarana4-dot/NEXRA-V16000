from app.core.mcp.transport import MCPTransport
def test_default(): assert MCPTransport().kind == "unknown"
def test_supported():
    t=MCPTransport(); assert t.supports("stdio")
    assert t.supports("http"); assert t.supports("sse")
def test_unsupported():
    assert not MCPTransport().supports("ftp")
