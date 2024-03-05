from flask import Blueprint, abort, request, jsonify
from app.utils.regex import is_ip_address
from app.services.ip import get_ip

ip = Blueprint('ip',__name__)

@ip.route('/api/ip',methods=['GET'])
def get_ip_information() :
    search_value = request.args.get('value')
    if search_value is None or is_ip_address(search_value) is False :
        abort(400)

    ip_address_dict = {}
    ip_address_dict = get_ip(search_value)

    return jsonify(ip_address_dict)

@ip.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided or are correctly wrote"}), 400