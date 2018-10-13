"""app entry point."""

# System Imports
from os import getenv

# Third party Imports
from flask import jsonify
from flask_script import Manager

# Local Imports
from main import create_app
from config import app_config

config_name = getenv('FLASK_ENV', default='prod')
app = create_app(app_config[config_name])

if __name__ == '__main__':
    app.run()
