import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_elasticache as ec
import aws_cdk.aws_cloudwatch as cw
from aws_cdk import Stack,aws_s3 as s3,aws_dynamodb as ddb,aws_lambda as lam,aws_events as ev,aws_stepfunctions as sf,aws_stepfunctions as sfn,aws_logs as logs
class NexraStack(Stack):
    def __init__(self,scope,id):
        super().__init__(scope,id)
        s3.Bucket(self,"EvidenceBucket",versioned=True,encryption=s3.BucketEncryption.S3_MANAGED,block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
        ddb.Table(self,"EvidenceTable",partition_key=ddb.Attribute(name="tenant_id",type=ddb.AttributeType.STRING),point_in_time_recovery=True,encryption=ddb.TableEncryption.AWS_MANAGED,stream=ddb.StreamViewType.NEW_AND_OLD_IMAGES)
        vpc=ec2.Vpc(self,"NexraVpc",max_azs=2)
        sg=ec2.SecurityGroup(self,"RedisSG",vpc=vpc)
        sub=ec.CfnSubnetGroup(self,"RedisSubnets",subnet_ids=vpc.private_subnets)
        ec.CfnCacheCluster(self,"Redis",engine="redis",cache_node_type="cache.t3.micro",num_cache_nodes=1,port=6379,cache_subnet_group_name=sub.ref,vpc_security_group_ids=[sg.security_group_id])
        task=lam.Function(self,"TaskHandler",runtime=lam.Runtime.PYTHON_3_12,handler="index.handler",timeout=cdk.Duration.seconds(30),memory_size=256,code=lam.Code.from_inline("def handler(event,context): return event"))
        logs.LogGroup(self,"TaskLogs",retention=logs.RetentionDays.ONE_MONTH)
        cw.Alarm(self,"TaskErrors",metric=task.metric_errors(),evaluation_periods=1,threshold=1)
        cw.Dashboard(self,"NexraDash")
        ev.Rule(self,"TaskEvents",event_pattern=ev.EventPattern(source=["nexra"]))
        sf.Pass(self,"DecisionStep")
        sf.StateMachine(self,"DecisionFlow",definition_body=sfn.DefinitionBody.from_chainable(sf.Pass(self,"FlowStep")))
app=cdk.App(outdir='cdk.out')
NexraStack(app,"NexraFoundation")
app.synth()
