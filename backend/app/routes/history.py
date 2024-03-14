from flask import Blueprint, abort, jsonify
from app.utils.database import Database
from bson import ObjectId


history = Blueprint('history', __name__)

@history.route('/api/history', methods=['GET'])
def get_history():
    history = []

    db = Database().get_connection()

    history_collection = db["history"]
    history_data = history_collection.find({}, {"data": 0}).sort("datetime", -1)

    for data in history_data:
        data["_id"] = str(data["_id"])
        history.append(data)
    return jsonify(history)

@history.route('/api/history', methods=['DELETE'])
def clear_history():
    db = Database().get_connection()
    db.history.delete_many({})
    return jsonify({"message": "History cleared"})

@history.route('/api/history/<id>', methods=['GET'])
def get_history_element(id):
    db = Database().get_connection()
    if not ObjectId.is_valid(id) or db.history.find_one({"_id": ObjectId(id)}) == None:
        abort(400)
    history_element = db.history.find_one({"_id": ObjectId(id)})
    history_element["_id"] = str(history_element["_id"])
    return jsonify(history_element)

@history.route('/api/history/<id>', methods=['DELETE'])
def delete_history_element(id):
    db = Database().get_connection()
    if not ObjectId.is_valid(id) or db.history.find_one({"_id": ObjectId(id)}) == None:
        abort(400)
    db.history.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "History element deleted"})

@history.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@history.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error"}), 500