import jwt.exceptions
from rest_framework import authentication
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import User
from common.authentication.utils import decode_token


class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # token = request.COOKIES.get('auth_token') or request.META.get('HTTP_AUTHTOKEN')
        token = get_authorization_header(request).split()[1]
        # Header name should be Authorization and the value should be Bearer {Token value}

        if not token:
            raise AuthenticationFailed("Unauthorized")

        try:
            payload = decode_token(token)
            user = User.objects.filter(email=payload['email']).first()
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthorized")

        return (user, None)  # authentication successful
