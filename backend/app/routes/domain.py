from flask import Blueprint, abort, request, jsonify
from app.services.domain import hunter
from app.utils.regex import is_domain
from app.utils.History import History
from app.utils.vars import HUNTER_API_KEY

domain = Blueprint('domain', __name__)

@domain.route('/api/domain',methods=['GET'])
def get_domain() :
    domain = request.args.get('value')
    domain_dict = {}

    if domain == None or is_domain(domain) is False or HUNTER_API_KEY == None:
        abort(400)

    domain_dict = hunter(str(domain))
    history = History()
    history.add_element(domain_dict, "domain", [domain])
    return jsonify(domain_dict)

@domain.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400