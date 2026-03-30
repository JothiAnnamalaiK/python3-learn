from flask import jsonify


def api_response(success, message, data=None, status=200):
    response = {"success": success, "message": message, "data": data}
    return jsonify(response), status  # FOR SENDING JSON RESPONSE WITH STATUS CODE
