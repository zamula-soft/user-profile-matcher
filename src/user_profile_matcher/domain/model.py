import enum
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
    id: int
    name: str

class Gender(enum.Enum):
    MALE = "male"
    FEMALE = "female"
    NONBINARY = "nonbinary"

@dataclass
class PlayerProfile:
    player_id: int
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
    _custom_field: str

@dataclass
class Matcher:
    level: dict # min 1 max 3
    has: dict # country items
    does_not_have: dict # items

@dataclass
class Campaign:
    campaign_id: int
    game: str
    name: str
    priority: float
    matchers: Matcher
    start_date: datetime
    end_date: datetime
    enabled: bool
    last_update: datetime
