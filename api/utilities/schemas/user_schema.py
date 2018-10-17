""" 
User model serializer 
"""
# Third Party Imports
from marshmallow import fields, post_load

# Local Imports
from api.utilities.schemas.base_schema import AuditableBaseSchema
from api.utilities.messages.error_messages import SERIALIZATION_ERRORS
from api.utilities.validators.email_validator import email_validator


class UserSchema(AuditableBaseSchema):
    """ user model schema

    Schema object for serializing the user object fields
    """
    id = fields.String()
    first_name = fields.String(
        load_from='firstname',
        dump_to='firstname',
        required=True,
        error_messages={'required': SERIALIZATION_ERRORS['field_required']})
    last_name = fields.String(
        load_from='lastname',
        dump_to='lastname',
        required=True,
        error_messages={'required': SERIALIZATION_ERRORS['field_required']})
    email = fields.String(
        required=True,
        error_messages={'required': SERIALIZATION_ERRORS['field_required']},
        validate=email_validator)
    password = fields.String(
        required=True,
        load_only=True,
        error_messages={'required': SERIALIZATION_ERRORS['field_required']})

    book_count = fields.Integer(dump_to='bookCount', dump_only=True)

    full_names = fields.Method('get_full_names', dump_to="names")

    def get_full_names(self, obj):
        """ Get the full names of user

        Generates the full names of the user

        Args:
            object (dict): The object to be serialized
        """
        return obj.first_name + ' ' + obj.last_name
