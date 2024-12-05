import uuid

from src.user_profile_matcher.domain.model import PlayerProfile


def get_player_profile(player_profile_data) -> PlayerProfile:
    """Get data from player profile for PlayerProfileInstance"""
    _fields_dict = {}

    for field in PlayerProfile.__annotations__:
        if field in player_profile_data.keys():
            _fields_dict[field] = player_profile_data[field]

    return PlayerProfile(**_fields_dict)

def get_player_profile_data(player_id: uuid.UUID):
    """"""
    player_profile_data = {
        "player_id": "97983be2-98b7-11e7-90cf-082e5f28d836",
        "credential": "apple_credential",
        "created": "2021-01-10 13:37:17Z",
        "modified": "2021-01-23 13:37:17Z",
        "last_session": "2021-01-23 13:37:17Z",
        "total_spent": 400,
        "total_refund": 0,
        "total_transactions": 5,
        "last_purchase": "2021-01-22 13:37:17Z",
        "active_campaigns": [],
        "devices": [
            {
                "id": 1,
                "model": "apple iphone 11",
                "carrier": "vodafone",
                "firmware": "123"
            }
        ],
        "level": 3,
        "xp": 1000,
        "total_playtime": 144,
        "country": "CA",
        "language": "fr",
        "birthdate": "2000-01-10 13:37:17Z",
        "gender": "male",
        "inventory": {
            "cash": 123,
            "coins": 123,
            "item_1": 1,
            "item_34": 3,
            "item_55": 2
        },
        "clan": {
            "id": "123456",
            "name": "Hello world clan"
        },
        "_customfield": "mycustom"
    }

    return player_profile_data

