# AWS Lambda Automation

The Lambda function uses Python and the AWS SDK for Python (Boto3) to inspect running EC2 instances matching the configured Name tag.

## Functionality

- Queries EC2 instance information.
- Filters for the `web-server-1` Name tag.
- Returns matching running instance IDs.
- Uses an IAM execution role with EC2 read-only permissions.

## Validation

The function was tested successfully and returned HTTP-style status code 200 with a matching EC2 instance ID.
