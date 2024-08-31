from rest_framework import serializers

from . import models
from django.contrib.auth.models import User
from rest_framework import status

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields ='__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        # username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        # Check if a user with this username (email) already exists
        if User.objects.filter(username=email).exists():
            raise serializers.ValidationError({'email': 'A user with this email already exists.'})

        account = User(email=email, username=email, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)