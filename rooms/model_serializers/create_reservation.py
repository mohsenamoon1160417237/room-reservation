from rest_framework import serializers
from rooms.models.reservation import RoomReservation
from rooms.views.utils.get_reservation import get_reservation
from rooms.views.utils.get_user_room_date_time import get_user_room_date_time


class CreateRoomReservationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=30)
    room_name = serializers.CharField(max_length=30)
    date = serializers.DateField()
    from_time = serializers.TimeField()
    to_time = serializers.TimeField()

    class Meta:

        model = RoomReservation
        fields = ['username', 'room_name', 'date', 'from_time', 'to_time']

    def validate(self, data):

        username = data['username']
        room_name = data['room_name']
        date = data['date']
        from_time = data['from_time']
        to_time = data['to_time']
        result = get_user_room_date_time(username, room_name, date, from_time, to_time)
        user = result[0]
        room = result[1]
        date_time = result[2]
        if date_time.is_filled is True:
            raise serializers.ValidationError('This time is filled')
        reservations = RoomReservation.objects.filter(user=user,
                                                      room=room,
                                                      date_time=date_time,
                                                      canceled=False)
        if reservations.exists():
            raise serializers.ValidationError('Already reserved')

        return data

    def create(self, validated_data):

        data = get_user_room_date_time(validated_data['username'],
                                       validated_data['room_name'],
                                       validated_data['date'],
                                       validated_data['from_time'],
                                       validated_data['to_time'])
        user = data[0]
        room = data[1]
        date_time = data[2]
        reservation = RoomReservation.objects.create(user=user,
                                                     room=room,
                                                     date_time=date_time)
        date_time.reserved_number += 1
        date_time.save()
        return reservation
