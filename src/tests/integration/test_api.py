from http import HTTPStatus

import requests
import uuid

import src.user_profile_matcher.service_layer.services
from src.user_profile_matcher.config import get_api_url
from src.user_profile_matcher import views


def test_get_config_profile_when_wrong_type_parameter_player_id_is_given():
    url = f"{get_api_url()}/get_client_config/abc"
    response = requests.get(url)
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_get_config_profile_when_correct_type_parameter_player_id_is_given_and_parameter_not_exist():
    url = f"{get_api_url()}/get_client_config/00000000-0000-0000-0000-000000000000"
    response = requests.get(url)
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_get_config_profile_when_mocking_result(mocker):
    correct_player_id = uuid.UUID("97983be2-98b7-11e7-90cf-082e5f28d836")
    mock_data = src.user_profile_matcher.views.get_player_profile_data(player_id=correct_player_id)
    mocker.patch(
        "src.user_profile_matcher.service_layer.services.get_client_config",
        return_value=mock_data
    )
    url = f"{get_api_url()}/get_client_config/{correct_player_id}"
    response = requests.get(url)
    assert response.status_code == HTTPStatus.OK
