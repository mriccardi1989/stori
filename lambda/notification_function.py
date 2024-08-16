import requests


def handler(event, context):
    """
    Placeholder function to notify front end app where the resized file was stored so the user can download the file
    """

    input_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    input_file_path = event["Records"][0]["s3"]["object"]["key"]

    url = "placeholder_url"
    data = f"{input_bucket}/{input_file_path}"

    requests.post(url=url, data=data)

    return {"statusCode": 200}
