from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math
import random

from rest_framework.views import APIView


class SendOtp(APIView):
    @staticmethod
    def generate_otp():
        digits = "0123456789"
        otp = ""
        for i in range(4):
            otp += digits[math.floor(random.random() * 10)]
        return otp

    @staticmethod
    def post(request):
        email = request.data.get('email')
        otp = generate_otp()
        htmlgen = '<p>Your OTP is <strong>otp</strong></p>'
        send_mail('OTP request', otp, '<your gmail id>', [email], fail_silently=False, html_message=htmlgen)
        ...


def generate_otp():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    return otp


def send_otp(request):
    email = request.GET.get("email")
    otp = generate_otp()
    htmlgen = '<p>Your OTP is <strong>o</strong></p>'
    send_mail('OTP request', otp, '<your gmail id>', [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(otp)
