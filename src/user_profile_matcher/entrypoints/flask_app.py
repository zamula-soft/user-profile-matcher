from flask import Flask, jsonify, request
from src.user_profile_matcher import views

app = Flask(__name__)

@app.route("/get_client_config/<player_id>", methods=["GET"])
def get_client_config(player_id):
    result = {'1': player_id}
    result = views.get_player_profile(player_id=player_id)
    if not result:
        return "not found", 404
    return jsonify(result), 200
