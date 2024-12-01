from dataclasses import dataclass
from datetime import datetime


@dataclass
class Devices:
    id: int
    model: str
    carrier: str
    firmware: str

@dataclass
class Inventory:
    cash: int
    coins: int
    item_1: int
    item_34: int
    item_55: int

@dataclass
class Clan:
    id: int
    name: str

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
    devices: list[Devices]
    level: int
    xp: int
    total_playtime: int
    country: str
    language: str
    birthdate: datetime
    gender: str
    clan: Clan
    _custom_field: str

@dataclass
class Matcher:
    level: bool # min 1 max 3
    has: bool # country items
    does_not_have: bool # items

@dataclass
class Campaign:
    game: str
    name: str
    priority: float
    matchers: Matcher
    start_date: datetime
    end_date: datetime
    enabled: bool
    last_update: datetime
