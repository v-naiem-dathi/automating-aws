import boto3

session = boto3.Session(profile_name='acg-course')

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('Movies')

table.delete()
