from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rooms.permissions.IsManager import IsManager
from rest_framework.response import Response
from rooms.views.utils.get_reservation import get_reservation
from rooms.views.utils.get_user_room_date_time import get_user_room_date_time



class CancelReservation(GenericAPIView):

    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request):

        data = request.data
        username = data['username']
        room_name = data['room_name']
        date = data['date']
        from_time = data['from_time']
        to_time = data['to_time']

        date_time = get_user_room_date_time(username, room_name, date, from_time, to_time)[2]
        reservation = get_reservation(username, room_name, date, from_time, to_time)
        reservation.canceled = True
        reservation.save()
        date_time.reserved_number -= 1
        date_time.save()
        return Response({'status': 'canceled reservation'})
