import jwt
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import User


class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('auth_token') or request.META.get('HTTP_AUTHTOKEN')
        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = User.objects.filter(id=payload['id']).first()
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        return (user, None)  # authentication successful
