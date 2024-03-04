import asyncio
from flask import Blueprint, abort, request, jsonify
from app.services.phone import get_phone_info

phone = Blueprint('phone', __name__)

@phone.route('/api/phone', methods=['GET'])
def get_phone():
    phone_number = request.args.get('value')

    if phone_number is None:
        abort(400)

    phone_dict = {
        "phone_number": phone_number
    }

    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    output_phone = asyncio.run(get_phone_info(phone_number))
    phone_dict.update(output_phone)
    return jsonify(phone_dict)

@phone.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@phone.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error"}), 500