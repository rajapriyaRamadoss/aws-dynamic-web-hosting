aws-dynamic-web-hosting
Dynamic Web Hosting on AWS using EC2, Application Load Balancer, Auto Scaling, CloudWatch, SNS, and Lambda for scalable and monitored web hosting.
# Dynamic Web Hosting on AWS

## Project Overview

Designed and deployed a scalable web hosting infrastructure on Amazon Web Services (AWS) using an Application Load Balancer, EC2 instances across multiple Availability Zones, and an Auto Scaling Group.

The project demonstrates core cloud infrastructure concepts, load balancing, health monitoring, automated notifications, and serverless automation.

## Objectives

- Host a custom website on AWS EC2 instances.
- Distribute incoming HTTP traffic using an Application Load Balancer.
- Improve availability using multiple Availability Zones.
- Configure Auto Scaling to manage web server capacity.
- Monitor infrastructure health using Amazon CloudWatch.
- Send monitoring alerts through Amazon SNS.
- Use AWS Lambda to programmatically inspect EC2 instances.

## AWS Services Used

| Service | Purpose |
|---|---|
| IAM | Identity and access management |
| Amazon VPC | Isolated cloud network |
| Public Subnets | Place web infrastructure across Availability Zones |
| Internet Gateway | Internet connectivity |
| Amazon EC2 | Host Apache web servers |
| Amazon Machine Image (AMI) | Reusable server image |
| Application Load Balancer | Distribute HTTP traffic |
| Target Group | Register and health-check web servers |
| Launch Template | Define EC2 launch configuration |
| Auto Scaling Group | Maintain and adjust instance capacity |
| Amazon CloudWatch | Monitor metrics and trigger alarms |
| Amazon SNS | Deliver email notifications |
| AWS Lambda | Run serverless EC2 inspection code |

## Architecture

Internet → Application Load Balancer → Target Group → EC2 Web Servers across two Availability Zones

CloudWatch → SNS Email Notifications

AWS Lambda → EC2 Instance Inspection

## Implementation Highlights

- Created a custom VPC with CIDR `10.0.0.0/16`.
- Configured two public subnets in separate Availability Zones.
- Set up routing through an Internet Gateway.
- Deployed Apache web servers with custom HTML pages.
- Created an AMI and Launch Template for repeatable instance deployment.
- Registered instances with a target group and verified target health.
- Configured an Application Load Balancer and Auto Scaling Group.
- Created a CloudWatch CPU utilization alarm and SNS email notification.
- Developed and tested a Lambda function that checks running EC2 instances.

## Validation

- Verified that the custom website was accessible.
- Checked target group health.
- Tested the Lambda function and confirmed a successful response containing an EC2 instance ID.
- Configured CloudWatch monitoring and SNS notifications.

## Skills Demonstrated

AWS | Cloud Networking | Linux | Apache | IAM | EC2 | Load Balancing | Auto Scaling | CloudWatch | SNS | AWS Lambda | Python | Troubleshooting

## Future Improvements

- Provision infrastructure using Terraform.
- Implement a CI/CD pipeline using GitHub Actions.
- Add HTTPS using AWS Certificate Manager.
- Improve IAM permissions using least privilege.
- Add automated scaling policies and more comprehensive monitoring.

## Author

Rajapriya R

GitHub: [rajapriyaRamadoss](https://github.com/rajapriyaRamadoss)

