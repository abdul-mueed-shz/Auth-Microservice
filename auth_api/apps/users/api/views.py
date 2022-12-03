from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import UserSerializer
import jwt
import datetime

from common.authentication.auth import JwtAuthentication


# Create your views here.
class RegisterView(APIView):
    @staticmethod
    def post(request):
        registration_data = request.data
        serializer = UserSerializer(data=registration_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='auth_token', value=token, httponly=True)
        response.data = {
            "auth_token": token
        }
        return response


class LogoutView(APIView):
    @staticmethod
    def post(request):
        response = Response()
        response.delete_cookie('auth_token')
        response.data = {
            "message": "Logged out successfully"
        }
        return response


class UserView(APIView):
    authentication_classes = (JwtAuthentication,)

    @staticmethod
    def get(request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
