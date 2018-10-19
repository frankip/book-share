"""
Module for handling and manipulating book related actions
"""
# Third party Imports
from flask_restplus import Resource
from flask import Flask, request
from marshmallow import pprint

# local imports
from main import api

# Models
from api.models.models import Books, Users

# Schemas
from api.utilities.schemas.book_schema import BookSchema

# helpers
from api.decorators.token_decorator import authentication_request
from api.middlewares.base_validator import ValidationError

# messages
from api.utilities.messages.error_messages import JWT_ERRORS
from api.utilities.messages.success_messages import SUCCESS_MESSAGES


@api.route('/books')
class BookResource(Resource):
    """
    Resource class for peforming adding and viewing books
    """

    def post(self):
        """
        POST method for adding books.

        Payload should have the following parameters:
            name(str): name of the book
        """

        # Get the access token
        data = request.get_json()
        access_token = authentication_request()
        if access_token:
            # Attempt to decode the token and get the User ID
            user_id = Users.decode_token(access_token)

            data['uploded_by'] = user_id

            book_data_schema = BookSchema()
            book_data = book_data_schema.load_object_into_schema(data)

            book = Books(**book_data)
            book.save()
            return {
                'status': 'success',
                'message': SUCCESS_MESSAGES['created'],
                'data': book_data_schema.dump(book).data
            }, 201
        else:
            raise ValidationError({'message': JWT_ERRORS['no_token']}, 401)

    def get(self):
        """
        Get method getting all books.
        """
        books = Books.query.all()

        book_schema = BookSchema(many=True, exclude=['bookCount'])

        return {
            'status': 'success',
            'data': book_schema.dump(books).data,
            'message': SUCCESS_MESSAGES['fetched'].format('Books')
        }, 200
