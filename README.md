# Masteming_GAME

This is the repository to play the Mastermind game. The game consists in a pattern of 4 random digitis and the player (codebreaker) needs to guess the pattern, in both digits and order, within 10 moves. Each move the codebreaker inputs his guess and gets the feedback, returning '1' for each correct digit in the correct location and '0' for each correct digit in the wrong location.

In its current form, the code is meant to be executed in Python 3, it's necessary to have the python libraries within the code and the MongoDB installed. 

*Don't have MongoDB?* check https://docs.mongodb.com/manual/installation/ .

	List of libraries in use:
		- flask
		- flask_wtf
		- pymongo
		- logging
		- wtforms 
		- random
		- threading

# Ready to play?

In order to start the game, clone all the files within this repo or downloand the current master and unzip it in the directory of your choice.

Next, you need to start your mongo.

	sudo systemctl start mongod

In my case, I'm using Ubuntu 18.04. For other OS, check the mongodb manual above.

Run the API.py file, it will return a url for the localhost where the game will be running. Click on it or copy to the browser of your choice and start playing. 


# Files:

**API.py**

With flask, the script displays the templates for each page in your browser and generate .log outputs.

@app.route("/") - it's the home page created with home.html and layout.html

@app.route("/Start") - It is the registration page created with Start.html and layout.html. In it is possible to create new accounts by calling:
	The RegistrationForms from Forms.py 
	The Start function from mastermind class in Functions.py


@app.route("/Play") - It is the Play page created with Play.html and layout.html. In it the player can input the username, email and the new guess and gets the feedback after each guess. And it calls:
	The AttemptForm from Forms.py
	The find and Tentativa methods from Functions.py

@app.route("/GameRecord") -  It is created with the GameRecord.html and layout.html. This page displays some infos about all the players and their game status by calling:
	The record function from Functions.py


**Functions.py**

In the mastermind class:
	- 'Create_number' function returns a new four digit pattern. 
	- 'Start' function gets the username and the email inputed by the player, calls the
	  'Create_number' function and save all the infos in the MongoDB database.
	- 'Tentativa' receives the username, email and the new guess as parameters. Gets the info of 
	  the player from the MongoDB, checks the result, update the database and returns the feedback.
	- 'record' return all the infos from the database, it will be use in the GameRecord page.
	- 'find' returns the info from a specific player, using the username and password.


**Forms.py**

Consists in two classes:
	RegistrationForms: Requires the username, email from the player.
	AttemptForms: Requires the username, email and the new guess from the player.


**MongoDB.py**

In the DB class:
	- 'start_conn' starts the connection with the database 
	- 'insertion_mongo' inserts a new sample in the collection, both passed as arguments
	- 'find_mongo' finds the user in the collection, according to the name and email passed as arguments
	- 'findall' returns all the info from the database
	- 'update' update the info from a specific user	


The 'templates' folder contains all the .html code used in this application. 
