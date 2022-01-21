from rooms.models.room import Room
from user_register.models.user import UserRegister
from rooms.models.room_date_time import RoomDateTime
from django.shortcuts import get_object_or_404


def get_user_room_date_time(username, room_name, date, from_time, to_time):

    user = get_object_or_404(UserRegister, username=username)
    room = get_object_or_404(Room, name=room_name)
    date_time = get_object_or_404(RoomDateTime,
                                  room=room,
                                  date=date,
                                  from_time=from_time,
                                  to_time=to_time)
    return [user, room, date_time]
