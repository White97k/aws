#!/bin/bash

#  Define a region
REGION=ap-southeast-1

# List out codedeploy applications with prefix
APP=aws deploy list-applications --region $REGION --output json | jq -r '.applications[] | select(startswith("xxx"))'

# Reconfigure codedeploy application deployment to CodeDeployDefault.OneAtATime
    aws deploy update-deployment-group --application-name $APP --current-deployment-group-name $APP --deployment-config-name CodeDeployDefault.OneAtATime --region $REGION
done
