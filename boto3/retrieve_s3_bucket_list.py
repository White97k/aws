#!/usr/bin/env python

# Retrieve the list of existing buckets
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
for bucket in response['Buckets']:
    print(bucket["Name"])
