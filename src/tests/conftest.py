import pytest
from sqlalchemy.orm import clear_mappers

from src.user_profile_matcher.adapters.orm import create_mappers


@pytest.fixture
def mappers():
    create_mappers()
    yield
    clear_mappers()
