import boto3
import json
import uuid

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the table name
table_name = 'Users'

# Define the JSON data
json_data = [
    {
        "_id": str(uuid.uuid4()),
        "username": "nad14517",
        "score": 7,
        "dificultad": "easy"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "lexxx85",
        "score": 2,
        "dificultad": "medium"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "mamamaaay159",
        "score": 10,
        "dificultad": "hard"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "aleleny753",
        "score": 4,
        "dificultad": "hard"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "valentina438",
        "score": 10,
        "dificultad": "medium"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "humberto864",
        "score": 3,
        "dificultad": "easy"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "dani468",
        "score": 8,
        "dificultad": "hard"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "Pablongo154",
        "score": 10,
        "dificultad": "easy"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "papic879",
        "score": 9,
        "dificultad": "medium"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "bu201",
        "score": 5,
        "dificultad": "medium"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "frrr603",
        "score": 2,
        "dificultad": "hard"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "p-p748",
        "score": 7,
        "dificultad": "easy"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "motojorge550",
        "score": 3,
        "dificultad": "easy"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "mel766",
        "score": 10,
        "dificultad": "medium"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "yari959",
        "score": 1,
        "dificultad": "hard"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "economialalo740",
        "score": 6,
        "dificultad": "hard"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "leyva001",
        "score": 10,
        "dificultad": "easy"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "lore966",
        "score": 9,
        "dificultad": "medium"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "abril598",
        "score": 4,
        "dificultad": "medium"
    },
    {
        "_id": str(uuid.uuid4()),
        "username": "mikaela999",
        "score": 10,
        "dificultad": "hard"
    }
]

json_str = json.dumps(json_data)
print(json_str)
for item in json_data:
    # Convert the dictionary to a string
    json_string = json.dumps(item)

    # Insert the item into DynamoDB
    response = dynamodb.put_item(
        TableName=table_name,
    Item={
        '_id': {'S': item['_id']},
        "username": {'S': item['username']},
        "score": {'N': str(item['score'])},  # Convert score to string and specify the data type as 'N'
        "dificultad": {'S': item['dificultad']}  # Specify the data type as 'S'
    }
    )

    # Check the response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('Item inserted successfully!')
    else:
        print('Error inserting item:', response['ResponseMetadata']['HTTPStatusCode'])