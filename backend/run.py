from flask import Flask
from app.routes.person import person
from app.routes.email import email
from app.routes.phone import phone
from app.routes.username import username

def create_app():
    app = Flask(__name__)
    app.register_blueprint(person)
    app.register_blueprint(email)
    app.register_blueprint(phone)
    app.register_blueprint(username)
    return app

app = create_app()

if __name__ == "__main__":
    # Démarrer le backend avec "python run.py
    app.run(debug=True, host="127.0.0.1")