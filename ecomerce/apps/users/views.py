from django.contrib.auth import authenticate
from datetime import datetime

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.api.serializer import CustomTokenObtainPairSerializer
from apps.users.api.serializer import CustomUserSerializer
from apps.users.models import User


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Session Exitosa!.'
                }, status= status.HTTP_200_OK)
            
            else:
                return Response({'Error':'Datos invalidos'}, status= status.HTTP_401_UNAUTHORIZED)
        else:
                return Response({'Error':'Datos invalidos'}, status= status.HTTP_401_UNAUTHORIZED)
        

class Logout(GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id = request.data.get('user'))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message':'Session Cerrada Con Existo!.'}, status=status.HTTP_200_OK)
        
        return Response({'Error':'Datos invalidos'}, status= status.HTTP_401_UNAUTHORIZED)
        
        