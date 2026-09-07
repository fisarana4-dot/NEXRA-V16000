from app.core.workflow.workflow_engine import WorkflowEngine
def test_workflow():
 w=WorkflowEngine()
 w.define("x",[lambda c:{**c,"ok":1}])
 assert w.run("x")=={"ok":1}
