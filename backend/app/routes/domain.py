from flask import Blueprint, abort, request, jsonify
from app.services.domain import hunter
from app.utils.regex import is_domain

domain = Blueprint('domain', __name__)

@domain.route('/api/domain',methods=['GET'])
def get_domain() :
    domain = request.args.get('value')
    json_data = {}

    if domain is None or is_domain(domain) is False :
        abort(400)

    json_data = hunter(str(domain))
    return jsonify(json_data)

@domain.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400