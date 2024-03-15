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
]

# Describe instances
response = ec2_client.describe_instances(Filters=filters)

# Extract instance ID, private IP addresses, and tags
instances_info = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        private_ip_address = instance['PrivateIpAddress']
        tags = instance.get('Tags', [])
        name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), None)
        instance_info = {'InstanceId': instance_id, 'PrivateIpAddress': private_ip_address, 'Name': name_tag}
        instances_info.append(instance_info)

# Print instances information
for instance_info in instances_info:
    print("Instance ID:", instance_info['InstanceId'])
    print("Private IP Address:", instance_info['PrivateIpAddress'])
    print("Tag:", instance_info['Name'])
    print(' ')
