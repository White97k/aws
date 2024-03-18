#!/bin/bash

Service=$(jps | grep jar | awk '{print $2}' | awk -F '.jar' '/\.jar$/{print $(NF-1)}')

# Fetch the status of checks from Consul agent
status=$(curl -s 127.0.0.1:8500/v1/agent/checks | jq -r '.[] | .Status')

# Check if the status is "passing"
if [[ "$status" == "passing" ]]; then
    echo " $Service checks are passing."

# Check if the status is "critical"
elif [[ "$status" == "critical" ]]; then
    echo "Service checks are critical, and Restarting $Service.service"
    systemctl restart jx-$Service.service
else
    echo "Service checks are not passing. Status: $status"
fi
