from app.services.phone import get_phone_info, format_phone
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify
import asyncio

phone = Blueprint('phone', __name__)

@phone.route('/api/phone', methods=['GET'])
def get_phone():
    phone_number = request.args.get('value')

    if phone_number == None:
        abort(400)
    
    phone_number = format_phone(phone_number)

    phone_dict = {
        "phone_number": phone_number
    }

    output_phone = asyncio.run(get_phone_info(phone_number))
    phone_dict.update(output_phone)
    history = History()
    history.add_element(param_data=phone_dict, param_type="phone", param_args=[phone_number])
    return jsonify(phone_dict)

@phone.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@phone.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500