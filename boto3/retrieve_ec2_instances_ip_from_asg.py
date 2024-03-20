#!/usr/bin/env python

import boto3

def get_instance_ids_from_auto_scaling_group(auto_scaling_group_name, region_name):
    # Create a boto3 session with specified region
    session = boto3.Session(region_name=region_name)

    # Create a boto3 client for Auto Scaling
    autoscaling_client = session.client('autoscaling')

    # Describe the Auto Scaling Group
    response = autoscaling_client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[auto_scaling_group_name]
    )

    # Extract instance IDs from the Auto Scaling Group
    instance_ids = []
    for group in response['AutoScalingGroups']:
        for instance in group['Instances']:
            instance_ids.append(instance['InstanceId'])

    return instance_ids

def describe_instances(instance_ids, region_name):
    # Create a boto3 session with specified region
    session = boto3.Session(region_name=region_name)

    # Create a boto3 client for EC2
    ec2_client = session.client('ec2')

    # Describe instances
    response = ec2_client.describe_instances(
        InstanceIds=instance_ids
    )

    # Extract instance information
    instances_info = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A')
            }
            instances_info.append(instance_info)

    return instances_info

if __name__ == "__main__":
    print('Ensure your AWS profile is authorised permission to perform this action')
    print("\n Warn, your input must be used FULL NAME of asg \n ")
    auto_scaling_group_name = input('Input your ASG: ')
    region_name = 'ap-southeast-1'

    # Get instance IDs from the specified Auto Scaling Group
    instance_ids = get_instance_ids_from_auto_scaling_group(auto_scaling_group_name, region_name)

    # Describe instances
    instances_info = describe_instances(instance_ids, region_name)

    # Print instance information
    print('')
    print("Instances in Auto Scaling Group:", auto_scaling_group_name)
    print('\n')
    for instance_info in instances_info:
        print("Instance ID:", instance_info['InstanceId'])
        print("Instance Type:", instance_info['InstanceType'])
        print("Public IP Address:", instance_info['PublicIpAddress'])
        print("Private IP Address:", instance_info['PrivateIpAddress'])
        print("--------------------------------------------")
