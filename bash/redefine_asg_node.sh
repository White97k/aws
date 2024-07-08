#!/bin/bash

REGION=ap-southeast-1

# List out ASG list with prefix
for ASG in $(aws autoscaling describe-auto-scaling-groups --query 'AutoScalingGroups[?starts_with(AutoScalingGroupName, `xxx-`)].AutoScalingGroupName' --output text --region $REGION); do
# Set desired capacity to 1 with min size 0
    aws autoscaling update-auto-scaling-group --auto-scaling-group-name $ASG --desired-capacity 1 --min-size 0 --region $REGION
