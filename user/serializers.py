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
    
    def create(self, validated_data):
        role = validated_data.get('role_name', 'user')
        
        user = super().create(validated_data)

        if role == 'admin':
            user.is_superuser = True
            user.is_staff = True

        user.save()
        return user