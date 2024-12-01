from flask import Flask, jsonify, request
from src.user_profile_matcher import views

app = Flask(__name__)

@app.route("/get_client_config/<player_id>", methods=["GET"])
def get_client_config(player_id):
    player_profile = views.get_player_profile(player_id=player_id)
    current_campaign = None
    if check_matchers(player_profile, current_campaign):
        update_player_profile(player_profile)

    result = player_profile
    if not result:
        return "not found", 404
    return jsonify(result), 200

def check_matchers(player_profile, current_campaign):
    pass

def update_player_profile(player_profile):
    pass

# @mock_data
# API get list CurrentCampains
