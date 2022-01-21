from rest_framework import serializers
from rooms.models.reservation import RoomReservation
from rooms.views.utils.get_reservation import get_reservation
from rooms.views.utils.get_user_room_date_time import get_user_room_date_time


class UpdateRoomReservationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=30)
    room_name = serializers.CharField(max_length=30)
    date = serializers.DateField()
    from_time = serializers.TimeField()
    to_time = serializers.TimeField()
    new_date = serializers.DateField()
    new_from_time = serializers.TimeField()
    new_to_time = serializers.TimeField()

    class Meta:

        model = RoomReservation
        fields = ['username',
                  'room_name',
                  'date',
                  'from_time',
                  'to_time',
                  'new_date',
                  'new_from_time',
                  'new_to_time']

    def validate(self, data):

        username = data['username']
        room_name = data['room_name']
        date = data['new_date']
        from_time = data['new_from_time']
        to_time = data['new_to_time']
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

    def update(self, instance, validated_data):

        instance.date_time.reserved_number -= 1
        instance.save()
        date_time = get_user_room_date_time(validated_data['username'],
                                            validated_data['room_name'],
                                            validated_data['new_date'],
                                            validated_data['new_from_time'],
                                            validated_data['new_to_time'])[2]
        instance.date_time = date_time
        date_time.reserved_number += 1
        instance.save()
        return instance
