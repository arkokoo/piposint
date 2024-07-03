from app.services.domain import hunter
from app.utils.regex import is_domain
from app.utils.History import History
from app.utils.vars import HUNTER_API_KEY
from flask import Blueprint, abort, request, jsonify

domain = Blueprint('domain', __name__)

@domain.route('/api/domain',methods=['GET'])
def get_domain() :
    """
    Retourne les informations d'un domaine.
    ---
    tags:
      - Services
    parameters:
      - name: value
        in: query
        type: string
        required: true
        description: Domaine à rechercher
    definitions:
      Domain:
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
    responses:
      200:
        description: Informations du domaine
        schema:
          $ref: '#/definitions/Domain'
      400:
        description: Bad Request, please ensure all parameters are provided
      500:
        description: Internal Server Error
    """

    domain = request.args.get('value')
    domain_dict = {
        "type": "domain",
        "args": [domain],
        "data": {}
    }

    if domain == None or is_domain(domain) is False or HUNTER_API_KEY == None or HUNTER_API_KEY == "":
        abort(400)

    domain_dict["data"] = hunter(str(domain))
    history = History()
    history.add_element(param_dict=domain_dict)
    return jsonify(domain_dict)

@domain.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@domain.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500