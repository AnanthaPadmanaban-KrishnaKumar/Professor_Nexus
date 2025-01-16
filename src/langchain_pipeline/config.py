import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_bedrock_client():
    """
    Returns an Amazon Bedrock client using credentials and region from the environment.
    """
    return boto3.client(
        service_name="bedrock-runtime",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
