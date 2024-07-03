from app.routes.person import person
from app.routes.email import email
from app.routes.phone import phone
from app.routes.username import username
from app.routes.ip import ip
from app.routes.domain import domain
from app.routes.history import history
from app.routes.swagger import swagger
from app.utils.vars import *
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
import yaml

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(person)
    app.register_blueprint(email)
    app.register_blueprint(phone)
    app.register_blueprint(username)
    app.register_blueprint(ip)
    app.register_blueprint(domain)
    app.register_blueprint(history)
    app.register_blueprint(swagger)
    return app

with open('swagger_template.yml', 'r', encoding='utf-8') as file:
    template = yaml.safe_load(file)

app = create_app()
swag = Swagger(app, template=template)

if __name__ == "__main__":
    # Dev : Démarrer le backend avec "python run.py"
    # Prod : Démarrer le backend avec "gunicorn -w 4 -b 0.0.0.0:5000 run:app"
    app.run(debug=True, host="0.0.0.0")