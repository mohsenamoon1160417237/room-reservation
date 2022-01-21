from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rooms.permissions.IsManager import IsManager
from rooms.models.reservation import RoomReservation
from rest_framework.response import Response
from rooms.model_serializers.reservation_list import ReservationListSerializer


class ReservationList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):

        reservations = RoomReservation.objects.filter(canceled=False)
        serializer = ReservationListSerializer(reservations, many=True)
        return Response(serializer.data)
