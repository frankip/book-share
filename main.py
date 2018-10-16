""" Initialize the flask app instance """

# System Imports
from os import getenv

# Third Party Imports
from flask import Flask, jsonify
from flask_restplus import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Local Imports
from api import api_blueprint
from api.middlewares.base_validator import (middleware_blueprint,
                                            ValidationError)
from config import app_config

config_name = getenv('FLASK_ENV', default='dev')

api = Api(api_blueprint, doc=False)

# initialize sql-alchemy
db = SQLAlchemy()


def initialize_errorhandlers(application):
    ''' Initialize error handlers '''
    application.register_blueprint(middleware_blueprint)
    application.register_blueprint(api_blueprint)


def create_app(config_name):
    """
    Initialize the app instance depending on the enviroment passed to it
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize error handlers
    initialize_errorhandlers(app)

    # bind app to db
    db.init_app(app)

    # initialize migration scripts
    migrate = Migrate(app, db)

    from api.models.models import Users

    # import views
    import api.views

    return app


@api.errorhandler(ValidationError)
@middleware_blueprint.app_errorhandler(ValidationError)
def handle_exception(error):
    """Error handler called when a ValidationError Exception is raised"""

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
