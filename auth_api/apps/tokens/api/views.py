from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RefreshTokenSerializer
from ..models import RefreshToken


# Create your views here.
class RefreshTokenView(APIView):
    ...
