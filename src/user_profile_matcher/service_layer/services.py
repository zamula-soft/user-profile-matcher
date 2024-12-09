import uuid

from src.external_service_list_campaigns.service_mocked_data import (
    ExternalServiceListCampaigns,
)
from src.user_profile_matcher import views, config
from src.user_profile_matcher.domain.model import Campaign, Matcher
from src.user_profile_matcher.service_layer import unit_of_work

logger = config.get_logger("SERVICES")


def check_matchers(player_profile_data: dict, matchers: Matcher) -> bool:
    """Check all available matchers"""
    if matchers.level:
        if "min" in matchers.level.keys():
            if player_profile_data.get("level") < matchers.level["min"]:
                return False
        if "max" in matchers.level.keys():
            if player_profile_data.get("level") > matchers.level["max"]:
                return False

    if matchers.has:
        if not (
            "country" in matchers.has.keys()
            and player_profile_data.get("country") in matchers.has["country"]
        ):
            return False
        if not ("items" in matchers.has.keys()):
            return False
        else:
            matchers_has_items_list = matchers.has["items"]
            for item in matchers_has_items_list:
                if not (item in player_profile_data.get("inventory").keys()):
                    return False
    logger.info("2")
    if matchers.does_not_have:
        if "items" in matchers.does_not_have.keys():
            matchers_does_not_have_items_list = matchers.does_not_have["items"]
            for item in matchers_does_not_have_items_list:
                if item in player_profile_data.get("inventory").keys():
                    return False
    logger.info("3")
    return True


def update_player_profile_data(player_profile_data, campaign_name):
    """Add campaign to active campaigns in player profile"""
    if "active_campaigns" in player_profile_data.keys():
        player_profile_data["active_campaigns"].append(campaign_name)
    else:
        player_profile_data["active_campaigns"] = [campaign_name]
    return player_profile_data


def get_data_as_dict(player_profile, clan, device, inventory):
    player_profile_data = player_profile.get_dict()

    player_profile_data["clan"] = {"id": clan.id, "name": clan.name}
    player_profile_data.pop("clan_id")

    player_profile_data["device"] = {
        "id": device.id,
        "model": device.model,
        "carrier": device.carrier,
        "firmware": device.firmware,
    }
    player_profile_data.pop("device_id")

    player_profile_data["inventory"] = {
        "cash": inventory.cash,
        "coins": inventory.coins,
        "item_1": inventory.item_1,
        "item_34": inventory.item_34,
        "item_55": inventory.item_55,
    }
    player_profile_data.pop("inventory_id")

    return player_profile_data


def get_client_config(player_id: uuid.UUID, uow: unit_of_work.AbstractUnitOfWork):
    """Get player profile data to check matchers"""
    with uow:
        logger.debug("---------------------------------------------------")
        query_result = uow.player_profile.get(player_id=player_id)
        player_profile_data = get_data_as_dict(*query_result)

        external_service = ExternalServiceListCampaigns()
        campaigns = external_service.get_list_campaigns_data()

        for campaign_entry in campaigns:
            current_campaign = Campaign(**campaign_entry)
            if current_campaign.enabled:
                matcher_obj = Matcher(**current_campaign.matchers)
                if check_matchers(
                    player_profile_data=player_profile_data, matchers=matcher_obj
                ):
                    player_profile_data = update_player_profile_data(
                        player_profile_data=player_profile_data,
                        campaign_name=current_campaign.name,
                    )
                    logger.debug(player_profile_data)

    return player_profile_data
