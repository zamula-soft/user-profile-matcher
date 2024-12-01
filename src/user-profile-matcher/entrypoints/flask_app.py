from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get_client_config/<player_id>", methods=["GET"])
def get_client_config(player_id):
    result = "{'OK': 200}"
    if not result:
        return "not found", 404
    return jsonify(result), 200
