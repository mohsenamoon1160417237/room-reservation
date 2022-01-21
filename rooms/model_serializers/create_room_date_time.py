from rest_framework import serializers
from rooms.models.room_date_time import RoomDateTime
from rooms.models.room import Room
from django.shortcuts import get_object_or_404


class CreateRoomDateTimeSerializer(serializers.ModelSerializer):

    room_name = serializers.CharField(max_length=30)

    class Meta:

        model = RoomDateTime
        fields = ['room_name', 'date', 'from_time', 'to_time']

    def validate(self, data):

        date = data['date']
        from_time = data['from_time']
        room = get_object_or_404(Room, name=data['room_name'])
        date_times = RoomDateTime.objects.filter(room=room,
                                                    date=date)
        for date_time in date_times:
            prev_from_time = date_time.from_time
            prev_to_time = date_time.to_time
            prev_date = date_time.date
            if prev_date == date:
                if prev_from_time == from_time:
                    raise serializers.ValidationError('conflict with previous date times')
                elif (from_time > prev_from_time) and (from_time < prev_to_time):
                    raise serializers.ValidationError('conflict with previous date times')

        return data

    def create(self, validated_data):

        room = get_object_or_404(Room, name=validated_data['room_name'])

        room_date_time = RoomDateTime.objects.create(date=validated_data['date'],
                                                     from_time=validated_data['from_time'],
                                                     to_time=validated_data['to_time'],
                                                     room=room)
        return room_date_time
