from flask import Blueprint, abort, request, jsonify
from app.services.username import get_blackbird
from app.utils.database import Database

username = Blueprint('username', __name__)

@username.route('/api/username',methods=['GET'])
def get_username() :
    username = request.args.get('value')

    if username == None or username is "" :
        abort(400)

    user_dict = {}
    user_dict = get_blackbird(username)
    Database.add_history_element(user_dict, "username", [username])
    return jsonify(user_dict)

@username.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400