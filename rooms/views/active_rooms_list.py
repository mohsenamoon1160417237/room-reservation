from rest_framework.generics import GenericAPIView
from rooms.models.room import Room
from rest_framework.permissions import IsAuthenticated
from rooms.models.room_date_time import RoomDateTime
from rest_framework.response import Response
from rooms.model_serializers.room_list import RoomListSerializer


class ActiveRoomsList(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        rooms = Room.objects.all()

        for room in rooms:
            date_time_count = RoomDateTime.objects.filter(room=room).count()
            if date_time_count == 0:
                name = room.name
                rooms = rooms.exclude(name=name)

        serializer = RoomListSerializer(rooms, many=True)
        return Response(serializer.data)
