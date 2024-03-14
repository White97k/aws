#!/usr/bin/env python
import boto3

# Define the region
region = 'ap-southeast-1'  # Replace 'your-region' with your desired AWS region, e.g., 'us-west-1'

ec2 = boto3.client('ec2', region_name=region)
response = ec2.describe_key_pairs()

for keypair in response['KeyPairs']:
    print(keypair["KeyName"])
