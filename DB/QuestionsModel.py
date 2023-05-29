import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table schema
table_name = 'Questions'
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': '_id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': '_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'question',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'question-index',
            'KeySchema': [
                {
                    'AttributeName': 'question',
                    'KeyType': 'HASH'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    ]
)

# Wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

# Print the table details
print("Table created successfully!")
print(f"Table Name: {table.table_name}")
print(f"Table ARN: {table.table_arn}")
print(f"Table Status: {table.table_status}")