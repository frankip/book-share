"""
Books model serializer
"""
# Third Party Imports
from marshmallow import fields, post_dump

# Local Imports
from api.utilities.schemas.base_schema import AuditableBaseSchema
from api.utilities.messages.error_messages import SERIALIZATION_ERRORS
from api.utilities.schemas.user_schema import UserSchema
from api.middlewares.base_validator import ValidationError


class BookSchema(AuditableBaseSchema):
    """
    book model schema
    """
    id = fields.String()
    name = fields.String(
        required=True,
        error_messages={'required': SERIALIZATION_ERRORS['field_required']})
    uploded_by = fields.Integer(
        load_only=True,
        required=True,
        error_messages={'required': SERIALIZATION_ERRORS['field_required']})

    user = fields.Nested(
        UserSchema,
        dump_only=True,
        dump_to="user",
        only=['full_names', 'book_count'])

    @post_dump(pass_many=True)
    def validate_book_count(self, data, many):
        """ find the book count

        validate that the book count is not more than 10

        Args:
            data (dict) : validated serialized data
        
        Raises:
            ValidationError: raises validation if book count is grater than 10
        """
        if isinstance(data,
                      dict) and data.get('user').get('bookCount', 0) > 10:
            raise ValidationError(
                {
                    'message': SERIALIZATION_ERRORS['books_number_exceed']
                }, 400)
