from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.user_profile_matcher import config, bootstrap
from src.user_profile_matcher.service_layer import services

# bus = bootstrap.bootstrap()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)

@app.route("/get_client_config/<player_id>", methods=["GET"])
def get_client_config_endpoint(player_id):
    try:
        player_profile = services.get_client_config(player_id=player_id)
    except Exception as e:
        return {"message": str(e)}, 400

    if not player_profile:
        return "not found", 404
    return jsonify(player_profile), 200
