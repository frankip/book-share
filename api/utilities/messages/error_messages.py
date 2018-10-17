"""
contains all the error messages to be used in the app
"""

SERIALIZATION_ERRORS = {
    'field_required':
    "This field is required",
    'email_syntax':
    "Ensure that the email field is filled out correctly",
    'user_exists':
    "Sorry a user with that email already exists",
    'error':
    "An error occurred",
    'empty_fields':
    'Ensure that email field and password field are present',
    'invalid_credentials':
    'Invalid Email or Password, Please Try again',
    'books_number_exceed':
    'Sorry you can not add more books, you have reached the maximum limit'
}

JWT_ERRORS = {
    "token_expired": "Expired token. Please login to get a new token",
    "invalid_token": "Authorization failed due to an Invalid token.",
    "no_token": "Bad request. Header does not contain an authorization token."
}
