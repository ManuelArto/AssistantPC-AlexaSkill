import boto3

def get_url():
    # 1. Assume the AWS resource role using STS AssumeRole Action
    sts_client = boto3.client('sts')
    assumed_role_object=sts_client.assume_role(RoleArn="arn:aws:iam::750711143750:role/AssistancPCRole",
                                              RoleSessionName="AssistancPCRole")
    credentials=assumed_role_object['Credentials']
    
    # 2. Make a new DynamoDB instance with the assumed role credentials
    dynamodb = boto3.resource('dynamodb',
                      aws_access_key_id=credentials['AccessKeyId'],
                      aws_secret_access_key=credentials['SecretAccessKey'],
                      aws_session_token=credentials['SessionToken'],
                      region_name='us-east-1')

    table = dynamodb.Table('AssistantPC-AlexaSkill')
    response = table.scan()
    return response["Items"][0]["url"]