from app.services.username import get_blackbird
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify

username = Blueprint('username', __name__)

@username.route('/api/username',methods=['GET'])
def get_username() :
    """
    Retourne les informations d'un nom d'utilisateur.
    ---
    tags:
      - Services
    parameters:
      - name: value
        in: query
        type: string
        required: true
        description: Nom d'utilisateur à rechercher
    definitions:
      Username:
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
              sites:
                type: array
                items:
                  type: object
                  properties:
                    app:
                      type: string
                    metadata:
                      type: array
                      items:
                        type: string
                    url:
                      type: string
    responses:
      200:
        description: Informations du nom d'utilisateur
        schema:
          $ref: '#/definitions/Username'
      400:
        description: Bad Request, please ensure all parameters are provided
      500:
        description: Internal Server Error
    """


    username = request.args.get('value')

    if username == None or username == "" :
        abort(400)

    user_dict = {
        "type": "username",
        "args": [username],
        "data": {}
    }
    output_username = get_blackbird(username)
    output_username.pop('search-params', None)
    user_dict["data"].update(output_username)
    history = History()
    history.add_element(param_dict=user_dict)
    return jsonify(user_dict)

@username.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400