from flask import Blueprint, abort, request, jsonify
import re
from app.services.email import get_holehe

EMAIL_FORMAT = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email = Blueprint('email', __name__)

@email.route('/api/email', methods=['GET'])
def get_email():
    email = request.args.get('value')

    associated_domains = []
    if email is None or bool(re.fullmatch(EMAIL_FORMAT, email)) is False:
        abort(400)
    
    associated_domains = get_holehe(email)
    return jsonify({"email": email, "associated_domains": associated_domains})

@email.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400