"""Module for User model."""
# System Imports
from os import getenv
from datetime import datetime, timedelta
from sqlalchemy.orm import column_property
from sqlalchemy import select, func

# Third party Imports
import jwt
from passlib.apps import custom_app_context as pwd_context

# Local Imports
from main import db

# messages
from api.utilities.messages.error_messages import JWT_ERRORS

# Helpers
from api.middlewares.base_validator import ValidationError


class Users(db.Model):
    """
    This class handles all the logic and methods
    associated with a user
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256), nullable=False)
    books = db.relationship(
        'Books', backref='user', cascade="delete", lazy='dynamic')

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = pwd_context.encrypt(password)

    def save(self):
        """Creates a new user and saves to the database"""
        db.session.add(self)
        db.session.commit()

    def verify_password(self, password):
        """
        check pasword provided with hash in db

        Args:
            password (string): pasword string sent from the user

        Returns:
            bool: Returns True or false
        """
        return pwd_context.verify(password, self.password)

    def get_full_names(self):
        """
        Returns the full namesod user
        """
        return self.first_name + ' ' + self.last_name

    def generate_token(self, user_id):
        """
        Generating the access token

        Args:
            user_id (int): the user id

        Returns:
            access_token (str) : Returns access token
        """
        try:
            #set up payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=50),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            # create the byte string token using the payload and the SECRET key

            jwt_string = jwt.encode(
                payload, getenv('SECRET_KEY'), algorithm='HS256')
            return jwt_string

        except Exception as error:
            # return an error in string format if an exception occurs
            return str(error)

    @staticmethod
    def decode_token(token):
        """ Decodes the token 
        Decodes the access token from the Authorization header.
        Args:
            token (string) : token string 
        
        Returns: 
            userid (int): returns the user id 
        """
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, getenv('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # The token is expired, return an error string
            raise ValidationError({
                'message': JWT_ERRORS['token_expired']
            }, 401)
        except jwt.InvalidTokenError:
            #The token is invalid, return an error string
            raise ValidationError({
                'message': JWT_ERRORS['invalid_token']
            }, 401)

    @property
    def book_count(self):
        """
        Get book count for each user
        Returns:
            result(int): users count for corresponding roles
        """

        from api.models.models import Books

        query = select([func.count(
            Books.id)]).where(Books.uploded_by == self.id)
        result = db.engine.execute(query).scalar()
        return result

    def __repr__(self):
        return "<User: {}>".format(self.get_full_names)


class Books(db.Model):
    """
    This class handles all the logic and methods
    associated with a books
    """
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    uploded_by = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)

    def __init__(self, name, uploded_by):
        self.name = name
        self.uploded_by = uploded_by

    def save(self):
        """Creates a new user and saves to the database"""
        db.session.add(self)
        db.session.commit()
