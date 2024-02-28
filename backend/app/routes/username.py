from flask import Blueprint, abort, request, jsonify
from app.services.username import get_blackbird

username = Blueprint('username', __name__)

@username.route('/api/username',methods=['GET'])
def get_username() :
    username = request.args.get('value')

    if username is None or username is "" :
        abort(400)

    userJson = get_blackbird(username)
    return jsonify(userJson)

@username.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400