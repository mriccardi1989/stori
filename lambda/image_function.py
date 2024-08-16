import requests
from image_processor import reduce_size


OUTPUT_BUCKET = "output_images_bucket"


def handler(event, context):
    input_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    input_file_path = event["Records"][0]["s3"]["object"]["key"]

    reduce_size(
        input_bucket=input_bucket,
        input_file_path=input_file_path,
        output_bucket=OUTPUT_BUCKET,
    )

    return {"statusCode": 200}
