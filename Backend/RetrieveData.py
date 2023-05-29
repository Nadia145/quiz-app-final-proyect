# Final Project: Quiz Application with Microservices
# Date: 29-May-2023
# Authors:
#          A01752030 Juan Pablo Castañeda Serrano
#          A0752221 Omar Rodrigo Talavera Becerra
#          A01752013 Nadia Paola Ferro Gallegos

import boto3
import json

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')


def RetrieveUsers():
    """Retrieves the users from the 'Users' table."""

    # Specify the table name
    table_name = 'Users'

    # Retrieve the table
    table = dynamodb.Table(table_name)

    # Perform the scan operation to retrieve all items
    response = table.scan()

    # Access the items retrieved
    items = response['Items']

    return (items)


def RetrieveQuestions():
    """Retrieves the questions from the 'Questions' table."""

    # Specify the table name
    table_name = 'Questions'

    # Retrieve the table
    table = dynamodb.Table(table_name)

    # Perform the scan operation to retrieve all items
    response = table.scan()

    # Access the items retrieved
    items = response['Items']

    readable = [json.loads(item['data']) for item in items]

    return (readable)


if __name__ == '__main__':
    Full = RetrieveQuestions()
    limit = 8
    Qs = []

    print(Full[8])

    for i in range(len(Full)):
        if Full[i]['difficulty'] == 'difficult':
            Qs.append(Full[i]['question'])

    # Qs = [question['question'] for question in Full[:limit] if question['difficulty'] == 'difficult']
    # FB = [question['feedback'] for question in Full[:limit] if question['difficulty'] == 'difficult']

    print(Qs)
