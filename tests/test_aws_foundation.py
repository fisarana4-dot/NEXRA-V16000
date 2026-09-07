import boto3
def test_aws_clients():
 assert boto3.client("s3",region_name="us-east-1")
 assert boto3.client("bedrock-runtime",region_name="us-east-1")
 assert boto3.client("events",region_name="us-east-1")
 assert boto3.client("stepfunctions",region_name="us-east-1")
