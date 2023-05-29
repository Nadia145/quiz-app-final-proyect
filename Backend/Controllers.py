# Final Project: Quiz Application with Microservices
# Date: 29-May-2023
# Authors:
#          A01752030 Juan Pablo Castañeda Serrano
#          A0752221 Omar Rodrigo Talavera Becerra
#          A01752013 Nadia Paola Ferro Gallegos

from flask import Flask, request, jsonify
import RetrieveData
import boto3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/single', methods=['GET'])
def GetASingleThing():
    """Retrieves a single item."""
    thing = RetrieveData.RetrieveUsers()
    return (str(thing[0]["score"]))


@app.route('/test', methods=['GET'])
def api_endpoint():
    """Test endpoint to chcek the connection with the backend."""
    # Handle the request and return a response
    data = {'message': 'Hello from the backend!'}
    return jsonify(data)


@app.route('/easyqs', methods=['GET'])
def GetEasyQuestions():
    """Retrieves de easy questions."""
    Full = RetrieveData.RetrieveQuestions()
    limit = int(request.args.get('limit', default=12))

    Qs = [question['question'] for question in Full if question['difficulty'] == 'easy']
    FB = [question['feedback'] for question in Full if question['difficulty'] == 'easy']

    return [Qs[:limit], FB[:limit]]


@app.route('/mediumqs', methods=['GET'])
def GetMediumQuestions():
    """Retrieves de medium questions."""
    Full = RetrieveData.RetrieveQuestions()
    limit = int(request.args.get('limit', default=12))

    Qs = [question['question'] for question in Full if question['difficulty'] == 'medium']
    FB = [question['feedback'] for question in Full if question['difficulty'] == 'medium']

    return [Qs[:limit], FB[:limit]]


@app.route('/hardqs', methods=['GET'])
def GetHardQuestions():
    """Restrieves the hard questions."""
    Full = RetrieveData.RetrieveQuestions()
    limit = int(request.args.get('limit', default=12))

    Qs = [question['question'] for question in Full if question['difficulty'] == 'difficult']
    FB = [question['feedback'] for question in Full if question['difficulty'] == 'difficult']

    return [Qs[:limit], FB[:limit]]


@app.route('/10Hard', methods=['GET'])
def GetTop10PlayersHard():
    """Retrieves the top 10 players in the hard category."""
    users = RetrieveData.RetrieveUsers()
    HardUsers = [item for item in users if 'dificultad' in item and item['dificultad'] not in ['easy', 'medium']]
    SortedUsers = sorted(HardUsers, key=lambda x: x['score'], reverse=True)

    return SortedUsers


@app.route('/10Medium', methods=['GET'])
def GetTop10PlayersMedium():
    """Retrieves the top 10 players in the medium category."""
    users = RetrieveData.RetrieveUsers()
    HardUsers = [item for item in users if 'dificultad' in item and item['dificultad'] not in ['easy', 'hard']]
    SortedUsers = sorted(HardUsers, key=lambda x: x['score'], reverse=True)

    return SortedUsers


@app.route('/10Easy', methods=['GET'])
def GetTop10PlayersEasy():
    """Retrieves the top 10 players in the easy category."""
    users = RetrieveData.RetrieveUsers()
    HardUsers = [item for item in users if 'dificultad' in item and item['dificultad'] not in ['hard', 'medium']]

    SortedUsers = sorted(HardUsers, key=lambda x: x['score'], reverse=True)

    return SortedUsers


@app.route('/AddUser', methods=['POST'])
def add_data():
    """Adds user data to the database."""
    data = request.get_json()
    dynamodb = boto3.resource('dynamodb')
    table_name = 'Users'
    table = dynamodb.Table(table_name)
    table.put_item(Item=data)
    return 'Data added successfully'


if __name__ == '__main__':
    app.run(debug=True)
