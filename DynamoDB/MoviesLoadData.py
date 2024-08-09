import decimal
import json

import boto3

session = boto3.Session(profile_name='acg-course')

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float=decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': info,
            }
        )
