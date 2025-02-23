from rest_framework import serializers
from .models import User
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
