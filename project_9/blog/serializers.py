from rest_framework import serializers
from .models import User, Profile, Post, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProfileSerializer(serializers.ModelSerializer):
            class Meta:
                model = Profile
                fields = ('id', 'user', 'bio')
                depth = 1
                read_only_fields = ('id',)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'created_at')
        depth = 1
    def validate_content(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Content is too long')
        return value
