import pytest
from app.agent_harness.engine import AgentHarness
def test_harness_initializes():
    assert AgentHarness().max_retries == 2
def test_harness_stop():
    assert AgentHarness().stop("test").status == "STOPPED"
def test_harness_requires_approval():
    assert AgentHarness().require_approval("risk").status == "HUMAN_APPROVAL"
def test_negative_retries_rejected():
    with pytest.raises(ValueError):
        AgentHarness(-1)
def test_authorized_tool():
    assert AgentHarness().authorize_tool("search", {"search"})
def test_unauthorized_tool():
    assert not AgentHarness().authorize_tool("delete", {"search"})
def test_empty_tool_rejected():
    assert not AgentHarness().authorize_tool("", {"search"})
def test_none_tool_rejected():
    assert not AgentHarness().authorize_tool(None, {"search"})
def test_invalid_allowlist_rejected():
    assert not AgentHarness().authorize_tool("search", None)
def test_authorized_execution():
    r = AgentHarness().execute_tool("search", {"search"}, lambda: 42)
    assert r.status == "COMPLETED" and r.output == 42
def test_unauthorized_execution_blocked():
    called = []
    r = AgentHarness().execute_tool(
        "delete", {"search"}, lambda: called.append(True)
    )
    assert r.status == "STOPPED"
    assert called == []
def test_invalid_executor_blocked():
    r = AgentHarness().execute_tool("search", {"search"}, None)
    assert r.status == "STOPPED"
    assert r.reason == "Invalid executor"

def test_executor_exception_stops_safely():
    def fail():
        raise RuntimeError("failure")

    r = AgentHarness().execute_tool("search", {"search"}, fail)
    assert r.status == "STOPPED"
    
    assert r.reason == "RuntimeError"
