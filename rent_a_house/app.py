from flask import Flask

from rent_a_house.api import room
from rent_a_house.flask_settings import DevConfig, TestConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(room.blueprint)
    return app
