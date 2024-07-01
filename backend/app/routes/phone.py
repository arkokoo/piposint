from app.services.phone import get_phone_info, format_phone
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify
import asyncio

phone = Blueprint('phone', __name__)

@phone.route('/api/phone', methods=['GET'])
def get_phone():
    """
    Retourne les informations d'un numéro de téléphone.
    ---
    tags:
      - Services
    parameters:
      - name: value
        in: query
        type: string
        required: true
        description: Numéro de téléphone à rechercher
    definitions:
      Phone:
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
            properties:
              country:
                type: string
              location:
                type: string
              carrier:
                type: string
              line_type:
                type: string
    responses:
      200:
        description: Informations du numéro de téléphone
        schema:
          $ref: '#/definitions/Phone'
      400:
        description: Bad Request, please ensure all parameters are provided
      500:
        description: Internal Server Error
    """

    phone_number = request.args.get('value')

    if phone_number == None:
        abort(400)
    
    phone_number = format_phone(phone_number)

    phone_dict = {
        "type": "phone",
        "args" : [phone_number],
        "data" : {}
    }

    output_phone = asyncio.run(get_phone_info(phone_number))
    output_phone.pop('phone_number', None)
    phone_dict["data"].update(output_phone)
    history = History()
    history.add_element(param_dict=phone_dict)

    return jsonify(phone_dict)

@phone.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@phone.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500