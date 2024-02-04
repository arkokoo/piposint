from flask import Flask
from app.routes.person import person
from app.routes.email import email

def create_app():
    app = Flask(__name__)
    app.register_blueprint(person)
    app.register_blueprint(email)
    return app