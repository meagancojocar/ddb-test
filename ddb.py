import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Test-123')

# table.put_item(
#    Item={
#         'Username': 'janedoe',
#         'Timestamp': 1606609864
#     }
# )

response = table.get_item(
    Key={
        'Username': 'janedoe',
        'Timestamp': 1606609864
    }
)
item = response['Item']
print(item)
print(response)