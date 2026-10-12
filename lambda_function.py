import json
import boto3

ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    response = ec2.describe_instances(
        Filters=[
            {"Name": "tag:Name", "Values": ["web-server-1"]},
            {"Name": "instance-state-name", "Values": ["running"]}
        ]
    )

    instances = [
        instance["InstanceId"]
        for reservation in response["Reservations"]
        for instance in reservation["Instances"]
    ]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "EC2 instance check completed",
            "instances": instances
        })
    }
