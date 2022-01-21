from rest_framework import serializers
from user_register.models.user import UserRegister
from django.contrib.auth.models import Group


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserRegister
        fields = ['username', 'password', 'user_type']

    def create(self, validated_data):

        user_type = validated_data['user_type']
        user = UserRegister.objects.create(username=validated_data['username'],
                                           user_type=user_type)
        user.set_password(validated_data['password'])

        user.save()
        return user
