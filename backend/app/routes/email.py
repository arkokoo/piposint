from flask import Blueprint, abort, request, jsonify
from app.services.email import get_holehe
from app.utils.regex import is_email
from app.utils.History import History

email = Blueprint('email', __name__)

@email.route('/api/email', methods=['GET'])
def get_email():
    email = request.args.get('value')

    if email == None or is_email(email) is False:
        abort(400)
    
    email_dict = { "email": email, "associated_domains": []}
    email_dict["associated_domains"] = get_holehe(email)

    history = History()
    history.add_element(email_dict, "email", [email])

    return jsonify(email_dict)

@email.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400