from app.services.username import get_blackbird
from app.utils.History import History
from flask import Blueprint, abort, request, jsonify

username = Blueprint('username', __name__)

@username.route('/api/username',methods=['GET'])
def get_username() :
    username = request.args.get('value')

    if username == None or username == "" :
        abort(400)

    user_dict = {}
    user_dict = get_blackbird(username)
    history = History()
    history.add_element(param_data=user_dict, param_type="username", param_args=[username])
    return jsonify(user_dict)

@username.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400