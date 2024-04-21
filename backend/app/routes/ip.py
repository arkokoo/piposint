from app.utils.regex import is_ip_address
from app.utils.History import History
from app.services.ip import get_ip
from flask import Blueprint, abort, request, jsonify

ip = Blueprint('ip',__name__)

@ip.route('/api/ip',methods=['GET'])
def get_ip_information() :
    search_value = request.args.get('value')
    if search_value == None or is_ip_address(search_value) is False :
        abort(400)

    ip_address_dict = {}
    ip_address_dict = get_ip(search_value)
    history = History()
    history.add_element(param_data=ip_address_dict, param_type="ip", param_args=[search_value])
    return jsonify(ip_address_dict)

@ip.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@ip.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500