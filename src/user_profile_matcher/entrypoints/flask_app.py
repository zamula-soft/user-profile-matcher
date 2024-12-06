from http import HTTPStatus

from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.user_profile_matcher import config, bootstrap
from src.user_profile_matcher.service_layer import services, unit_of_work

# # bus = bootstrap.bootstrap()
# # # get_session = sessionmaker(bind=config.get_postgres_uri())
# get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)

@app.route("/get_client_config/<player_id>", methods=["GET"])
def get_client_config_endpoint(player_id):
    try:
        uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlAlchemyUnitOfWork()
        player_profile = services.get_client_config(player_id=player_id, uow=uow)
    except Exception as e:
        return {"message": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

    if not player_profile:
        return "not found", HTTPStatus.NOT_FOUND
    return jsonify(player_profile), HTTPStatus.OK
