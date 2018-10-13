"""
Module for handling user related activities
"""

# Third party Imports
from flask_restplus import Resource
from flask import Flask, request

# Local Imports
from main import api
from api.models.models import Users
from api.utilities.schemas.user_schema import UserSchema
from api.utilities.messages.success_messages import SUCCESS_MESSAGES
from api.utilities.validators.user_validator import create_a_user


@api.route('/registration')
class Registration(Resource):
    """
    Resource class for registering user to the app
    """

    def post(self):
        request_data = request.get_json()

        user_data_schema = UserSchema()
        user_data = user_data_schema.load_object_into_schema(request_data)

        user = create_a_user(user_data)
        user.save()

        return {
            'status': 'success',
            'message': SUCCESS_MESSAGES['created'],
            'data': user_data_schema.dump(user).data
        }, 201
