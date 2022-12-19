import jwt
import datetime


def create_token(user, expiration, token_type):
    return jwt.encode({
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        'type': token_type,
        "exp": datetime.datetime.utcnow() + expiration,
        "iat": datetime.datetime.utcnow()
    }, 'secret', algorithm='HS256')


def decode_token(token):
    return jwt.decode(token, 'secret', algorithms=['HS256'])


def create_access_token(user):
    return create_token(user, datetime.timedelta(seconds=45), 'access')


def create_refresh_token(user):
    return create_token(user, datetime.timedelta(minutes=30), 'refresh')
