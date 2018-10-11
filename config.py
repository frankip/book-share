"""
Applications enviroment configuration settings
"""
from os import getenv


class Config:
    """
    Common configurations
    """

    SECRET_KEY = getenv('SECRET KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_DATABSE_URI = getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABSE_URI = getenv('TEST_DATABASE_URL')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
