from django.contrib.sessions.models import Session
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from apps.users.api.serializer import UserTokenSerializer



class UserToken(APIView):
    
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user = UserTokenSerializer().Meta.model.objects.filter(username = username).first())
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error':'Credenciales enviadas no validas'
            }, status= status.HTTP_400_BAD_REQUEST)



class Login(ObtainAuthToken):
    

    def post(self, request, *args, **kwargs):

        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response ({
                        'Token': token.key,
                        'User': user_serializer.data,
                        'message':'Inicio de Session Exitosa'
                        },status = status.HTTP_201_CREATED)
                else:
                    
                    #Filtra todas las sessiones que tengan un tiempo de expiracion igual o mayor al tiempo de la peticion mas reciente
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():

                        # Buscara en cada una de las sessiones que arroje la busquedad 
                        for session in all_sessions:
                            session_data = session.get_decoded()

                            # toma el numero del id del usuario que tiene la session abierta y
                            # lo compara con el id del usuario que quiere iniciar sesion, si es igual  lo eliminara
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()

                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response ({
                        'Token': token.key,
                        'User': user_serializer.data,
                        'message':'Inicio de Session Exitosa'
                        },status = status.HTTP_201_CREATED)
            else:
                return Response({'error':'Usuario No Autorizado'}, status= status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Usuario o Contraseña Incorrectos.'}, status= status.HTTP_400_BAD_REQUEST)


class logout(APIView):

    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            print(token)
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                
                token.delete()
                token_message = 'token eliminado!'
                session_message = 'Sessiones culminadas con exito!'

                return Response({'token_message':token_message, 'session_message':session_message},
                                status=status.HTTP_200_OK)
            
            return Response({'error':'No se ha encontrado un usuario con estas credenciales.'})
        
        except:
            return Response({'token no encontrado en la peticion'}, status=status.HTTP_409_CONFLICT)