from rest_framework import serializers
from home.models import UserPost, UserProfile
from django.contrib.auth.models import User


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ['id', 'user', 'caption', 'image', 'date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'userimage', 'bio', 'connection']
