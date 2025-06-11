from rest_framework import serializers

from .models import CustomUser
from djoser.serializers import UserCreateSerializer


class CustomUserSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'password',
        ]

class AdminUserSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'password'
        ]
        
    def create(self, validated_data):
        user = super().create(validated_data)
        
        user.is_superuser = True
        user.is_staff = True
        
        user.save()
        return user