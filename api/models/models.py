"""Module for User model."""
# System Imports
from datetime import datetime, timedelta

# Third party Imports
import jwt

# Local Imports
from main import db
from config import app_config


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

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save(self):
        """Creates a new user and saves to the database"""
        db.session.add(self)
        db.session.commit()

    def generate_token(self, user_id):
        """Generating the access token"""
        try:
            #set up payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=50),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(payload, app.secret_key, algorithm='HS256')
            return jwt_string

        except Exception as error:
            # return an error in string format if an exception occurs
            return str(error)

    @staticmethod
    def decode_token(token):
        """ Decodes the access token from the Authorization header. """
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, app.secret_key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # The token is expired, return an error string
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            #The token is invalid, return an error string
            return "Invalid token. Please register or login"

    def __repr__(self):
        return "<User: {}>".format(self.first_name)
