import pytest
from rent_a_house.app import create_app
from rent_a_house.flask_settings import TestConfig


@pytest.fixture(scope="function")
def app():
    return create_app(TestConfig)
