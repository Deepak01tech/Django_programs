from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'user', 'title', 'description',
            'due_date', 'priority', 'status',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    # Optional: Custom validation for `due_date`
    def validate_due_date(self, value):
        if value and value < serializers.DateField().to_representation(datetime.date.today()):
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
