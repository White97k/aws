#!/bin/bash

# Set your AWS region
AWS_REGION="ap-southeast-1" ##edit

# Set your AWS CodeDeploy application name and deployment group name
APPLICATION_NAME="YOUR_APPLICATION_NAME"  ##edit

# List deployments and store IDs in an array
deployments=$(aws deploy list-deployments --application-name $APPLICATION_NAME --deployment-group-name $APPLICATION_NAME --region $AWS_REGION --output text --query 'deployments[*]')
deployment_ids=($deployments)

# Slice the array to include only the recent 5 deployments
recent_deployments=("${deployment_ids[@]: -5}")

# Iterate through recent deployment IDs and get deployment status
for deployment_id in "${recent_deployments[@]}"
do
    if [ "$deployment_id" != "DEPLOYMENTS" ]; then
        status=$(aws deploy get-deployment --deployment-id $deployment_id --region $AWS_REGION --query 'deploymentInfo.status' --output text)
        echo "Deployment ID: $deployment_id, Status: $status"
    fi
done
