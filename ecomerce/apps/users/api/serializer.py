from rest_framework import serializers
from apps.users.models import User




# Serializador para mostrar usuarios autenticados por Token

class UserTokenSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ('username','email','name', 'last_name')

# Serializador para crear y actualizar usuarios
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user





# Serializador para mostrar usuarios
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    # Lista los datos solo con los campos descritos
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }