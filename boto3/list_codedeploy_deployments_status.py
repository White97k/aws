#!/usr/bin/env python
import boto3
from datetime import datetime, timedelta
import time

def get_deployments(region):
    # Initialize CodeDeploy client with the specified region
    client = boto3.client('codedeploy', region_name=region)

    # Get today's date
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # Calculate the end of today
    end_of_today = today + timedelta(days=1)

    # List deployments
    response = client.list_deployments(
        includeOnlyStatuses=[
            'Created',
            'Queued',
            'InProgress',
            'Baking',
            'Succeeded',
            'Failed',
            'Stopped',
            'Ready',
        ],
        createTimeRange={
            'start': today,
            'end': end_of_today
        }
    )

    # Get deployment details with deploymentInfo status
    for deployment_id in response['deployments']:
        deployment_info = client.get_deployment(deploymentId=deployment_id)
        deployment_status = deployment_info['deploymentInfo']['status']

        print("{}, Status: {}".format(deployment_id, deployment_status))


# Define the region
region = 'ap-southeast-1'  # Replace 'your-region' with your desired AWS region, e.g., 'us-west-1'

# Loop to keep accessing deployments every 30 seconds
while True:
    get_deployments(region)
    time.sleep(30)  # Sleep for 30 seconds before accessing deployments again
    print('\n#### in progressing... ####\n')
