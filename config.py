"""
Applications enviroment configuration settings
"""

# System Imports
from os import getenv


class Config:
    """
    Common configurations
    """

    SECRET_KEY = getenv('SECRET KEY', 'my_precious_secret_key')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://francky:postgres@localhost/book_share'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True


class TestingConfig(Config):
    """
    Testing configurations
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv('TEST_DATABASE_URI')


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
