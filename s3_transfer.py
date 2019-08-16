import boto3

s3 = boto3.client('s3')
s3.upload_file('demo.txt', 'mres3btemp', 'S3_script.txt')


s3 = boto3.client('s3')
response = s3.list_buckets()
for file in response['Buckets']:
    print(file)

s3.create_bucket(Bucket = 'mrepybucket')

#Dynamodb
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#define a schema for table
table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
#table status
print("Table status:", table.table_status)


#LOAD movie fromjson and copy

import json
import decimal

table = dynamodb.Table('Movies')

with open('moviedata.json') as json_file:
    movies = json.load(json_file,parse_float=decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']
        print('putting item to dynamodb')
        table.put_item(
            Item = {
                'year':year,
                'title':title,
                'info':info,
            }
        )






