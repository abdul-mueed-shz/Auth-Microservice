from django.urls import path
from .views import SendOtp

urlpatterns = [
    path('register', SendOtp.as_view()),
]
