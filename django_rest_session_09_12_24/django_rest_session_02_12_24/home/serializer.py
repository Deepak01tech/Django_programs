from rest_framework import serializers
from .models import Student

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