from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tokens.api.serializers import RefreshTokenSerializer
from apps.tokens.models import RefreshToken
from apps.users.models import User
from apps.users.serializers import UserSerializer
import jwt
import datetime

from common.authentication.auth import JwtAuthentication
from common.authentication.utils import create_access_token, create_refresh_token, decode_token
from django.shortcuts import get_object_or_404


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        registration_data = request.data
        serializer = UserSerializer(data=registration_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        print(user.id)
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        access_token = create_access_token(user)
        refresh_token = create_refresh_token(user)

        token_data = {
            "user": user.id,
            "token": refresh_token
        }

        serializer = RefreshTokenSerializer(data=token_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            "auth_token": access_token,
            "refresh_token": refresh_token,
        }

        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = data
        return response


class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token') or request.META.get('HTTP_REFRESHTOKEN')
        if not refresh_token:
            raise AuthenticationFailed("Unauthorized")
        token_object = get_object_or_404(RefreshToken, token=refresh_token)
        try:
            payload = decode_token(refresh_token)
            user = User.objects.filter(email=payload['email']).first()
            access_token = create_access_token(user)
            renewed_token = create_refresh_token(user)

            token_data = {
                "token": renewed_token,
                "modified_on": datetime.datetime.utcnow(),
            }

            serializer = RefreshTokenSerializer(token_object, token_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthorized")

        data = {
            "auth_token": access_token,  # get and add new tokens here
            "refresh_token": renewed_token,  # get and add new tokens here
        }
        response = Response()
        response.set_cookie(key='refresh_token', value=renewed_token, httponly=True)
        response.data = data
        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('refresh_token')
        response.data = {
            "message": "Logged out successfully"
        }
        return response


class UserView(APIView):
    authentication_classes = (JwtAuthentication,)

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
