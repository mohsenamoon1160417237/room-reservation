from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rooms.permissions.IsManager import IsManager
from rooms.model_serializers.room import RoomCreateSerializer
from rooms.models.room import Room
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class CreateUpdateDeleteRoom(GenericAPIView):

    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request):

        data = request.data

        name = data['name']

        serializer_data = {
            'name': name,
            'chair_number': data['chair_number']
        }

        rooms = Room.objects.filter(name=name)
        if rooms.exists():
            room = rooms[0]
            serializer = RoomCreateSerializer(room, data=serializer_data)
            status = 'updated room'
        else:
            serializer = RoomCreateSerializer(data=serializer_data)
            status = 'created room'

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = serializer_data
        response.data['status'] = status
        return response

    def delete(self, request):

        data = request.data
        name = data['name']
        room = get_object_or_404(Room, name=name)
        room.delete()
        return Response({'status': 'deleted room'})
