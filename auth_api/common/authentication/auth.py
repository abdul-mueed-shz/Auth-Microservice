import jwt.exceptions
from rest_framework import authentication
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import User
from common.authentication.utils import decode_token
from common.constants.app_constants import UNAUTHORIZED


class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # token = request.COOKIES.get('auth_token') or request.META.get('HTTP_AUTHTOKEN')
        token = get_authorization_header(request)
        # Header name should be Authorization and the value should be Bearer {Token value}

        if not token:
            raise AuthenticationFailed(UNAUTHORIZED)
        token = token.split()[1]
        try:
            payload = decode_token(token)
            token_type = payload['type']
            if not token_type == 'access':
                raise AuthenticationFailed(UNAUTHORIZED)
            user = User.objects.filter(email=payload['email']).first()
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(UNAUTHORIZED)

        return (user, None)  # authentication successful
