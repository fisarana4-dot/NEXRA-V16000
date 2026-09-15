import boto3
def test_aws_services():
 assert all(boto3.client(s,region_name="us-east-1") for s in ["s3","events"])
 assert boto3.client("bedrock-runtime",region_name="us-east-1")
 assert boto3.client("stepfunctions",region_name="us-east-1")
