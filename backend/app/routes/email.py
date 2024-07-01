from app.services.email import get_holehe
from app.utils.regex import is_email
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify

email = Blueprint('email', __name__)

@email.route('/api/email', methods=['GET'])
def get_email():
    """
    Retourne les informations d'une adresse email.
    ---
    tags:
      - Services
    parameters:
      - name: value
        in: query
        type: string
        required: true
        description: Email à rechercher
    definitions:
      Email:
        type: object
        properties:
          type:
            type: string
          args:
            type: array
            items:
              type: string
          data:
            type: object
            properties:
              associated_domains:
                type: array
                items:
                  type: string
    responses:
      200:
        description: Informations de l'email
        schema:
          $ref: '#/definitions/Email'
      400:
        description: Bad Request, please ensure all parameters are provided
      500:
        description: Internal Server Error
    """

    email = request.args.get('value')

    if email == None or is_email(email) is False:
        abort(400)
    
    email_dict = {
        "type": "email",
        "args" : [email],
        "data" : {
            "associated_domains": []
        } 
    }

    email_dict["data"]["associated_domains"] = get_holehe(email)

    history = History()
    history.add_element(param_dict=email_dict)

    return jsonify(email_dict)

@email.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@email.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500