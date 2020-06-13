# AlexaSkill-AssistantPC
AssistantPC is an alexa skill that let you control your pc using voice commands

## e.g.
##### IN: "Turn off computer"   -->  OUT: "OK, shutting down computer"
##### IN: "Search on Netflix for 'The Interview'" --> OUT: "OK, looking for 'The Interview'

## HOW IT WORKS
A Server is running on the host machine:
- Starting the server
- Tunneling using Ngrok
- Writing ngrok_url on AWS DynamoDB
- Listening for new request

Alexa Skill:
- Listening for input voice commands
- Reading ngrok_url on AWS DynamoDB with IAM role credentials
- Making POST request

## SETUP

AlexaSkill:
- Create a new Alexa Skill using files in "AlexaSkill" folder

Server:
- Create a new AWS DynamoDB
- Create a new IAM Role and give access to your Alexa Skill
- Go to Server/helpers folder
- Create a new python file "credential" and insert your 'AWS DynamoDB keys' and, optionally, your 'Netflix credentials'
- Download "driver" for selenium and change paths in "helpers/BrowseDriver.py"
- ``` bash
	$ cd Server/
	$ python -m venv venv
	$ source venv/bin/activate/
	$ pip install -r requirements.txt
	$ python main.py
	```
