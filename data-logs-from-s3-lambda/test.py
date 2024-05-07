import json
import boto3
import csv
import io

s3Client = boto3.client('s3')  #this is used to call the object in the bucket

def lambda_handler(event, context):

    # here it will check the event records the first one 0 then it checks the s3 and find the bucket and the name using the event name 
    bucket = event['Records'][0]['s3']['bucket']['name']  
    key = event['Records'][0]['s3']['object']['key']
    
    print(bucket)
    print(key)
    
    #determine the object
    response = s3Client.get_object(Bucket=bucket, Key=key)
    
    #Process it
    data = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(data))
    next(reader)
    for row in reader:
        print(str.format("SKU = {}, Product = {}, Location = {}", row[0], row[1], row[2]))