from django.db import models
from user_register.models.user import UserRegister
from .room import Room
from .room_date_time import RoomDateTime


class RoomReservation(models.Model):

    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    date_time = models.ForeignKey(RoomDateTime, on_delete=models.CASCADE, related_name='reservations')
    canceled = models.BooleanField(default=False)
    def __str__(self):

        return self.room
