## Real-Time Data Processing with AWS Kinesis and Lambda

This project demonstrates how to collect real-time weather data from IoT devices, process it through AWS Kinesis, and trigger AWS Lambda functions for further processing and storage in S3 buckets. The processed data can then be visualized using AWS CloudWatch.

### Architecture Overview

The solution utilizes:
- **AWS Kinesis**: Manages real-time ingestion and processing of data streams from IoT devices.
- **AWS Lambda**: Processes incoming data from Kinesis and stores it in an S3 bucket.
- **Amazon S3**: Serves as the storage solution for processed data.
- **AWS CloudWatch**: Used for monitoring operations and visualizing data.

### Prerequisites

- AWS account
- AWS CLI installed
- Python 3 and Boto3 SDK
- IAM roles with appropriate permissions

### Setup and Configuration

1. **IAM Role Creation**:
    - Navigate to the IAM console and create a new role with the following permissions:
        - `AmazonKinesisFullAccess`
        - `CloudWatchLogsFullAccess`
        - `AmazonS3FullAccess`
        - `AWSLambdaBasicExecutionRole`
        - `AWSXRayFullAccess`
        - `AWSLambda_FullAccess`

2. **S3 Bucket Setup**:
    - Create an S3 bucket named `data-kinesis-s3-logs` to store the processed data in JSON format.

3. **Kinesis Stream Configuration**:
    - Create a Kinesis stream named `kinesis-data-streaming` with 2 shards.

4. **Lambda Function Deployment**:
    - Create a new Lambda function named `datalogs-s3-kinesis` with Python 3.9 runtime.
    - Attach the previously created IAM role.
    - Add Kinesis as the trigger with a batch size of 2.
    - Replace the default Lambda function code with the provided Python script.
    - Deploy the code by clicking "Deploy".

5. **AWS CLI and Python Environment Setup**:
    - Install the AWS CLI and configure your AWS credentials.
    - Install Python and the Boto3 library.
    - Set environment variables for AWS credentials.

### Data Simulation and Streaming

Run the Python script to simulate an IoT device generating weather data. The script sends data to the Kinesis stream, which is then processed by the Lambda function and stored in S3.

```bash
python3 lambda-weather.py
```

### Monitoring and Validation

- **CloudWatch Logs**: Confirm the Lambda function's execution and success.
- **S3 Bucket**: Verify that the data is correctly stored in the S3 bucket.

For more detailed guidance, refer to the [comprehensive blog post on Medium](https://alpharm.medium.com)
---

This README.md provides a brief overview of the system architecture, setup instructions, and operational steps to get the solution up and running.