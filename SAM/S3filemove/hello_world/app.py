import json
import boto3
from datetime import date

today = date.today()
todaydate=today.strftime("%Y%m%d")
s3_client = boto3.client("s3")

def lambda_handler(event, context):
    # TODO implement

    destination_bucket_name = 'myprojects-all'

    # event contains all information about uploaded object
    print("Event :", event)

    # Bucket Name where file was uploaded
    source_bucket_name = event['Records'][0]['s3']['bucket']['name']

    # Filename of object (with path)
    file_key_name_src = event['Records'][0]['s3']['object']['key']

    file_key_name_tgt = 'data/processed/'+todaydate+'/'+file_key_name_src.split('/')[-1]

    # Copy Source Object
    copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name_src}

    # S3 copy object operation
    s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name_tgt)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
