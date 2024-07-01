from flask import Blueprint, redirect

swagger = Blueprint('swagger', __name__)

# Rediriger /api/ vers la documentation Swagger
@swagger.route('/api', methods=['GET'])
@swagger.route('/api/', methods=['GET'])
def api_docs():
    return redirect('/apidocs/')