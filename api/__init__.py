# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['config_name'])
    db.init(app)

    return app

