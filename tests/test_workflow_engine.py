from app.core.workflow.workflow_engine import WorkflowEngine
def test_workflow():
 w=WorkflowEngine()
 w.define("x",[lambda c:{**c,"ok":1}])
 assert w.run("x")=={"ok":1}
def test_unknown(): assert WorkflowEngine().run("x") == {}
def test_empty_steps(): assert WorkflowEngine().run("x", {"a":1}) == {"a":1}
def test_step_order(): w=WorkflowEngine(); w.define("x",[lambda c:{**c,"a":1},lambda c:{**c,"b":c["a"]+1}]); assert w.run("x")=={"a":1,"b":2}
import pytest
def test_step_error(): w=WorkflowEngine(); w.define("x",[lambda c:1/0]); exec("with pytest.raises(ZeroDivisionError): w.run(\"x\")")
def test_isolated(): w=WorkflowEngine(); w.define("a",[lambda c:{"a":1}]); w.define("b",[lambda c:{"b":2}]); assert w.run("a")=={"a":1}; assert w.run("b")=={"b":2}
