import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='your_access_key_id',
    aws_secret_access_key='your_secret_access_key',
    region_name='your_aws_region'
)
