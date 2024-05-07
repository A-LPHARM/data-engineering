import boto3
import os
import json
import time
import random


# Retrieve AWS credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Check if credentials are loaded
if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    raise Exception("AWS credentials are not set in environment variables.")

# Initialize the Kinesis client
region_name = 'us-east-1'

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=region_name)

def put_weather_data(city, temperature, humidity, wind_speed):
    try:
        data = {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "timestamp": int(time.time())
        }

        response = kinesis_client.put_record(
            StreamName='kinesis-data-streaming',
            Data=json.dumps(data),
            PartitionKey='city'
        )
        print(f"Weather information. SequenceNumber: {response['SequenceNumber']}, ShardId: {response['ShardId']}, Data: {data}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cities = ["Lagos", "Abuja", "Accra", "Houston", "New york", "ondo", "texas", "london"]

    for _ in range(8):
        city = random.choice(cities)
        temperature = round(random.uniform(-10, 40), 2)
        humidity = round(random.uniform(40, 80), 2)
        wind_speed = round(random.uniform (0, 100), 2)

        put_weather_data(city, temperature, humidity, wind_speed)
        time.sleep(2)  # Simulating periodic data transmission
