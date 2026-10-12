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


## Architecture and Traffic Flow

### Web Traffic

1. A user sends an HTTP request to the Application Load Balancer.
2. The ALB listener forwards the request to the configured target group.
3. The target group routes traffic to healthy EC2 web servers.
4. Apache serves the custom HTML website from the selected instance.

### Availability and Scaling

- Two public subnets are configured in separate Availability Zones.
- The Auto Scaling Group uses a Launch Template to define EC2 instances.
- The target group health checks help identify unhealthy web servers.
- The Auto Scaling Group is configured with minimum, desired, and maximum capacity.

### Monitoring and Automation

- CloudWatch monitors EC2 CPU utilization.
- An alarm can notify an SNS topic when its configured threshold is breached.
- The Lambda function queries EC2 to identify matching running instances.

### Security Notes

- Security groups control inbound traffic.
- IAM roles provide permissions to AWS services.
- The Lambda execution role has EC2 read-only permissions for instance inspection.
