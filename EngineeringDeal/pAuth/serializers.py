from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2, max_length=200, default="")
    last_name = serializers.CharField(min_length=2, max_length=200, default="")
    username = serializers.CharField(max_length=255, min_length=2)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {'email', ('Email already exists')}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user',
                  'profile_pic',
                  'mobile_no',
                  'address',
                  'freelancer',
                  'seller']
