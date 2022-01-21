from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rooms.model_serializers.create_reservation import CreateRoomReservationSerializer


class CreateReservation(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        username = request.user.username

        serializer_data = {
            'username': username,
            'room_name': data['room_name'],
            'date': data['date'],
            'from_time': data['from_time'],
            'to_time': data['to_time']
        }

        serializer = CreateRoomReservationSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = serializer_data
        response.data['status'] = 'created reservation'
        return response
