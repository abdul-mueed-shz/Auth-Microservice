from django.urls import path
from .views import SendOtp

urlpatterns = [
    path('send-otp', SendOtp.as_view()),
]
