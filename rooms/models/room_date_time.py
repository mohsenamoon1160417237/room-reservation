from django.db import models
from .room import Room


class RoomDateTime(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='date_times')
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    reserved_number = models.PositiveIntegerField(default=0)

    def is_filled(self):
        chr_number = self.room.chair_number
        if self.reserved_number == chr_number:
            return True
        return False

    def __str__(self):
        return str(self.date)
