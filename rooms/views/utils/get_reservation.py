from rooms.models.reservation import RoomReservation
from django.shortcuts import get_object_or_404
from .get_user_room_date_time import get_user_room_date_time


def get_reservation(username, room_name, date, from_time, to_time):

    data = get_user_room_date_time(username, room_name, date, from_time, to_time)
    user = data[0]
    room = data[1]
    date_time = data[2]

    reservation = get_object_or_404(RoomReservation,
                                    user__id=user.id,
                                    room__id=room.id,
                                    date_time__id=date_time.id,
                                    canceled=False)
    return reservation
