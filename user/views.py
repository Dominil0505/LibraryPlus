from django.shortcuts import render
from rest_framework.views import APIView

from user.serializers import CustomUserSerializer


# Create your views here.

# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = CustomUserSerializer(data = request.data)
#         if()