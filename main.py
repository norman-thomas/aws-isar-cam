import boto3
import requests
from io import BytesIO
import datetime

S3_BUCKET = 'isar-webcam'
IMAGE_URL = 'http://www.webcammuenchen.com/Prolog-PR.com---cam3.jpg'

def lambda_handler(event, context):
    page = requests.get(IMAGE_URL)
    image = page.content

    now = datetime.datetime.utcnow()
    filename = '{}/isar-{}.jpg'.format(now.date().isoformat(), now.isoformat())

    s3 = boto3.client('s3')
    with BytesIO(image) as f:
        s3.upload_fileobj(f, S3_BUCKET, filename)

    return 'stored ' + filename
