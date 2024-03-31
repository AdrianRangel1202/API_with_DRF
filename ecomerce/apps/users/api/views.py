from rest_framework.views import APIView
from .serializer import UserSerializer
from apps.users.models import User
from rest_framework.response import Response
from rest_framework import status



class UserAPIView(APIView):

    def get(self, request):
        if request.method == "GET":

            queryset = User.objects.all()
            filtered_queryset = self.filter_queryset(queryset)

            if filtered_queryset:
                serializer = UserSerializer(filtered_queryset, many=True)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            
            elif not filtered_queryset :
                return Response({'Error':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
            else:
                users = User.objects.all()
                user_serializer = UserSerializer(users, many = True)
                return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
            
    
    def post(self,request):
        if request.method == "POST":
            user_serializer = UserSerializer(data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors)
        
        
    def filter_queryset(self, queryset):
        search_query = self.request.GET.get('username')
        if search_query:
            return queryset.filter(username__icontains=search_query)
        return queryset

    def put(self, request):
        if request.method == "PUT":
            user = User.objects.filter(username= request.data["username"]).first()
            user_serializer =  UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(user_serializer.errors)
        
    def delete(self,request):

        if request.method == "DELETE":      
            user = User.objects.filter(username = self.request.GET.get("username")).first()
            user.delete()
            return Response({'menssage':'user successfully deleted'}, status=status.HTTP_200_OK)