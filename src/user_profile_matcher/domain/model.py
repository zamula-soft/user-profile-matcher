import enum
import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Device:
    id: int
    model: str
    carrier: str
    firmware: str


@dataclass
class Inventory:
    id: int
    cash: int
    coins: int
    item_1: int
    item_34: int
    item_55: int


@dataclass
class Clan:
    id: str
    name: str



class Gender(enum.Enum):
    MALE = "male"
    FEMALE = "female"
    NONBINARY = "nonbinary"

@dataclass
class PlayerProfile:
    player_id: uuid.UUID
    credential: str
    created: datetime
    modified: datetime
    last_session: datetime
    total_spent: int
    total_refund: int
    total_transactions: int
    last_purchase: datetime
    active_campaigns: list[str]
    devices: list[Device]
    level: int
    xp: int
    total_playtime: int
    country: str
    language: str
    birthdate: datetime
    gender: Gender
    clan: Clan
    _customfield: str

    def update_player_profile(self, campaign_name):
        """Add campaign to active campaigns in player profile"""
        self.active_campaigns.append(campaign_name)

    @staticmethod
    def get_player_profile_from_data(player_profile_data):
        """Get data from player profile for PlayerProfileInstance"""
        _fields_dict = {}

        for field in PlayerProfile.__annotations__:
            if field in player_profile_data.keys():
                _fields_dict[field] = player_profile_data[field]
        return PlayerProfile(**_fields_dict)


@dataclass
class Matcher:
    level: dict # min 1 max 3
    has: dict # country items
    does_not_have: dict # items


@dataclass
class Campaign:
    game: str
    name: str
    priority: float
    matchers: dict
    start_date: datetime
    end_date: datetime
    enabled: bool
    last_updated: datetime
