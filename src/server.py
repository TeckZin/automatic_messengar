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


    s3 = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )

    # --- List all buckets ---
    print("Buckets:")
    for bucket in s3.list_buckets()["Buckets"]:
        print(f" - {bucket['Name']}")

    # --- List objects in a specific bucket ---
    bucket_name = "sgi-members"
    print(f"\nObjects in {bucket_name}:")
    objects = s3.list_objects_v2(Bucket=bucket_name)




