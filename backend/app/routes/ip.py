from flask import Blueprint, abort, request, jsonify
from app.utils.ip.ip_regex import regex_compare
from app.services.ip import get_ip

ip = Blueprint('ip',__name__)

@ip.route('/api/ip',methods=['GET'])
def get_ip_information() :
    information_json = {}
    search_value = request.args.get('value')
    if search_value is None :
        abort(400)
    if regex_compare(search_value) is False :
        abort(400)

    information_json = get_ip(search_value)
    return jsonify(information_json)

@ip.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided or are correctly wrote"}), 400