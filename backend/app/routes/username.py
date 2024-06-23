from app.services.username import get_blackbird
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify

username = Blueprint('username', __name__)

@username.route('/api/username',methods=['GET'])
def get_username() :
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