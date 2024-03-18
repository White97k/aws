#!/usr/bin/env python
import boto3
from datetime import datetime, timedelta
import time

# Define the region
region = 'ap-southeast-1'  # Replace 'your-region' with your desired AWS region, e.g., 'us-west-1'

print('\n #### in progress... #### \n')

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
    deployment_statuses = []
    for deployment_id in response['deployments']:
        deployment_info = client.get_deployment(deploymentId=deployment_id)
        deployment_status = deployment_info['deploymentInfo']['status']
        application_name = deployment_info['deploymentInfo']['applicationName']
        deployment_statuses.append(deployment_status)
        print("{}, {}, {}".format(application_name, deployment_id, deployment_status))

    return deployment_statuses


# Loop to keep accessing deployments every 30 seconds
while True:
    statuses = get_deployments(region)
    print('\n #### end ### \n')
    if all(status in ['Succeeded', 'Failed', 'Stopped'] for status in statuses):
        print('All deployments have reached a terminal state.')
        break

    time.sleep(30)  # Sleep for 30 seconds before accessing deployments again
