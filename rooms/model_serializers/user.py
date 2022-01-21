from rest_framework import serializers
from user_register.models.user import UserRegister


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserRegister
        fields = ['username']