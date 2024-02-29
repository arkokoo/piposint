from flask import Flask
from pymongo import MongoClient
from app.routes.person import person
from app.routes.email import email
from app.routes.phone import phone
from app.routes.username import username
from app.routes.ip import ip
from app.routes.domain import domain
from app.utils.vars import *

def create_app():
    app = Flask(__name__)
    app.register_blueprint(person)
    app.register_blueprint(email)
    app.register_blueprint(phone)
    app.register_blueprint(username)
    app.register_blueprint(ip)
    app.register_blueprint(domain)
    return app

def get_database():
    client = MongoClient(f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@localhost:27017/")
    db = client[DB_NAME]
    return db

app = create_app()
db = get_database()
history_collection = db["history"]

if __name__ == "__main__":
    # Dev : Démarrer le backend avec "python run.py"
    # Prod : Démarrer le backend avec "gunicorn -w 4 -b 0.0.0.0:5000 run:app"
    app.run(debug=True, host="0.0.0.0")