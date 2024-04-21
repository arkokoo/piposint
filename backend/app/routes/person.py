from app.services.person import get_person_info
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify

person = Blueprint('person', __name__)

@person.route('/api/person', methods=['GET'])
def get_person():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')

    if firstname == None or lastname == None:
        abort(400)
    
    person_dict = {
        "firstname": firstname,
        "lastname": lastname,
        "gender": None,
        "country": None
    }

    person_dict["gender"], person_dict["country"] = get_person_info(firstname, lastname)
    history = History()
    history.add_element(param_data=person_dict, param_type="person", param_args=[firstname, lastname])
    return jsonify(person_dict)

@person.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@person.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error"}), 500
