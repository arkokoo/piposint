from app.services.website import wappalyzer
from app.utils.regex import is_website
from app.utils.History import History
from app.utils.vars import WAPPALYZER_API_KEY
from flask import Blueprint, abort, request, jsonify

website = Blueprint('website', __name__)

@website.route('/api/website',methods=['GET'])
def get_website() :
    website = request.args.get('value')
    website_dict = {}

    if website == None or is_website(website) is False or WAPPALYZER_API_KEY == None or WAPPALYZER_API_KEY == "":
        abort(400)

    website_dict = wappalyzer(str(website))
    history = History()
    history.add_element(param_data=website_dict, param_type="website", param_args=[website])
    return jsonify(website_dict)

@website.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@website.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error", "description": error.description}), 500