import abc
from src.user_profile_matcher.domain import model


class AbstractRepository(abc.ABC):
    def __init__(self):
        pass

    def get(self, player_id) -> model.PlayerProfile:
        player_profile = self._get(player_id=player_id)
        return player_profile

    @abc.abstractmethod
    def _get(self, player_id) -> model.PlayerProfile:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _get(self, player_id):
        return self.session.query(model.PlayerProfile).filter_by(player_id=player_id).first()
