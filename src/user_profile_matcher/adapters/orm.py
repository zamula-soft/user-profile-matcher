from datetime import datetime

from sqlalchemy import Table, MetaData, Column, Integer, String, UUID, DateTime, ForeignKey, Enum, ARRAY, Float, \
    Boolean, JSON
from sqlalchemy.orm import mapper

from src.user_profile_matcher.domain import model

metadata = MetaData()

clans = Table(
    "clans",
    metadata,
    Column("id", primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False)
)

player_profiles = Table(
    "player_profiles",
    metadata,
    Column("player_id", UUID, primary_key=True, autoincrement=True),
    Column("clan", Integer, ForeignKey("clans.id")),
    Column("credential", String(255)),
    Column("created", DateTime, default=datetime.now),
    Column("modified", DateTime, default=datetime.now, onupdate=datetime.now),
    Column("last_session", DateTime, default=datetime.now, onupdate=datetime.now),
    Column("total_spent", Integer),
    Column("total_refund", Integer),
    Column("total_transactions", Integer),
    Column("last_purchase", DateTime),
    Column("level", Integer),
    Column("xp", Integer),
    Column("total_playtime", Integer),
    Column("country", String(2)),
    Column("language", String(2)),
    Column("birthdate", DateTime),
    Column("gender", Enum("male", "female", "nonbinary", name="gender_enum", create_type=False)),
    Column("_custom_field", String(255))
)

inventories = Table(
    "inventories",
    metadata,
    Column("player_id", ForeignKey("player_profiles.player_id"), primary_key=True),
    Column("cash", Integer),
    Column("coins", Integer),
    Column("item_1", Integer),
    Column("item_34", Integer),
    Column("item_55", Integer)
)

devices = Table(
    "devices",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("model", String(255)),
    Column("carrier", String(255)),
    Column("firmware", String(255)),
)

player_profiles_devices = Table(
    "player_profiles_devices",
    metadata,
    Column("player_id", ForeignKey("player_profiles.player_id")),
    Column("device_id", ForeignKey("devices.id"))
)

campaigns = Table(
    "campaigns",
    metadata,
    Column("id", primary_key=True, autoincrement=True),
    Column("game", String(255), nullable=False),
    Column("name", String(255), nullable=False),
    Column("priority", Float),
    Column("matchers", JSON, nullable=True),
    Column("start_date", DateTime),
    Column("end_date", DateTime),
    Column("enabled", Boolean),
    Column("last_update", DateTime, default=datetime.now, onupdate=datetime.now)
)

player_profiles_campaigns = Table(
    "player_profiles_campaigns",
    metadata,
    Column("player_id", ForeignKey("player_profiles.player_id")),
    Column("campaign_id", ForeignKey("campaigns.id"))
)

def create_mappers():
    devices_mapper = mapper(model.Device, devices)
    inventories_mapper = mapper(model.Inventory, inventories)
    clans_mapper = mapper(model.Clan, clans)
    player_profiles_mapper(
        model.PlayerProfile,
        player_profiles,
        {

        }
    )


