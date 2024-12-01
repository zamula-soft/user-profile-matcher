from flask import Flask, jsonify, request
from src.user_profile_matcher import views

app = Flask(__name__)

@app.route("/get_client_config/<player_id>", methods=["GET"])
def get_client_config(player_id):
    player_profile = views.get_player_profile(player_id=player_id)
    campaign_data = None
    if check_matches(player_profile, campaign_data):
        update_player_profile(player_profile)

    result = player_profile
    if not result:
        return "not found", 404
    return jsonify(result), 200
