"""
Module for creating and checking if a user exist
"""

# Local imports
from api.models.models import Users
from api.middlewares.base_validator import ValidationError
from api.utilities.messages.error_messages import SERIALIZATION_ERRORS


def create_a_user(data):
    """
    checks if a user with similar email exists
    """
    # check If user exists
    user = Users.query.filter_by(email=data.get('email')).first()

    if not user:
        try:
            user = Users(**data)
            return user

        except Exception as error:
            # An error occured, therefore return a string message containing the error
            raise ValidationError({'message': str(error)}, 400)
    else:
        raise ValidationError({
            'message': SERIALIZATION_ERRORS['user_exists']
        }, 409)
