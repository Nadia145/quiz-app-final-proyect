# quiz-app-final-proyect

Design and implementation of a quiz application, using a microservice architecture and various AWS services.

###########################################################################################
---------------------------GENERAL OVERVIEW-----------------------

---

The project “quiz-app-final-proyect” is a quiz application that provides an interactive quiz. The project utilices a full-stack approach, using React on the frontend and Python on the backend. The main purpose of the application is to allow users to test their knowledge about design patterns, anti patterns, refactoring and UML.
The backend handles the storage of quiz questions, user information and ranking data. The frontend serves as the intermediary between the user and the system, facilitating communication and interaction.

At the moment of playing the quiz you will find that questions are categorized into three difficulties: hard, medium and easy. The application tracks the user's progress and provides immediate feedback. At the end of the quiz, the user is shown their final score, and rank based on the global ranking, so the ranking system allows the user to compare their score with other participants.

---

###########################################################################################

La arquitectura utilizada en el código es cliente-servidor basada en servicios en la nube. El código se conecta a DynamoDB, que es un servicio de base de datos administrada proporcionado por Amazon Web Services (AWS). Utiliza la biblioteca `boto3` de AWS para interactuar con DynamoDB y realizar operaciones como crear una tabla y cargar datos en ella. La arquitectura general implica el uso de una aplicación cliente (este código) que se comunica con el servicio DynamoDB a través de la biblioteca `boto3` para realizar operaciones en la base de datos.

Las credenciales utilizadas en el codigo fueron configuradas en el AWS cli

###########################################################################################

InsertQuestions.py:
#The estructure of the definitions of thatas its next:

# id: define the unique tiket

# question: Its the string that the user will answer

# dificulty: Its how hardly is the question

# feedback: Its the array that determinate if the user answer is correct

InsertUsers.py
#The estructure of the definitions of thatas its next:

# id: define the unique tiket

# username: Is the nickname that the user use to solve the quiz

# score: Is the points that the user obteined

# dificultad: Is how hardly the quiz was

###########################################################################################

Controllers.py

## A little explication about any controller.

---

/single (GET): This controller calls the RetrieveData.RetrieveUsers() function to fetch the users and returns the score of the first user as a string.

/test (GET): This controller simply returns a greeting message from the backend in JSON format.

/easyqs (GET): This controller calls the RetrieveData.RetrieveQuestions() function to fetch all the questions and then filters the questions with "easy" difficulty. It returns a list of questions and feedback, limited according to the optional "limit" parameter provided in the request.

/mediumqs (GET): Similar to the previous controller, but it filters the questions with "medium" difficulty.

/hardqs (GET): Similar to the previous controller, but it filters the questions with "difficult" difficulty.

/10Hard (GET): This controller retrieves all the users and filters out those whose difficulty is neither "easy" nor "medium". The users are then sorted based on their score in descending order, and a list of the top 10 users is returned.

/10Medium (GET): Similar to the previous controller, but it filters the users whose difficulty is neither "easy" nor "hard".

/10Easy (GET): Similar to the previous controller, but it filters the users whose difficulty is neither "hard" nor "medium".

/AddUser (POST): This controller receives data in JSON format through a POST request and adds them to a "Users" table in DynamoDB using the boto3 library.
