from app.utils.regex import is_ip_address
from app.utils.History import History
from app.services.ip import get_ip
from flask import Blueprint, abort, request, jsonify

ip = Blueprint('ip',__name__)

@ip.route('/api/ip',methods=['GET'])
def get_ip_information() :
    """
    Retourne les informations d'une adresse IP.
    ---
    tags:
      - Services
    parameters:
      - name: value
        in: query
        type: string
        required: true
        description: Adresse IP à rechercher
    definitions:
      IP:
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
              asn:
                type: string
              isp:
                type: string
              country:
                type: string
              city:
                type: string
              region:
                type: string
              timezone:
                type: string
              latitude:
                type: number
              longitude:
                type: number
    responses:
      200:
        description: Informations de l'adresse IP
        schema:
          $ref: '#/definitions/IP'
      400:
        description: Bad Request, please ensure all parameters are provided
      500:
        description: Internal Server Error
    """

    search_value = request.args.get('value')
    if search_value == None or is_ip_address(search_value) is False :
        abort(400)

    ip_address_dict = {
        "type": "ip",
        "args": [search_value],
        "data": {}
    }

    ip_address_dict["data"] = get_ip(search_value)
    history = History()
    history.add_element(param_dict=ip_address_dict)
    return jsonify(ip_address_dict)

@ip.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@ip.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500