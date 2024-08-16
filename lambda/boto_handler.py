import boto3
from io import BytesIO


def get_s3_resource():
    return boto3.resource("s3")


def get_s3_client():
    return boto3.client("s3")


def read_file(bucket: str, file_path: str):
    s3_resource = get_s3_resource()
    bucket = s3_resource.Bucket(bucket)
    object = bucket.Object(file_path)
    response = object.get()
    return response["Body"]


def write_file(bucket: str, file_path: str, file_obj: BytesIO):
    s3_client = get_s3_client()
    s3_client.upload_fileobj(Bukect=bucket, Fileobj=file_obj, Key=file_path)
