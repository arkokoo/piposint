from app.services.domain import hunter
from app.utils.regex import is_domain
from app.utils.History import History
from app.utils.vars import HUNTER_API_KEY
from flask import Blueprint, abort, request, jsonify

domain = Blueprint('domain', __name__)

@domain.route('/api/domain',methods=['GET'])
def get_domain() :
    domain = request.args.get('value')
    domain_dict = {}

    if domain == None or is_domain(domain) is False or HUNTER_API_KEY == None or HUNTER_API_KEY == "":
        abort(400)

    domain_dict = hunter(str(domain))
    history = History()
    history.add_element(param_data=domain_dict, param_type="domain", param_args=[domain])
    return jsonify(domain_dict)

@domain.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@domain.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500