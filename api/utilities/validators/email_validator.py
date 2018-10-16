""" 
Module for validating emails
"""
# System Imports
import re

# Third party Imports
from marshmallow import ValidationError

# Local Imports
from api.utilities.messages.error_messages import SERIALIZATION_ERRORS


def email_validator(email):
    """
    Checks if given string is valid email
    
    Args:
        data (string) : email string

    Raises:
        ValidationError: Used to raise exception if email is not valid
    """

    data = email.lower()

    # Check if email pattern is matches
    if not re.search(r'[\w.-]+@[\w.-]+.\w+', email):
        raise ValidationError(SERIALIZATION_ERRORS['email_syntax'])
