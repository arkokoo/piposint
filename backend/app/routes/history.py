from flask import Blueprint, abort, jsonify
from app.utils.History import History
import glob
import os
import json

history = Blueprint('history', __name__)

@history.route('/api/history', methods=['GET'])
def get_history():
    history = []

    hist = History()

    files = glob.glob(f"{hist.folder_path}/*.json")
    for file in files:
        try:
            with open(file, "r") as f:
                json_data = json.load(f)
                json_data.pop("data", None)
                history.append(json_data)
        except json.JSONDecodeError:
            continue
    return jsonify(history)

@history.route('/api/history', methods=['DELETE'])
def clear_history():
    hist = History()
    files = glob.glob(f"{hist.folder_path}/*.json")
    for file in files:
        os.remove(file)

    return jsonify({"message": "History cleared"})

@history.route('/api/history/<uuid>', methods=['GET'])
def get_history_element(uuid):
    hist = History()
    file = glob.glob(f"{hist.folder_path}/{uuid}.json")
    if uuid == None or uuid == "" or len(file) == 0:
        abort(400)
    with open(file[0], "r") as f:
        return jsonify(json.load(f))

@history.route('/api/history/<uuid>', methods=['DELETE'])
def delete_history_element(uuid):
    hist = History()
    file = glob.glob(f"{hist.folder_path}/{uuid}.json")
    if uuid == None or id == "" or len(file) == 0:
        abort(400)
    os.remove(file[0])
    return jsonify({"message": "History element deleted"})

@history.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@history.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error"}), 500