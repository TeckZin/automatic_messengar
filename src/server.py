import os
from dotenv import load_dotenv
import boto3

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_DEFAULT_REGION")


if __name__ == "__main__" :

    print("Start server")
    print(aws_region)



