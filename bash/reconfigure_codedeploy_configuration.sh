#!/bin/bash


# Reconfigure codedeploy application deployment to CodeDeployDefault.OneAtATime
    aws deploy update-deployment-group --application-name $ASG --current-deployment-group-name $ASG --deployment-config-name CodeDeployDefault.OneAtATime --region $REGION
done
