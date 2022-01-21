from rest_framework import serializers
from rooms.models.reservation import RoomReservation
from .room import RoomCreateSerializer
from .base_room_date_time import BaseRoomDateTimeSerializer
from .user import UserSerializer


class ReservationListSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    room = RoomCreateSerializer()
    date_time = BaseRoomDateTimeSerializer()

    class Meta:

        model = RoomReservation
        fields = ['user', 'date_time', 'room']
