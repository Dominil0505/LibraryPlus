from rest_framework.response import Response
from rest_framework import viewsets
from user.models import CustomUser
from user.serializers import AdminUserSerializer
from rest_framework.decorators import action
from rest_framework import status

from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer
    
    @action(detail= False, methods=['post'], url_path='create-admin', permission_classes=[permissions.IsAdminUser])
    def create_admin(self, request):
        serializer = AdminUserSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)