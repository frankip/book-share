"""
Module for creating and checking if a user exist
"""

# Local imports
from api.models.models import Users
from api.middlewares.base_validator import ValidationError
from api.utilities.messages.error_messages import SERIALIZATION_ERRORS


class UserAuthentication:
    @classmethod
    def user_query(cla, email):
        """
        Querys the data base if email exist

        Args:
            email (str) : email string
        
        Returns:
            (object) : Returns User object
        """

        # check If user exists
        return Users.query.filter_by(email=email).first()

    @classmethod
    def user_creation(cls, data):
        """
        Handles user creation

        Args:
            data (dict) : request data
        
        Returns:
            (user instance) : Returns instantiated user object

        Raises:
            (ValidationError) : Used to raise exception if user object is present
        """

        if not cls.user_query(data.get('email')):
            try:
                user = Users(**data)
                return user

            except Exception as error:
                # An error occured, therefore return a string message containing the error
                raise ValidationError({'message': str(error)}, 400)
        else:
            raise ValidationError(
                {
                    'message': SERIALIZATION_ERRORS['user_exists']
                }, 409)

    @classmethod
    def user_login(cls, request_data):
        """
        Handles user login

        Args:
            request_data (dict): request data sent from client

        Returns:
            profile (string): full names of the user object
            access_token (string): jwt access token
        """
        cls.request_data = request_data

        # if not cls.request_data.get('email') and not cls.request_data.get(
        #         'password'):
        #     raise ValidationError(
        #         {
        #             'message': SERIALIZATION_ERRORS['empty_fields']
        #         }, 400)

        user = cls.user_query(cls.request_data.get('email'))
        profile = user.get_full_names()
        if user and user.verify_password(cls.request_data.get('password')):
            access_token = user.generate_token(user.id)
            return profile, access_token
        else:
            raise ValidationError(
                {
                    'message': SERIALIZATION_ERRORS['invalid_credentials']
                }, 401)
