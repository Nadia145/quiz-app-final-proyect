import boto3
import json
import uuid

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the table name
table_name = 'Questions'

# Define the JSON data
json_data = [{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern is used to create an instance of several families of classes?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Abstract Factory",
    "incorrect_answer": [
      "Builder",
      "Prototype",
      "Singleton"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern separates an object's interface from its implementation?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Bridge",
    "incorrect_answer": [
      "Adapter",
      "Facade",
      "Proxy"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern is used to sequentially access the elements of a collection?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Iterator",
    "incorrect_answer": [
      "Command",
      "Mediator",
      "Observer"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is an AntiPattern?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "A literary form that describes a commonly occurring solution to a problem with negative consequences.",
    "incorrect_answer": [
      "A solution to a problem with positive consequences.",
      "A vocabulary used by software practitioners.",
      "A process of code modification."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What do AntiPatterns highlight?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "The most common problems in the software industry.",
    "incorrect_answer": [
      "The best practices in software development.",
      "The benefits of using design patterns.",
      "The tools for optimizing code performance."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is the purpose of software refactoring?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "To improve the software structure and support long-term maintenance.",
    "incorrect_answer": [
      "To introduce new features into the software.",
      "To fix bugs in the code.",
      "To optimize the performance of the software."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which code smell refers to code, methods, and classes that have become excessively large and difficult to work with?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Long Method",
    "incorrect_answer": [
      "Lazy Class",
      "Duplicate Code",
      "Feature Envy"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which code smell occurs when a class is obsessed with using primitive data types instead of creating dedicated classes for the data?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Primitive Obsession",
    "incorrect_answer": [
      "Incomplete Library Class",
      "Duplicate Code",
      "Extract Method"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which code smell refers to a situation where a method has a long list of parameters?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Long Parameter List",
    "incorrect_answer": [
      "Message Chains",
      "Replace Temp with Query",
      "Extract Class"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What does UML stand for?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Unified Modeling Language",
    "incorrect_answer": [
      "Universal Modeling Language",
      "Unique Modeling Language",
      "Ultimate Modeling Language"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is the main purpose of UML?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "To model business systems and software",
    "incorrect_answer": [
      "To develop software more quickly",
      "To facilitate communication between development teams",
      "To establish standards for object-oriented programming"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which of the following options best describes a use case diagram?",
  "difficulty": "easy",
  "feedback": {
    "correct_answer": "Describes the functionalities and behaviors of the system from the user's perspective",
    "incorrect_answer": [
      "Represents the interaction between objects in a system",
      "Shows the static structure of a system and its classes",
      "Illustrates the sequence of interactions between objects in a specific scenario"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern can be used to add responsibilities to objects dynamically?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Decorator",
    "incorrect_answer": [
      "Flyweight",
      "Proxy",
      "Visitor"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern encapsulates a command request as an object?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Command",
    "incorrect_answer": [
      "Chain of responsibility",
      "Interpreter",
      "Strategy"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern defines simplified communication between classes?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Mediator",
    "incorrect_answer": [
      "Memento",
      "Observer",
      "State"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is the main focus of Architecture AntiPatterns?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Analyzing system-level and enterprise-level structure of applications.",
    "incorrect_answer": [
      "Improving software structure.",
      "Enhancing communication between software practitioners.",
      "Addressing people issues in software development."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is the consequence of an Autogenerated Stovepipe AntiPattern?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Problems arising from converting existing software interfaces to distributed interfaces.",
    "incorrect_answer": [
      "Limited reusability and robustness of the architecture.",
      "Excessive complexity in class interfaces.",
      "Lack of coordination and planning across a set of systems."
    ]
  }
},{
  "_id":str(uuid.uuid4()),
  "question": "What is a common issue addressed by Project Management AntiPatterns?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Inattention to the management of software development processes.",
    "incorrect_answer": [
      "Striving for perfection and completeness in the analysis phase.",
      "Excessive planning leading to complex schedules.",
      "Personality conflicts between managers affecting the work environment."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which code smell refers to the excessive use of switch statements instead of utilizing polymorphism?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Switch Statements",
    "incorrect_answer": [
      "Extract Method",
      "Extract Class",
      "Replace Type Code with Class"
    ]
  }
},{
  "_id":str(uuid.uuid4()),
  "question": "Which code smell occurs when a class receives or holds a temporary field that is not used consistently?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Temporary Field",
    "incorrect_answer": [
      "Inappropriate Intimacy",
      "Replace Parameter with Method Call",
      "Replace Exception with Test"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which code smell occurs when a class inherits methods or properties that it doesn't actually need or use?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Refused Bequest",
    "incorrect_answer": [
      "Move Method",
      "Remove Middle Man",
      "Encapsulate Field"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which of the following is NOT a type of diagram in UML?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "Data flow diagram",
    "incorrect_answer": [
      "Sequence diagram",
      "Activity diagram",
      "Component diagram"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What does a class diagram represent in UML?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "The static structure of a system and its classes",
    "incorrect_answer": [
      "The sequence of interactions between objects in a specific scenario",
      "The physical distribution of components in a system",
      "The control flows and decisions in a business process"
    ]
  }
},{
  "_id":str(uuid.uuid4()),
  "question": "What is the main purpose of a sequence diagram in UML?",
  "difficulty": "medium",
  "feedback": {
    "correct_answer": "To show the interaction between objects in a system over time",
    "incorrect_answer": [
      "To represent the static structure of a system and its classes",
      "To illustrate the relationships between components in a system",
      "To describe the control flows and decisions in a business process"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern captures and restores an object's internal state?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Memento",
    "incorrect_answer": [
      "Chain of responsibility",
      "Null Object",
      "Visitor"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern alters an object's behavior when its state changes?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "State",
    "incorrect_answer": [
      "Interpreter",
      "Memento",
      "Observer"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which design pattern defines a new operation to a class without change?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Visitor",
    "incorrect_answer": [
      "Iterator",
      "Command",
      "Strategy"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is the solution to the Swiss Army Knife AntiPattern?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Simplifying the class interface to focus on specific functionality.",
    "incorrect_answer": [
      "Adding more interface signatures to meet all possible needs.",
      "Refactoring the design to distribute responsibilities more uniformly.",
      "Providing independence from vendor-specific solutions."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is the consequence of the Fear of Success AntiPattern?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Overemphasis on concerns about potential failures.",
    "incorrect_answer": [
      "Excessive planning for software projects.",
      "Chronic development crises due to bad management habits.",
      "De facto decisions and lack of resolution in project management."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is the purpose of the Blowhard Jamboree AntiPattern?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Dealing with controversial reports influencing technology decisions.",
    "incorrect_answer": [
      "Addressing difficult people obstructing the software development process.",
      "Overcoming excessive planning and project gridlock.",
      "Reducing indecisiveness and irrational management habits."
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which code smell refers to the situation where making a change in one place requires multiple changes in other parts of the code?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Shotgun Surgery",
    "incorrect_answer": [
      "Divergent Change",
      "Remove Parameter",
      "Inline Method"
    ]
  }
},{
  "_id":str(uuid.uuid4()),
  "question": "Which code smell occurs when there are unnecessary comments in the code that don't provide any additional information?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Comments",
    "incorrect_answer": [
      "Consolidate Conditional Expression",
      "Change Value to Reference",
      "Duplicate Code"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which code smell refers to the excessive coupling between classes, resulting in high interdependence and low maintainability?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Inappropriate Intimacy",
    "incorrect_answer": [
      "Feature Envy",
      "Incomplete Library Class",
      "Replace Type Code with State/Strategy"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "What is a deployment diagram in UML?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "A diagram that represents the physical distribution of components in a system",
    "incorrect_answer": [
      "A diagram that shows the static structure of a system and its classes",
      "A diagram that describes the functionalities and behaviors of the system from the user's perspective",
      "A diagram that shows the sequence of interactions between objects in a specific scenario"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "Which of the following options best describes a state diagram in UML?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "Describes the different states and transitions of an object or system",
    "incorrect_answer": [
      "Represents the interaction between objects in a system over time",
      "Shows the static structure of a system and its classes",
      "Illustrates the sequence of interactions between objects in a specific scenario"
    ]
  }
},{
  "_id": str(uuid.uuid4()),
  "question": "In UML, what is the purpose of a collaboration diagram?",
  "difficulty": "difficult",
  "feedback": {
    "correct_answer": "To describe the collaboration between objects and their messages",
    "incorrect_answer": [
      "To show the interaction between objects in a system over time",
      "To represent the static structure of a system and its classes",
      "To illustrate the relationships between components in a system"
    ]
  }
}]

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
            'data': {'S': json.dumps(item)}
        }
    )

    # Check the response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('Item inserted successfully!')
    else:
        print('Error inserting item:', response['ResponseMetadata']['HTTPStatusCode'])