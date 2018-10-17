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
from api.utilities.validators.user_validator import UserAuthentication


@api.route('/registration')
class UserRegistrationResource(Resource):
    """ User Registration resource

    Resource class for registering user to the app
    """

    def post(self):
        """
        POST method for adding books.

        Payload should have the following parameters:
            name(str): name of the book
        """
        request_data = request.get_json()

        user_data_schema = UserSchema()
        user_data = user_data_schema.load_object_into_schema(request_data)

        user = UserAuthentication.user_creation(user_data)
        user.save()

        return {
            'status': 'success',
            'message': SUCCESS_MESSAGES['created'],
            'data': user_data_schema.dump(user).data
        }, 201


@api.route('/login')
class UserLoginResource(Resource):
    """ User Login Resource
    
    Resource class for loging in the user to the app
    """

    def post(self):
        request_data = request.get_json()

        user_data_schema = UserSchema()
        user_data = user_data_schema.load_object_into_schema(
            request_data, partial=True)

        user, access_token = UserAuthentication.user_login(user_data)

        return {
            'message': SUCCESS_MESSAGES['logged_in'],
            "user": user,
            "access_token": access_token.decode()
        }, 200
