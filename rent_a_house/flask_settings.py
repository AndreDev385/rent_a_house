class Config:
    """Base Config"""


class ProdConfig(Config):
    """Production Config"""

    ENV = "production"
    DEBUG = False


class DevConfig(Config):
    ENV = "development"
    DEBUG = True


class TestConfig(Config):
    ENV = "test"
    TESTING = True
    DEBUG = True
