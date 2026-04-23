from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test-db")
def db_test():
    try:
        with db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return "<p>Database connection successful</p>"
    except Exception as e:
        return f"<p>Database connection failed: {str(e)}</p>"


@app.route("/Users", methods=["GET"])
def get_Users():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Users;"))
        return [dict(row._mapping) for row in result]


@app.route("/User_deck", methods=["GET"])
def get_User_deck():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM User_deck;"))
        return [dict(row._mapping) for row in result]


@app.route("/Deck", methods=["GET"])
def get_Deck():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Deck;"))
        return [dict(row._mapping) for row in result]


@app.route("/Cards", methods=["GET"])
def get_Cards():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Cards;"))
        return [dict(row._mapping) for row in result]


@app.route("/Deck_Cards", methods=["GET"])
def get_Deck_Cards():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Deck_Cards;"))
        return [dict(row._mapping) for row in result]


@app.route("/Bidding_Session", methods=["GET"])
def get_Bidding_Session():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Bidding_Session;"))
        return [dict(row._mapping) for row in result]

@app.route("/Transactions", methods=["GET"])
def get_Transactions():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Transactions;"))
        return [dict(row._mapping) for row in result]

if __name__ == "__main__":
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    
    app.run(debug=True)