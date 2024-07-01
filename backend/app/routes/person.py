from app.services.person import get_person_info
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify

person = Blueprint('person', __name__)

@person.route('/api/person', methods=['GET'])
def get_person():
    """
    Retourne les informations d'une personne à partir de son prénom et son nom de famille.
    ---
    tags:
      - Services
    parameters:
      - name: firstname
        in: query
        type: string
        required: true
        description: Prénom de la personne
      - name: lastname
        in: query
        type: string
        required: true
        description: Nom de famille de la personne
    definitions:
      Person:
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
              gender:
                type: object
              country:
                type: object
    responses:
      200:
        description: Informations de la personne
        schema:
          $ref: '#/definitions/Person'
      400:
        description: Bad Request, please ensure all parameters are provided
      500:
        description: Internal Server Error
    """


    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')

    if firstname == None or lastname == None:
        abort(400)
    
    person_dict = {
        "type": "person",
        "args" : [firstname, lastname],
        "data" : {
            "gender": None,
            "country": None
        }
    }

    person_dict["data"]["gender"], person_dict["data"]["country"] = get_person_info(firstname, lastname)
    history = History()
    history.add_element(param_dict=person_dict)
    return jsonify(person_dict)

@person.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@person.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error"}), 500
