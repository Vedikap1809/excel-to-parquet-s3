import boto3
BUCKET_NAME='zmx-training-bucketbatch2025'
FILE_NAME= 'employee.parquet'
s3=boto3.client('s3')
s3.upload_file(FILE_NAME,BUCKET_NAME,'VedikaP/'+FILE_NAME)