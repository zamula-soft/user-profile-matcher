import logging
import sys

from src.external_service_list_campaigns.service_mocked_data import ExternalServiceListCampaigns
from src.user_profile_matcher import views
from src.user_profile_matcher.domain.model import Campaign, Matcher, PlayerProfile


LOGGING_LEVEL = logging.DEBUG
logging.basicConfig(stream=sys.stdout, level=LOGGING_LEVEL)

logger = logging.getLogger("SERVICES")


def check_matchers(player_profile_data: dict, matchers: Matcher) -> bool:
    """Check all avaible matchers"""
    if matchers.level:
        if "min" in matchers.level.keys():
            if player_profile_data.get("level") < matchers.level["min"]:
                return False
        if "max" in matchers.level.keys():
            if player_profile_data.get("level") > matchers.level["max"]:
                return False

    if matchers.has:
        if not("country" in matchers.has.keys() and player_profile_data.get("country") in matchers.has["country"]):
            return False
        if not("items" in matchers.has.keys()):
            return False
        else:
            matchers_has_items_list = matchers.has["items"]
            for item in matchers_has_items_list:
                if not(item in player_profile_data.get("inventory").keys()):
                    return False

    if matchers.does_not_have:
        if "items" in matchers.does_not_have.keys():
            matchers_does_not_have_items_list = matchers.does_not_have["items"]
            for item in matchers_does_not_have_items_list:
                if item in player_profile_data.get("inventory").keys():
                    return False

    return True


def update_player_profile_data(player_profile_data, campaign_name):
    """Add campaign to active campaigns in player profile"""
    player_profile_data["active_campaigns"].append(campaign_name)
    return player_profile_data

def get_client_config(player_id):
    player_profile_data = views.get_player_profile_data(player_id=player_id)

    external_service = ExternalServiceListCampaigns()
    campaigns = external_service.get_list_campaigns_data()

    for campaign_entry in campaigns:
        current_campaign = Campaign(**campaign_entry)
        if current_campaign.enabled:
            matcher_obj = Matcher(**current_campaign.matchers)
            if check_matchers(player_profile_data=player_profile_data, matchers=matcher_obj):
                player_profile_data = update_player_profile_data(player_profile_data=player_profile_data, campaign_name=current_campaign.name)

    return player_profile_data