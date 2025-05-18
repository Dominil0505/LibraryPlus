from rest_framework import serializers

from .models import CustomUser
from djoser.serializers import UserCreateSerializer


class CustomUserSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'role_name',
            'password',
        ]