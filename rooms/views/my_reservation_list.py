from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rooms.models.reservation import RoomReservation
from rooms.model_serializers.reservation_list import ReservationListSerializer


class MyReservationList(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        reservations = RoomReservation.objects.filter(user=request.user,
                                                      canceled=False)

        serializer = ReservationListSerializer(reservations, many=True)
        return Response(serializer.data)
        