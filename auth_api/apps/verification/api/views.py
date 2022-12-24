from django.core.exceptions import BadRequest
from django.core.mail import send_mail
import math
import random

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils.app_utils import verify_email
from common.utils.encryption import encrypt
from django.conf import settings


class SendOtp(APIView):
    @staticmethod
    def generate_otp(digits='0123456789', max_length=4):
        otp = ""
        for i in range(max_length):
            otp += digits[math.floor(random.random() * 10)]
        return otp

    def post(self, request):
        response = Response()
        if not (settings.CRYPTO_CIPHER_KEY or settings.CRYPTO_CIPHER_IV):
            response.data = {"error": "Encryption error!"}
            response.status_code = 500
            return response

        email = request.data.get('email')
        if not verify_email(email):
            # raise BadRequest('Invalid Email!')
            response.data = {"error": "Invalid Email!"}
            response.status_code = 400
            return response

        otp = self.generate_otp(max_length=settings.OTP_LENGTH)
        try:
            htmlgen = '<div ' \
                      'style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">' \
                      ' <div ' \
                      'style="margin:50px auto;width:70%;padding:20px 0"> ' \
                      '<div style="border-bottom:1px solid #eee"> ' \
                      '<a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">' \
                      'abdul.mueed.shz.dev@gmail.com' \
                      '</a> ' \
                      '</div> ' \
                      '<p style="font-size:1.1em">Hi,</p> ' \
                      '<p>Thank you for choosing abdul.mueed.shz.dev authentication application. ' \
                      'Use the following OTP to complete your Sign Up procedures. </p> ' \
                      '<h2 style="background: #00466a;margin: 0 auto;width: ' \
                      f'max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{otp}</h2> ' \
                      '<p style="font-size:0.9em;">Regards,<br />abdul.mueed.shz.dev@gmail.com</p> ' \
                      '<hr style="border:none;border-top:1px solid #eee" /> ' \
                      '<div style="float:right;padding:8px 0;color:#aaa;' \
                      'font-size:0.8em;line-height:1;font-weight:300"> ' \
                      '<p>abdul.mueed.shz.dev@gmail.com</p>' \
                      '<p>136 Shah Jamal</p> ' \
                      '<p>Lahore</p> ' \
                      '</div>' \
                      ' </div>' \
                      ' </div>'

            send_mail('OTP request', otp, 'abdul.mueed.shz.dev@gmail.com', [email], fail_silently=False,
                      html_message=htmlgen)

            encrypted_otp = encrypt(otp, settings.CRYPTO_CIPHER_KEY, settings.CRYPTO_CIPHER_IV)
            response.data = {
                "token": encrypted_otp,
            }
            return response

        except ValidationError:
            raise ValidationError('Unable to send OTP')
