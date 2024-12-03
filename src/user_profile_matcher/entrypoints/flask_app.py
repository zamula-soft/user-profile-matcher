from flask import Flask, jsonify, request

from src.external_service_list_campaigns.service_mocked_data import ExternalServiceListCampaigns
from src.user_profile_matcher import views

app = Flask(__name__)

@app.route("/get_client_config/<player_id>", methods=["GET"])
def get_client_config(player_id):
    player_profile = views.get_player_profile(player_id=player_id)

    external_service = ExternalServiceListCampaigns()
    current_campaign = external_service.get_list_campaigns_data()

    if check_matchers(player_profile, current_campaign):
        update_player_profile(player_profile)

    result = current_campaign
    if not result:
        return "not found", 404
    return jsonify(result), 200

def check_matchers(player_profile, current_campaign):
    pass

def update_player_profile(player_profile):
    pass
