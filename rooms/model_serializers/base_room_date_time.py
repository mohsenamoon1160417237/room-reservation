from rest_framework import serializers
from rooms.models.room_date_time import RoomDateTime
from rooms.models.room import Room
from django.shortcuts import get_object_or_404


class BaseRoomDateTimeSerializer(serializers.ModelSerializer):

    class Meta:

        model = RoomDateTime
        fields = ['date', 'from_time', 'to_time']

