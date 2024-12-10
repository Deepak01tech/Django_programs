from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_name(self, value):
        """Custom validation for the 'name' field."""
        for char in value:
            if char.isdigit():
                raise serializers.ValidationError('Name cannot contain numbers')
        return value