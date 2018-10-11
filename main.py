""" Initialize the flask app instance """

# Third Party Imports
from flask import Flask


def create_app(config):
    """
    Initialize the app instance depending on the enviroment passed to it
    """
    app = Flask(__name__)
    app.config.from_object(config)

    return app
