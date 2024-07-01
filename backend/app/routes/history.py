from app.utils.History import History, get_overpass_turbo_args
from flask import Blueprint, abort, jsonify, request
import glob
import os
import json
from datetime import datetime

history = Blueprint('history', __name__)

@history.route('/api/history', methods=['GET'])
def get_history():
    """
    Retourne l'historique de toutes les requêtes effectuées.
    ---
    tags:
      - History
    definitions:
      History:
        type: object
        properties:
          Year:
            type: object
            properties:
              Month:
                type: object
                properties:
                  Day:
                    type: array
                    items:
                      $ref: '#/definitions/HistoryElement'
      HistoryElement:
        type: object
        properties:
          args:
            type: array
            items:
              type: string
          datetime:
            type: string
          uuid:
            type: string
          type:
            type: string
          data:
            type: object
    responses:
      200:
        description: Historique des requêtes effectuées
        schema:
          $ref: '#/definitions/History'
      500:
        description: Internal Server Error
    """

    history = {}

    hist = History()

    files = glob.glob(f"{hist.folder_path}/*.json")
    for file in files:
        try:
            with open(file, "r") as f:
                json_data = json.load(f)
                json_data.pop("data", None)

                datetime = json_data["datetime"]
                year = datetime[0:4]
                month = datetime[5:7]
                day = datetime[8:10]

                if year not in history:
                    history[year] = {}
                if month not in history[year]:
                    history[year][month] = {}
                if day not in history[year][month]:
                    history[year][month][day] = []

                history[year][month][day].append(json_data)
        except json.JSONDecodeError:
            continue
    return jsonify(history)

@history.route('/api/history', methods=['DELETE'])
def clear_history():
    """
    Supprime l'historique de toutes les requêtes effectuées.
    ---
    tags:
      - History
    responses:
        200:
            description: History cleared
        500:
            description: Internal Server Error
    """

    hist = History()
    files = glob.glob(f"{hist.folder_path}/*.json")
    for file in files:
        os.remove(file)

    return jsonify({"message": "History cleared"})

@history.route('/api/history', methods=['POST'])
def add_history_element():
    """
    Ajoute une requête à l'historique.
    ---
    tags:
      - History
    parameters:
        - name: service
          in: body
          type: string
          required: true
          description: Nom du service
        - name: data
          in: body
          type: object
          required: true
          description: Paramètres de la requête
    responses:
        200:
            description: History element added
        400:
            description: Bad Request, please ensure all parameters are provided
        500:
            description: Internal Server Error
    """

    hist = History()
    data = request.json
    if data is None:
        abort(400)

    service_name = data["service"]
    data.pop("service")

    service_dict = {
        "type": service_name,
        "args": [],
        "data": data
    }

    service_dict["args"] = get_overpass_turbo_args(service_name, data)

    hist.add_element(param_dict=service_dict)
    return jsonify({"message": "History element added"})

@history.route('/api/history/<uuid>', methods=['GET'])
def get_history_element(uuid):
    """
    Retourne un élément de l'historique.
    ---
    tags:
      - History
    parameters:
        - name: uuid
          in: path
          type: string
          required: true
          description: UUID de la requête
    responses:
        200:
            description: Contenu de l'élément de l'historique
            schema:
                $ref: '#/definitions/HistoryElement'
        500:
            description: Internal Server Error
    """

    hist = History()
    file = glob.glob(f"{hist.folder_path}/{uuid}.json")
    if uuid == None or uuid == "" or len(file) == 0:
        abort(404)
    with open(file[0], "r") as f:
        return jsonify(json.load(f))

@history.route('/api/history/<uuid>', methods=['DELETE'])
def delete_history_element(uuid):
    """
    Supprime un élément de l'historique.
    ---
    tags:
      - History
    parameters:
        - name: uuid
          in: path
          type: string
          required: true
          description: UUID de la requête
    responses:
        200:
            description: History element deleted
        404:
            description: History element not found
        500:
            description: Internal Server Error
    """

    hist = History()
    file = glob.glob(f"{hist.folder_path}/{uuid}.json")
    if uuid == None or id == "" or len(file) == 0:
        abort(404)
    os.remove(file[0])
    return jsonify({"message": "History element deleted"})

@history.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request, please ensure all parameters are provided"}), 400

@history.errorhandler(404)
def bad_request(error):
    return jsonify({"error": "History element not found"}), 404

@history.errorhandler(500)
def bad_request(error):
    return jsonify({"error": "Internal Server Error"}), 500