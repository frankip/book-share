""" 
Module for validating emails
"""
# System Imports
import re

# Third party Imports
from marshmallow import ValidationError

# Local Imports
from api.utilities.messages.error_messages import SERIALIZATION_ERRORS


def email_validator(data):
    """
    Checks if given string is valid email
    """

    data = data.lower()

    # Check if email pattern is matches
    if not re.search(r'[\w.-]+@[\w.-]+.\w+', data):
        raise ValidationError(SERIALIZATION_ERRORS['email_syntax'])
