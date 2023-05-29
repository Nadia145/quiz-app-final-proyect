import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the table name
table_name = 'Users'

# Define the partition key attribute
partition_key = {
    'AttributeName': '_id',
    'KeyType': 'HASH'  # HASH type indicates the partition key
}

# Define the attribute definitions
attribute_definitions = [
    {
        'AttributeName': '_id',
        'AttributeType': 'S'  # S type indicates a string attribute
    }
]

# Define the table schema
table_schema = {
    'TableName': table_name,
    'KeySchema': [partition_key],
    'AttributeDefinitions': attribute_definitions,
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,   # Adjust the values as per your requirements
        'WriteCapacityUnits': 5   # Adjust the values as per your requirements
    }
}

# Create the DynamoDB table
response = dynamodb.create_table(**table_schema)

# Check the response
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print('Table created successfully!')
else:
    print('Error creating table:', response['ResponseMetadata']['HTTPStatusCode'])