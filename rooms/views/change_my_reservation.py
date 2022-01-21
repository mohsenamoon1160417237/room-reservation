from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rooms.model_serializers.update_reservation import UpdateRoomReservationSerializer
from rooms.views.utils.get_reservation import get_reservation


class ChangeMyReservation(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        username = request.user.username
        room_name = data['room_name']
        date = data['date']
        from_time = data['from_time']
        to_time = data['to_time']
        serializer_data = {
            'username': username,
            'room_name': room_name,
            'date': date,
            'from_time': from_time,
            'to_time': to_time,
            'new_date': data['new_date'],
            'new_from_time': data['new_from_time'],
            'new_to_time': data['new_to_time']
        }

        reservation = get_reservation(username, room_name, date, from_time, to_time)
        serializer = UpdateRoomReservationSerializer(reservation, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = serializer_data
        response.data['status'] = 'changed reservation time'
        return response
