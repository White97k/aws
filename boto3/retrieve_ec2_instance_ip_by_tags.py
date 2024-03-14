#!/usr/bin/env python

import boto3

# Define the region
region = 'ap-southeast-1'  # Replace 'your-region' with your desired AWS region, e.g., 'us-west-1'

# Define the tag value
tag_value = input('please input your ec2-tag value: ')

# Initialize EC2 client
ec2_client = boto3.client('ec2', region_name=region)

# Define filters
filters = [
    {'Name': 'tag:Name', 'Values': [tag_value]},
  #  {'Name': 'tag:Prod_env', 'Values': ['uat01']}
]

# Describe instances
response = ec2_client.describe_instances(Filters=filters)

# Extract Private IP addresses
private_ip_addresses = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        private_ip_addresses.append(instance['PrivateIpAddress'])

print(private_ip_addresses)
