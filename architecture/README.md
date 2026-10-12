# Architecture Documentation

This folder contains the AWS infrastructure architecture diagram and traffic-flow documentation for the Dynamic Web Hosting project.

## High-Level Traffic Flow

1. Users access the website over HTTP.
2. The Application Load Balancer receives incoming requests.
3. The listener forwards requests to the target group.
4. Healthy EC2 web servers respond to requests.
5. CloudWatch monitors infrastructure metrics.
6. SNS sends notifications when configured alarms enter the alarm state.
7. AWS Lambda can inspect EC2 instance information using its execution role.
