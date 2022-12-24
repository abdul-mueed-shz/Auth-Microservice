from rest_framework import serializers
from ..models import RefreshToken
from ...users.models import User


class RefreshTokenSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = RefreshToken
        fields = [
            'id',
            'token',
            'user',
            'modified_on'
        ]
