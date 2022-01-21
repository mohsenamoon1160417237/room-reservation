from rest_framework import serializers
from rooms.models.room import Room
from .base_room_date_time import BaseRoomDateTimeSerializer


class RoomListSerializer(serializers.HyperlinkedModelSerializer):

    date_times = BaseRoomDateTimeSerializer(many=True)

    class Meta:

        model = Room
        fields = ['name', 'chair_number', 'date_times']
