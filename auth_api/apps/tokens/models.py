from django.db import models

from apps.users.models import User


# Create your models here.
class RefreshToken(models.Model):
    token = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
