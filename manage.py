"""app entry point."""

from os import getenv
from flask import jsonify
from flask_script import Manager
from main import create_app
from config import app_config

config_name = getenv('FLASK_ENV', default='production')

app = create_app(app_config[config_name])

manager = Manager(app)


@app.route('/')
def root():
    """ Dummy Endpoint for testing"""
    return jsonify({'hello': 'world'})


if __name__ == '__main__':
    manager.run()
