from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRegister(AbstractUser):

    user_type = models.CharField(max_length=30)

    def __str__(self):
        return self.username
