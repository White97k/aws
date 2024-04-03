#!/bin/bash

# Set the region
region="ap-southeast-1"

# Get the Auto Scaling Group name from user input
read -p "Enter the name of the Auto Scaling Group: " auto_scaling_group_name

# Retrieve the instance IDs of the specified Auto Scaling Group
instance_ids=$(aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names $auto_scaling_group_name --region $region --query "AutoScalingGroups[].Instances[].InstanceId" --output text)

# Loop through each instance ID and retrieve its IP address
for instance_id in $instance_ids; do
    # Retrieve the instance IP address
    instance_ip=$(aws ec2 describe-instances --instance-ids $instance_id --region $region --query "Reservations[].Instances[].PrivateIpAddress" --output text)
    
    # Output the instance ID and IP address
    echo "Instance ID: $instance_id, IP Address: $instance_ip"
done
