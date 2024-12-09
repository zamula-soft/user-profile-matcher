import logging
import abc

from sqlalchemy.orm import join

from src.user_profile_matcher import config
from src.user_profile_matcher.adapters import orm
from src.user_profile_matcher.domain import model

logger = config.get_logger("REPOSITORY")


class AbstractRepository(abc.ABC):
    """Abstract repo"""

    def __init__(self):
        pass

    def get(self, player_id) -> model.PlayerProfile:
        player_profile = self._get(player_id=player_id)
        return player_profile

    @abc.abstractmethod
    def _get(self, player_id) -> model.PlayerProfile:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    """Real repo for DB management"""

    def __init__(self, session):
        super().__init__()
        self.session = session

    def _get(self, player_id):
        logger.debug(player_id)

        result = (
            self.session.query(
                orm.PlayerProfile,
                orm.Clans,
                orm.Devices,
                orm.Inventories,
            )
            .filter(
                orm.PlayerProfile.player_id == player_id,
            )
            .filter(
                orm.Clans.id == orm.PlayerProfile.clan_id,
            )
            .filter(
                orm.Devices.id == orm.PlayerProfile.device_id,
            )
            .filter(
                orm.Inventories.id == orm.PlayerProfile.inventory_id,
            )
            .first()
        )

        logger.debug(result)
        return result

class FakeRepository(AbstractRepository):
    def _get(self, player_id) -> model.PlayerProfile:
        pass
