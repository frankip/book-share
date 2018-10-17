"""
Module for raising validation error
"""
# Third party Imports
from flask import Blueprint

middleware_blueprint = Blueprint('middleware', __name__)


class ValidationError(Exception):
    """
    Base class for handling validation errors
    """

    def __init__(self, error, status_code=None):
        Exception.__init__(self)
        self.status_code = 400
        self.error = error
        self.error['status'] = 'error'
        self.error['message'] = error['message']

        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return self.error
