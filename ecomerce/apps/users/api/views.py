from rest_framework.views import APIView
from .serializer import UserSerializer, UserListSerializer
from apps.users.models import User
from rest_framework.response import Response
from rest_framework import status



class UserAPIView(APIView):

    def get(self, request):
        if request.method == "GET":
            # Solo traeremos los campos que necesitemos para no traer campos innecesarios que no usaremos
            queryset = User.objects.all().values('id','username','email','password')
            # .values() devuelve los datos en un diccionario 

            filtered_queryset = self.filter_queryset(queryset)

           # Muestra el usuario que se devuelva en el filtrado
            if filtered_queryset:
                serializer = UserListSerializer(filtered_queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            #Si el usuario pasado por parametro no existe manda un error 404
            elif not filtered_queryset :
                return Response({'Error':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Muestra la lista de usuarios
            else:
                users = User.objects.all()
                user_serializer = UserListSerializer(users, many = True)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            
    
    def post(self,request):
        if request.method == "POST":
            user_serializer = UserSerializer(data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'Menssage': 'Create user successfully'}, status= status.HTTP_201_CREATED)
            return Response(user_serializer.errors)
        
        
    # Busca el usuario por medio de 'id' que se le pase por parametro en la URL (?id=id)
    def filter_queryset(self, queryset):
        search_query = self.request.GET.get('id')
        if search_query:
            return queryset.filter(id =search_query)
        return queryset
    

    def put(self, request):
        if request.method == "PUT":
            user = User.objects.filter(id = request.data["id"]).first()
            user_serializer =  UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'Menssage': 'Update user successfully'}, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):

        if request.method == "DELETE":      
            user = User.objects.filter(username = self.request.GET.get("username")).first()
            user.delete()
            return Response({'message':'user successfully deleted'}, status=status.HTTP_200_OK)