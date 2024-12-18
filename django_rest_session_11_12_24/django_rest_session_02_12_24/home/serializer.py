from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username','password']
    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        fields = '__all__'
        # exclude = ['id']
    def validate(self, data):

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError('name can not be numeric')
        return data