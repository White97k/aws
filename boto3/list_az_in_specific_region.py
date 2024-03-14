#!/usr/bin/env python
import boto3

region = 'ap-southeast-1'
ec2 = boto3.client('ec2', region_name=region)

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()

for zone in response['AvailabilityZones']:
    print(zone['ZoneName'])
