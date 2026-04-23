# MTG trading and deck builder
This application uses a FLASK framework with SQL to create tables that will store customer information and various other seller / buyer based functions that you might find in other e-commerce applications 

### Simple project summary
An application that will allow MTG (Magic the Gathering) enjoyers to search for cards they want to purchase for their builds, these cards would be coming from what other players are selling. If there is not a set in stone price, sellers have the optionn to start bids for their cards. Users will also be able to display deck builds that other players can view.

### Running flask for this project

First you will need to clone this repo
```
git clone https://github.com/abatista15/Project-EandK.git
```
Setup a venv to install flask using bash
```
python -m venv **NAME_OF_ENVIRONMENT**
```
Activate the venv
```
**NAME_OF_ENVIRONMENT**\Scripts\activate
```
Download requirements.txt
```
pip install -r requirements.txt
```
### Creating a PostgresSQL DB and running Flask in Python

Locate your PostgreSQL bin file path 
```
cd "C:\Program Files\PostgreSQL\18\bin"
```
Login to PostgreSQL via the terminal 
```
psql -U postgres
```
You will be prompted to type in your password but it will not show you what you are typing 

Create the DB locally
```
CREATE DATABASE flask_db;
CREATE USER username WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE flask_db TO username;
```
Make an .env file to hide your credentials
```
DATABASE_URL = postgresql://username:password@localhost/flask_db
```
After you setup your database, run the app in the root directory
```
flask --app server.app run
```
OR run the app by going into the server directory and running it there
```
cd server
flask run
```
At [http://localhost:5000/test-db](http://localhost:5000/test-db), the database will show you if the connection is successful or not.