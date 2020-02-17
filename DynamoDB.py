import boto3
from credentials import *

def write_url(url):
    session = boto3.Session(
        aws_access_key_id=AWS_SERVER_PUBLIC_KEY,
        aws_secret_access_key=AWS_SERVER_SECRET_KEY,
        region_name=REGION_NAME
    )
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('AssistantPC-AlexaSkill')
    table.put_item(
               Item={
                   'pub_url': "0",
                   "url": url
                }
            )
    del session
