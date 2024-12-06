from datetime import datetime
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    UUID,
    DateTime,
    ForeignKey,
    Enum,
    Float,
    Boolean,
    JSON,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = MetaData()


class Clans(Base):
    __tablename__ = "clans"

    id = Column("id", String(255), primary_key=True, autoincrement=True)
    name = Column("name", String(255), nullable=False)


class Devices(Base):
    __tablename__ = "devices"

    id = Column("id", String(255), primary_key=True, autoincrement=True)
    model = Column("model", String(255))
    carrier = Column("carrier", String(255))
    firmware = Column("firmware", String(255))


class PlayerProfile(Base):
    __tablename__ = "player_profiles"

    player_id = Column("player_id", UUID, primary_key=True, autoincrement=True)
    credential = Column("credential", String(255))
    created = Column("created", DateTime, default=datetime.now)
    modified = Column(
        "modified", DateTime, default=datetime.now, onupdate=datetime.now
    )
    last_session = Column(
        "last_session", DateTime, default=datetime.now, onupdate=datetime.now
    )
    total_spent = Column("total_spent", Integer)
    total_refund = Column("total_refund", Integer)
    total_transactions = Column("total_transactions", Integer)
    last_purchase = Column("last_purchase", DateTime)
    level = Column("level", Integer)
    xp = Column("xp", Integer)
    total_playtime = Column("total_playtime", Integer)
    country = Column("country", String(2))
    language = Column("language", String(2))
    birthdate = Column("birthdate", DateTime)
    gender = Column(
        "gender",
        Enum("male", "female", "nonbinary", name="gender_enum", create_type=False),
    )
    _customfield = Column("_customfield", String(255))

    clan_id = Column("clan_id", Integer, ForeignKey("clans.id"))
    device_id = Column("device_id", Integer, ForeignKey("devices.id"))
    inventory_id = Column("inventory_id", Integer, ForeignKey("inventories.id"))

    def get_dict(self):
        """Get dict from attributes"""
        new_dict = {
            attr: value
            for attr, value in self.__dict__.items()
            if not callable(value)
            and not attr.startswith("__")
            and not (attr == "_sa_instance_state")
        }
        return new_dict


class Inventories(Base):
    __tablename__ = "inventories"

    id = Column("id", String(255), primary_key=True, autoincrement=True)
    cash = Column("cash", Integer)
    coins = Column("coins", Integer)
    item_1 = Column("item_1", Integer)
    item_34 = Column("item_34", Integer)
    item_55 = Column("item_55", Integer)


clans = Table(
    "clans",
    metadata,
    Column("id", String(255), primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
)

inventories = Table(
    "inventories",
    metadata,
    Column("player_id", ForeignKey("player_profiles.player_id"), primary_key=True),
    Column("cash", Integer),
    Column("coins", Integer),
    Column("item_1", Integer),
    Column("item_34", Integer),
    Column("item_55", Integer),
)

devices = Table(
    "devices",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("model", String(255)),
    Column("carrier", String(255)),
    Column("firmware", String(255)),
)

player_profiles = Table(
    "player_profiles",
    metadata,
    Column("player_id", UUID, primary_key=True, autoincrement=True),
    Column("clan", String(255), ForeignKey("clans.id")),
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
    Column(
        "gender",
        Enum("male", "female", "nonbinary", name="gender_enum", create_type=False),
    ),
    Column("_customfield", String(255)),
)

player_profiles_devices = Table(
    "player_profiles_devices",
    metadata,
    Column("player_id", ForeignKey("player_profiles.player_id")),
    Column("device_id", ForeignKey("devices.id")),
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
    Column("last_update", DateTime, default=datetime.now, onupdate=datetime.now),
)

player_profiles_campaigns = Table(
    "player_profiles_campaigns",
    metadata,
    Column("player_id", ForeignKey("player_profiles.player_id")),
    Column("campaign_id", ForeignKey("campaigns.id")),
)
