import aws_cdk as cdk
from aws_cdk import Stack,aws_s3 as s3,aws_dynamodb as ddb,aws_lambda as lam,aws_events as ev,aws_stepfunctions as sf,aws_stepfunctions as sfn
class NexraStack(Stack):
    def __init__(self,scope,id):
        super().__init__(scope,id)
        s3.Bucket(self,"EvidenceBucket",versioned=True)
        ddb.Table(self,"EvidenceTable",partition_key=ddb.Attribute(name="tenant_id",type=ddb.AttributeType.STRING))
        lam.Function(self,"TaskHandler",runtime=lam.Runtime.PYTHON_3_12,handler="index.handler",code=lam.Code.from_inline("def handler(event,context): return event"))
        ev.Rule(self,"TaskEvents",event_pattern=ev.EventPattern(source=["nexra"]))
        sf.Pass(self,"DecisionStep")
        sf.StateMachine(self,"DecisionFlow",definition_body=sfn.DefinitionBody.from_chainable(sf.Pass(self,"FlowStep")))
app=cdk.App(outdir='cdk.out')
NexraStack(app,"NexraFoundation")
app.synth()
