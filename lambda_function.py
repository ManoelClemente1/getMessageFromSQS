import json
import boto3


AWS_REGION = 'us-east-2'

sqs_client = boto3.client("sqs", region_name=AWS_REGION)

def lambda_handler(event, context):
        
        response = sqs_client.receive_message(
            QueueUrl="",
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
            )
            
        print(response)
        
        for message in response.get("Messages", []):
            message_body = ["Body"]
            print(f"Message body: {json.loads(message_body)}"")
        
    }
