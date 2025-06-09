import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name = os.getenv("AWS_REGION")
)

BUCKET = os.getenv("S3_BUCKET_NAME")

def uploadPdfToS3(local_path: str , s3_key: str):
    s3.upload_file(local_path, BUCKET, s3_key)
    return f"https://{BUCKET}.s3.amazonaws.com/{s3_key}"

def downloadPdfFromS3(s3_key: str, local_path: str):
    s3.download_file(BUCKET, s3_key, local_path)