from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rooms.permissions.IsManager import IsManager
from rooms.model_serializers.create_room_date_time import CreateRoomDateTimeSerializer
from rooms.models.room import Room
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rooms.models.room_date_time import RoomDateTime


class CreateDeleteRoomDateTime(GenericAPIView):

    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, room_name):

        data = request.data
        room = get_object_or_404(Room, name=room_name)
        serializer_data = {
            'date': data['date'],
            'from_time': data['from_time'],
            'to_time': data['to_time'],
            'room_name': room_name
        }

        serializer = CreateRoomDateTimeSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(room=room)
        response = Response()
        response.data = serializer_data
        response.data['status'] = 'created room date time'
        return response

    def delete(self, request, room_name):

        data = request.data
        room = get_object_or_404(Room, name=room_name)
        date = data['date']
        from_time = data['from_time']
        to_time = data['to_time']
        room_datetime = get_object_or_404(RoomDateTime,
                                          room=room,
                                          date=date,
                                          from_time=from_time,
                                          to_time=to_time)
        room_datetime.delete()
        return Response({'status': 'deleted room date time'})
